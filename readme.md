# API DOC
разница между PUT и PATCH: https://ru.stackoverflow.com/questions/1070324/%D0%A0%D0%B0%D0%B7%D0%BD%D0%B8%D1%86%D0%B0-%D0%BE%D1%82%D0%BB%D0%B8%D1%87%D0%B8%D1%8F-%D0%BC%D0%B5%D0%B6%D0%B4%D1%83-put-%D0%B8-patch-%D0%B2-rest
## api/shop-bot-web/list/
### GET
Возвращает список всякого говна что у нас есть на проекте
```json
{
    "Shop": [
        {
            "id": 1,
            "owner": 2,
            "created_at": "2022-03-02T15:25:29Z",
            "is_locked": false,
            "owner_username": "whom",
            "is_owner": true,
            "title": "12312312"
        }
    ],
    "Bot": [
        {
            "shop": 1,
            "language": 1,
            "title": "Новый бот",
            "currency": 1,
            "display_item_out_of_stock": false,
            "display_item_quantity": false,
            "currency_display": "Рубли ₽",
            "language_display": "Русский",
            "id": 1,
            "shop_owner_username": "whom",
            "is_owner": true,
            "is_locked": false,
            "created_at": "2022-05-18T06:16:18.280511Z",
            "active_users": 0
      }
    ]
}
```
## /api/shop/list/
### GET
Возвращает список магазинов в которых он модератор/админ
```json
[
    {
        "id": 2,
        "owner": 2,
        "created_at": "2021-07-09T12:03:56Z",
        "is_locked": true,
        "owner_username": "whom",
        "is_owner": true
    },
    {
        "id": 1,
        "owner": 3,
        "created_at": "2021-07-09T11:34:26Z",
        "is_locked": false,
        "owner_username": "root",
        "is_owner": false
    }
]
```
## /api/shop/create/
### POST
Создает новый магазин <br><br>
Запрос:
```json
{"title": "1231231"}
```



Ответ:
```json
{
    "id": 7,
    "created_at": "2022-01-25T14:03:43.312264Z",
    "is_locked": false,
    "owner_username": "whom",
    "is_owner": true,
    "title": "1231231"
}
```
---
## /api/shop/update/{id}/
### GET
Детальная информация о магазине. 

Если у пользователя недостаточно прав для редактирования:<br>
```json
{
    "detail": "Not found."
}
```
Иначе:
```json
{
    "id": 2,
    "owner": 2,
    "created_at": "2021-07-09T12:03:56Z",
    "is_locked": true,
    "owner_username": "whom",
    "is_owner": true
}
```
### PUT or PATCH
Передача магазина другому пользователю.
```json
{"owner": 1}
```
---
## /api/bot/list/
### GET
Список ботов привязанных к магазину
```json
[
    {
        "shop": 1,
        "language": 1,
        "title": "Новый бот",
        "currency": 1,
        "display_item_out_of_stock": false,
        "display_item_quantity": false,
        "currency_display": "Рубли ₽",
        "language_display": "Русский",
        "id": 1,
        "shop_owner_username": "whom",
        "is_owner": true,
        "is_locked": false,
        "created_at": "2022-05-18T06:16:18.280511Z",
        "active_users": 0
    }
]
```
---
## /api/bot/update/{id}/
### PATCH or PUT
Используется для изменения принадлежности бота к магазину и настроек валюты и языка бота.
```json
{
    "shop": 2,
    "language": 1,
    "title": "Новый бот",
    "currency": 1,
    "display_item_out_of_stock": false,
    "display_item_quantity": false
}
```
---
## /api/bot/create/
### POST
Создание магазина(нужно заполнять поля при создании)
```json
{
    "shop": 2,
    "language": 1,
    "title": "Новый магазин",
    "currency": 2,
    "display_item_out_of_stock": false,
    "display_item_quantity": false
}
```
---
## api/category/list/{shop_id}/
### GET
Extend - продолжает категорию
Extend - null - корневая категория

```json
[
    {
        "id": 3,
        "shop": 2,
        "title": "12321 1232313123",
        "extend": 6,
        "extend_title": "12321312312 whom 12"
    },
    {
        "id": 6,
        "shop": 2,
        "title": "12321312312 whom 12",
        "extend": 3,
        "extend_title": "12321 1232313123"
    },
    {
        "id": 7,
        "shop": 2,
        "title": "12312312",
        "extend": null,
        "extend_title": null
    }
]
```
## api/category/update/{id}/
### PUT or PATCH
```json
{
    "id": 3,
    "shop": 2,
    "title": "12321 1232313123",
    "extend": 6,
    "extend_title": "12321312312 whom 12"
}
```
---
## api/shop/{id}/charts/orders_amount/{delta}/
### GET
delta - может принимать значения: "day" / "month"

Возвращает данные для highchart графика для оборота по заказам
```json
"chart_orders": {
"dates_list":[
"2021-09-04T09:09:09.034Z",
"2021-09-04T10:09:09.034Z",
"2021-09-04T11:09:09.034Z",
"2021-09-04T12:09:09.034Z",
"2021-09-04T13:09:09.034Z",
"2021-09-04T14:09:09.034Z",
"2021-09-04T15:09:09.034Z",
"2021-09-04T16:09:09.034Z",
"2021-09-04T17:09:09.034Z",
"2021-09-04T18:09:09.034Z",
"2021-09-04T19:09:09.034Z",
"2021-09-04T20:09:09.034Z",
"2021-09-04T21:09:09.034Z",
"2021-09-04T22:09:09.034Z",
"2021-09-04T23:09:09.034Z",
"2021-09-05T00:09:09.034Z",
"2021-09-05T01:09:09.034Z",
"2021-09-05T02:09:09.034Z",
"2021-09-05T03:09:09.034Z",
"2021-09-05T04:09:09.034Z",
"2021-09-05T05:09:09.034Z",
"2021-09-05T06:09:09.034Z",
"2021-09-05T07:09:09.034Z",
"2021-09-05T08:09:09.034Z"
],
"series":[
{
"name":"Заказы",
"data":[
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0
]
}
]
}
}
```
---
## api/shop/{id}/charts/orders/{delta}/
### GET
delta - может принимать значения: "day" / "week" / "mouth"

Возвращает данные для highchart графика для числа заказов

```json
{
"chart_orders":{
"dates_list":[
"2021-09-04T09:13:04.319Z",
"2021-09-04T10:13:04.319Z",
"2021-09-04T11:13:04.319Z",
"2021-09-04T12:13:04.319Z",
"2021-09-04T13:13:04.319Z",
"2021-09-04T14:13:04.319Z",
"2021-09-04T15:13:04.319Z",
"2021-09-04T16:13:04.319Z",
"2021-09-04T17:13:04.319Z",
"2021-09-04T18:13:04.319Z",
"2021-09-04T19:13:04.319Z",
"2021-09-04T20:13:04.319Z",
"2021-09-04T21:13:04.319Z",
"2021-09-04T22:13:04.319Z",
"2021-09-04T23:13:04.319Z",
"2021-09-05T00:13:04.319Z",
"2021-09-05T01:13:04.319Z",
"2021-09-05T02:13:04.319Z",
"2021-09-05T03:13:04.319Z",
"2021-09-05T04:13:04.319Z",
"2021-09-05T05:13:04.319Z",
"2021-09-05T06:13:04.319Z",
"2021-09-05T07:13:04.319Z",
"2021-09-05T08:13:04.319Z"
],
"series":[
{
"name":"Заказы",
"data":[
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0
]
}
]
}
}
```
---
## /api/statistics/shop/{id}/
### GET
```json
{"paid_orders": 1, "sold_in_total": 2, "sold_for_a_total_of": "110"}
```

## api/order/last/{shop_id}/
### GET
```json
[
    {
        "id": 1,
        "product_title": "Тестовый товар",
        "user_username": "whom",
        "paid_at": "2021-07-21T16:23:01Z"
    },
    {
        "id": 2,
        "product_title": "Тестовый товар",
        "user_username": "whom",
        "paid_at": "2021-08-03T23:03:09Z"
    }
]
```

## api/order/list/{shop_id}/
### GET
```json
[
    {
        "id": 1,
        "product_title": "Тестовый товар",
        "user_username": "whom",
        "paid_at": "2021-07-21T16:23:01Z"
    },
    {
        "id": 2,
        "product_title": "Тестовый товар",
        "user_username": "whom",
        "paid_at": "2021-08-03T23:03:09Z"
    }
]
```


## api/user/me/
### GET
```json
{
    "username_telegram": "whomLZT",
    "balance": 100.0
}
```

## api/user/list/{bot_id}/
### GET
```json
[
    {
        "user": 2,
        "is_banned": false,
        "chat_id": 0,
        "username": "whomLZT",
        "is_active": true
    },
    {
        "user": 2,
        "is_banned": false,
        "chat_id": 0,
        "username": "whomLZT",
        "is_active": true
    }
]
```

## api/product/list/<int:shop_id>/
### GET
```json
[
    {
        "id": 1,
        "title": "Тестовый товар",
        "shop": 2,
        "type": "Строковый (Цифровой)",
        "category": 6,
        "category_title": "12321312312 whom 12",
        "quantity": 1,
        "strings": "123",
        "price": "0.00",
        "is_hidden": false
    }
]
```

## api/product/update/<int:product_id>/
### GET
```json
{
    "id": 1,
    "title": "Тестовый товар",
    "shop": 2,
    "type": "Строковый (Цифровой)",
    "category": 6,
    "category_title": "12321312312 whom 12",
    "quantity": 1,
    "strings": "123"
}
```

## api/notifications/list/
### GET
SUCCESS = (1, 'Success') <br>
ERROR = (2, 'Error')
```json
[
    {
        "id": 1,
        "title": "123123323",
        "text": "1231231231",
        "type": 1,
        "created_at": "2022-05-18T06:30:31.395661Z"
    }
]
```
