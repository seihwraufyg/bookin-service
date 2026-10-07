echo "# API Plan - детальный план API для сервиса бронирования

## 1. GET /api/hotels
**Описание:** Получить список отелей с фильтрацией
**Параметры запроса:**
- city (string, optional) - фильтр по городу
- min_rating (float, optional) - минимальный рейтинг
- max_price (float, optional) - максимальная цена

**Ответ:** 200 OK
\`\`\`json
{
  \"hotels\": [
    {
      \"id\": 1,
      \"name\": \"Grand Hotel\",
      \"city\": \"Москва\",
      \"rating\": 4.8,
      \"price_from\": 5000,
      \"image\": \"url\"
    }
  ]
}
\`\`\`

## 2. GET /api/hotels/{id}
**Описание:** Получить детальную информацию об отеле
**Ответ:** 200 OK
\`\`\`json
{
  \"id\": 1,
  \"name\": \"Grand Hotel\",
  \"address\": \"ул. Тверская, 1\",
  \"city\": \"Москва\",
  \"rating\": 4.8,
  \"description\": \"Роскошный отель в центре Москвы\",
  \"rooms\": [
    {
      \"id\": 1,
      \"number\": \"101\",
      \"type\": \"suite\",
      \"price\": 15000,
      \"is_available\": true
    }
  ]
}
\`\`\`

## 3. GET /api/rooms
**Описание:** Получить доступные номера
**Параметры запроса:**
- hotel_id (int, required) - ID отеля
- check_in (date, required) - дата заезда
- check_out (date, required) - дата выезда
- guests (int, optional) - количество гостей

**Ответ:** 200 OK
\`\`\`json
{
  \"rooms\": [
    {
      \"id\": 1,
      \"number\": \"101\",
      \"type\": \"suite\",
      \"price\": 15000,
      \"capacity\": 4,
      \"is_available\": true
    }
  ]
}
\`\`\`

## 4. POST /api/bookings
**Описание:** Создать новое бронирование
**Тело запроса:**
\`\`\`json
{
  \"room_id\": 1,
  \"check_in\": \"2026-10-01\",
  \"check_out\": \"2026-10-05\",
  \"guests\": 2,
  \"user_id\": 1
}
\`\`\`
**Ответ:** 201 Created
\`\`\`json
{
  \"id\": 1,
  \"status\": \"confirmed\",
  \"total_price\": 60000,
  \"message\": \"Бронирование подтверждено\"
}
\`\`\`

## 5. GET /api/bookings
**Описание:** Получить все бронирования пользователя
**Параметры запроса:**
- user_id (int, required) - ID пользователя

**Ответ:** 200 OK
\`\`\`json
{
  \"bookings\": [
    {
      \"id\": 1,
      \"hotel_name\": \"Grand Hotel\",
      \"room_number\": \"101\",
      \"check_in\": \"2026-10-01\",
      \"check_out\": \"2026-10-05\",
      \"status\": \"confirmed\",
      \"total_price\": 60000
    }
  ]
}
\`\`\`

## 6. DELETE /api/bookings/{id}
**Описание:** Отменить бронирование
**Ответ:** 204 No Content

## 7. GET /api/search
**Описание:** Поиск отелей по городу и датам
**Параметры запроса:**
- city (string, required)
- check_in (date, required)
- check_out (date, required)
- guests (int, optional)

**Ответ:** 200 OK" > api-plan.md