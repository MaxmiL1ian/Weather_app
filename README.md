# Weather_app
Это простое приложение погоды, созданное с использованием Python и Django. Оно позволяет пользователям получать текущую погоду в разных городах с помощью открытого API OpenWeatherMap.

![app](https://github.com/MaxmiL1ian/Weather_app/blob/master/app.png)  

## Установка

1. Клонируйте репозиторий:

```
клон мерзавца https://github.com/yourusername/weather-app.git
```

2. Установите необходимые пакеты:

```
установка pip -r requirements.txt
```

3. Создайте файл `.env` в корневом каталоге и добавьте свой API-ключ:

```python
API_KEY=ваш_api_key
```

4. Запустите сервер:

```
python manage.py сервер запуска
```

5. Откройте приложение в своем браузере по ссылке "http://localhost:8000`

## Использование

1. Введите название города в строку поиска.
2. Нажмите на кнопку "Получить прогноз погоды", чтобы получить текущую информацию о погоде.
3. Приложение отобразит температуру, влажность и описание погоды для указанного города.

## Используемый API

Это приложение использует API OpenWeatherMap для получения данных о погоде. Вы можете получить бесплатный ключ API [здесь](https://openweathermap.org/api).
