# Weather_app
Это простое приложение, созданное с использованием Python и Django. Оно позволяет пользователям получать текущую погоду в разных городах с помощью API OpenWeatherMap.

![app](https://github.com/MaxmiL1ian/Weather_app/blob/master/app.png)  

## Установка

1. Клонируйте репозиторий:

```
git clone https://github.com/MaxmiL1ian/Weather_app.git
```

2. Установите необходимые пакеты:

```
pip install -r requirements.txt
```

3. Создайте файл `.env` в корневом каталоге и добавьте свой API-ключ:

```python
API_KEY = ваш_api_key
API_URL = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&lang=ru&appid={}"
```

4. Запустите сервер:

```
python manage.py runserver
```

5. Откройте приложение в своем браузере по ссылке: http://127.0.0.1:8000/

## Использование

1. Введите название города в строку поиска.
2. Нажмите на кнопку "Получить погоду", чтобы получить текущую информацию о погоде.
3. Приложение отобразит температуру и скорость ветра для указанного города.

## Используемый API

Это приложение использует API OpenWeatherMap для получения данных о погоде. Вы можете получить бесплатный ключ API [здесь](https://openweathermap.org/api).
