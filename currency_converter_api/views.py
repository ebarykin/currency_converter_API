from pydantic import ValidationError
from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import status
from .serializers import ConvertCurrencyModel
from .services import get_exchange_rate
from decimal import Decimal
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes, OpenApiExample


SUPPORTED_CURRENCIES = ["USD", "EUR", "RUB", "GBP", "JPY", "AUD"]


@extend_schema(
    parameters=[
        OpenApiParameter(
            name='from',
            type=OpenApiTypes.STR,
            description=f'Исходная валюта (доступные валюты: {SUPPORTED_CURRENCIES})',
            enum=SUPPORTED_CURRENCIES,
            examples=[
                OpenApiExample('Пример исходной валюты', value='USD')
            ],
            required=True
        ),
        OpenApiParameter(
            name='to',
            type=OpenApiTypes.STR,
            description=f'Целевая валюта (доступные валюты: {SUPPORTED_CURRENCIES})',
            enum=SUPPORTED_CURRENCIES,
            examples=[
                OpenApiExample('Пример целевой валюты', value='EUR')
            ],
            required=True
        ),
        OpenApiParameter(
            name='value',
            type=OpenApiTypes.NUMBER,
            description='Сумма для конвертации (по умолчанию: 1)',
            examples=[
                OpenApiExample('Пример суммы', value=100)
            ],
            required=False
        ),
    ],
    description=f"API для конвертации валют. Поддерживаемые валюты: {SUPPORTED_CURRENCIES}"
)
@api_view(['GET'])
def convert_currency(request):
    """
    Конвертирует сумму из одной валюты в другую.

    Параметры:
        request (HttpRequest): HTTP-запрос с параметрами:
            - 'from' (str): Исходная валюта (обязательный).
            - 'to' (str): Целевая валюта (обязательный).
            - 'value' (float, необязательный): Сумма для конвертации (по умолчанию 1).

    Исключения:
        ValidationError: Некорректные данные валют.
        APIException: Ошибка при получении курса обмена.

    Возвращает:
        Response: JSON с результатом конвертации или описанием ошибки.
    """
    try:
        data = ConvertCurrencyModel(
            from_currency=request.GET.get('from'),
            to_currency=request.GET.get('to'),
            value=request.GET.get('value', 1)
        )
    except ValidationError as e:
        return Response({"errors": e.errors()}, status=status.HTTP_400_BAD_REQUEST)
    except APIException as e:
        return Response({"errors": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    exchange_rate = get_exchange_rate(data.from_currency, data.to_currency)
    result = data.value * Decimal(exchange_rate)
    return Response({"result": round(result, 2)})
