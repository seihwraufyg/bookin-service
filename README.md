- Просматривать доступные номера
- Создавать бронирования номеров
- Просматривать список броней
- Отменять бронирования

---

## 🛠 Технологии

- **Язык:** Python 3.11
- **Фреймворк:** Flask 2.2.2
- **WSGI-сервер:** Werkzeug 2.2.2
- **Контейнеризация:** Docker

---

## 🌐 Эндпоинты API

| Метод | Адрес | Назначение |
|-------|-------|------------|
| GET | `/` | Информация о сервисе |
| GET | `/api/hotels` | Список отелей |
| GET | `/api/hotels/<id>` | Информация об отеле по ID |
| GET | `/api/rooms` | Список номеров |
| POST | `/api/bookings` | Создать бронирование |
| GET | `/api/bookings` | Список всех броней |
| DELETE | `/api/bookings/<id>` | Отменить бронирование |

---
## Инструкция по запуску
# Перейти в папку проекта и открыть PowerShell

# 1. Собрать образ
docker build -t booking-service .

# 2. Запустить контейнер
docker run -d -p 8080:5000 --name my-booking-app booking-service

# 3. Проверить статус
docker ps

# 4. Посмотреть логи
docker logs my-booking-app

# 5. Открыть в браузере: http://localhost:8080/api/hotels

# 6. Остановить и удалить (когда закончите)
docker stop my-booking-app
docker rm my-booking-app
