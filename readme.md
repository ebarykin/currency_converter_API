# Currency Converter API

## Описание

Currency Converter API предоставляет интерфейс для конвертации валют. Поддерживаемые валюты: USD, EUR, RUB, GBP, JPY, AUD.

## Установка и запуск

### Предварительные требования

Убедитесь, что у вас установлены следующие инструменты:

- Python 3.10
- Docker

### Клонирование репозитория

Склонируйте репозиторий:
```bash
git clone https://github.com/ebarykin/currency_converter_API.git
cd currency_converter_API
```

Создайте файл .env в корне проекта и добавьте в него ваш секретный ключ Django:
```plaintext
DJANGO_SECRET_KEY=ваш_секретный_ключ
```

Создайте Docker-образ и запустите контейнер:
```plaintext
docker build -t currency_converter .
docker run -d -p 8000:8000 currency_converter

```


## Использование API
Конвертация валют


Примеры запросов:
Конвертация 155,5 USD в EUR
```plaintext
GET http://localhost:8000/api/rates/?from=USD&to=EUR&value=155.5
```


Ответ:
```plaintext
{
    "result": 141.66
}
```



### Документация API доступна по следующим URL:

- Swagger UI
(http://localhost:8000/docs/) 
- Redoc
(http://localhost:8000/redoc/)