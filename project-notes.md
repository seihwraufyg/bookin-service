echo "# Project Notes - заметки по проекту бронирования

## Архитектура проекта
- REST API на Flask
- База данных PostgreSQL для хранения:
  - Отели
  - Номера
  - Бронирования
  - Пользователи
- Redis для кеширования доступных номеров
- Docker Compose для запуска всех сервисов

## Модели данных

### Hotel
- id (int)
- name (string)
- address (string)
- city (string)
- rating (float)
- description (text)

### Room
- id (int)
- hotel_id (int)
- number (string)
- type (string: single, double, suite)
- price (float)
- is_available (boolean)

### Booking
- id (int)
- user_id (int)
- room_id (int)
- check_in (date)
- check_out (date)
- status (string: confirmed, cancelled, completed)
- total_price (float)

### User
- id (int)
- name (string)
- email (string)
- phone (string)

## Планируемые эндпоинты
1. GET /api/hotels - поиск отелей
2. GET /api/hotels/{id} - детали отеля
3. GET /api/rooms?hotel_id={id} - номера отеля
4. POST /api/bookings - создать бронирование
5. GET /api/bookings - получить бронирования пользователя
6. DELETE /api/bookings/{id} - отменить бронирование

## Требования
- Python 3.10+
- PostgreSQL 15+
- Redis 7+
- Docker & Docker Compose" > project-notes.md