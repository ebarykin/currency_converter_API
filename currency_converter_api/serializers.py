from pydantic import BaseModel, constr, condecimal, conint


class ConvertCurrencyModel(BaseModel):
    """Модель для конвертации валют (from, to: 3 символа; value: > 0)."""
    from_currency: constr(min_length=3, max_length=3)
    to_currency: constr(min_length=3, max_length=3)
    value: condecimal(gt=0)

