<h1>Тестовое задание</h1>

<h3>Техническое задание:</h3>
Есть JSON массив вида:

```json
[{"Sensor_type": 10, "num": 0, "name": "N/A", "temperature": 20, "humidity": 25 }, 
{"Sensor_type": 4, "num": 1, "name": "N/A"},
{"Sensor_type": 1, "num": 2, "name": "N/A", "temperature": 13},
{"Sensor_type": 2, "num": 3, "name": "N/A", "humidity": 58 },
{"Sensor_type": 10, "num": 4, "name": "N/A", "temperature": 23, "humidity": 59 },
{"Sensor_type": 4, "num": 5, "name": "N/A"},
{"Sensor_type": 1, "num": 6, "name": "N/A", "temperature": 19},
{"Sensor_type": 2, "num": 7, "name": "N/A", "humidity": 35 },
{"Sensor_type": 10, "num": 8, "name": "N/A", "temperature": 22, "humidity": 50 }, 
{"Sensor_type": 4, "num": 9, "name": "N/A"},
{"Sensor_type": 1, "num": 10, "name": "N/A", "temperature": 20},
{"Sensor_type": 2, "num": 11, "name": "N/A", "humidity": 57 },
{"Sensor_type": 10, "num": 12, "name": "N/A", "temperature": 22, "humidity": 55 },
{"Sensor_type": 4, "num": 13, "name": "N/A"},
{"Sensor_type": 1, "num": 14, "name": "N/A", "temperature": 13},
{"Sensor_type": 2, "num": 15, "name": "N/A", "humidity": 45 },
{"Sensor_type": 10, "num": 16, "name": "N/A", "temperature": 21, "humidity": 35 },
{"Sensor_type": 4, "num": 17, "name": "N/A"},
{"Sensor_type": 1, "num": 18, "name": "N/A", "temperature": 20},
{"Sensor_type": 2, "num": 19, "name": "N/A", "humidity": 35 }]

```

Где, Sensor_type – тип датчика <br>
num – порядковый номер <br>
name- имя датчика <br>
temperature - температура, измеряемая датчиком в градусах Цельсия <br>
humidity- влажность, измеряемая датчиком в процентах <br><br>
С помощью средств python, html, JS и различных Задание:
1. Обработать данные из JSON массива
2. Сохранить данные в базу данных
3. Вычитать данные из базы данных и отобразить на странице

## api/add/rf/
###POST
Отправляете json массив выше.

## api/view/rf/
###GET
```json
[
    {
        "sensor_type": 10,
        "num": 0,
        "name": "N/A",
        "temperature": 20,
        "humidity": 25
    },
    {
        "sensor_type": 4,
        "num": 1,
        "name": "N/A",
        "temperature": null,
        "humidity": null
    },
    {
        "sensor_type": 1,
        "num": 2,
        "name": "N/A",
        "temperature": 13,
        "humidity": null
    },
    {
        "sensor_type": 2,
        "num": 3,
        "name": "N/A",
        "temperature": null,
        "humidity": 58
    },
    {
        "sensor_type": 10,
        "num": 4,
        "name": "N/A",
        "temperature": 23,
        "humidity": 59
    },
    {
        "sensor_type": 4,
        "num": 5,
        "name": "N/A",
        "temperature": null,
        "humidity": null
    },
    {
        "sensor_type": 1,
        "num": 6,
        "name": "N/A",
        "temperature": 19,
        "humidity": null
    },
    {
        "sensor_type": 2,
        "num": 7,
        "name": "N/A",
        "temperature": null,
        "humidity": 35
    },
    {
        "sensor_type": 10,
        "num": 8,
        "name": "N/A",
        "temperature": 22,
        "humidity": 50
    },
    {
        "sensor_type": 4,
        "num": 9,
        "name": "N/A",
        "temperature": null,
        "humidity": null
    },
    {
        "sensor_type": 1,
        "num": 10,
        "name": "N/A",
        "temperature": 20,
        "humidity": null
    },
    {
        "sensor_type": 2,
        "num": 11,
        "name": "N/A",
        "temperature": null,
        "humidity": 57
    },
    {
        "sensor_type": 10,
        "num": 12,
        "name": "N/A",
        "temperature": 22,
        "humidity": 55
    },
    {
        "sensor_type": 4,
        "num": 13,
        "name": "N/A",
        "temperature": null,
        "humidity": null
    },
    {
        "sensor_type": 1,
        "num": 14,
        "name": "N/A",
        "temperature": 13,
        "humidity": null
    },
    {
        "sensor_type": 2,
        "num": 15,
        "name": "N/A",
        "temperature": null,
        "humidity": 45
    },
    {
        "sensor_type": 10,
        "num": 16,
        "name": "N/A",
        "temperature": 21,
        "humidity": 35
    },
    {
        "sensor_type": 4,
        "num": 17,
        "name": "N/A",
        "temperature": null,
        "humidity": null
    },
    {
        "sensor_type": 1,
        "num": 18,
        "name": "N/A",
        "temperature": 20,
        "humidity": null
    },
    {
        "sensor_type": 2,
        "num": 19,
        "name": "N/A",
        "temperature": null,
        "humidity": 35
    }
]

```

<h2>api/view/table/</h2>
<h5>GET</h5>
Возвращает таблицу HTML с данными из json массива
