# NeoMarket B2C — Cart & Favorites Service

Сервис витрины покупателя (B2C) для NeoMarket.

Реализует домен:
- Избранное (favorites)
- Корзина (cart) — в будущем
- Главная страница — в будущем

Текущий фокус: **блок избранного (favorites)**.

---

## 📌 О проекте

NeoMarket — маркетплейс с архитектурой микросервисов:

- **B2B** — кабинет продавца (товары, SKU)
- **Moderation** — проверка товаров
- **B2C** — витрина покупателя (наш сервис)

Наш сервис:
- хранит избранное пользователя
- запрашивает данные о товарах из B2B
- формирует API для фронтенда

---

## 🚀 Текущий статус

Реализовано:

- [x] Django + DRF каркас сервиса
- [x] Endpoint `GET /api/v1/favorites`
- [x] Базовая структура проекта
- [x] Модель `FavoriteItem`

В работе:

- [ ] Логика получения избранного из БД
- [ ] Batch-запрос в B2B
- [ ] POST /favorites/{product_id}
- [ ] DELETE /favorites/{product_id}
- [ ] Обработка ошибок (400/401/503)

---

## 🧱 Стек

- Python 3.12
- Django
- Django REST Framework (DRF)
- PostgreSQL (по спецификации)
- SQLite (временно для разработки)
- Docker (для финального запуска)

---

## 📁 Структура проекта

```text
neomarket-b2c-cart/
├── src/
│ ├── config/ # настройки Django
│ ├── favorites/ # приложение избранного
│ └── manage.py
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
└── README.md

```
---

## ⚙️ Запуск проекта (локально)

### 1. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 2. Применение миграций
```bash
cd src
python manage.py migrate
```

### 3. Запуск сервера
```bash
python manage.py runserver
```

### 4. Проверка

Открыть в браузере:
```bash
http://127.0.0.1:8000/api/v1/favorites
```

Ожидаемый ответ:
```bash
{
  "items": [],
  "total": 0
}
```

🐳 Запуск через Docker
```bash
docker compose up --build
```

После запуска:
```bash
http://localhost:8000/api/v1/favorites
```

📊 Модель данных
FavoriteItem
user_id: UUID       
product_id: UUID       
added_at: datetime   

- хранит связь пользователь ↔ товар
- уникальность: (user_id, product_id)

📡 API (текущий)
GET /api/v1/favorites

Описание:
Возвращает список избранных товаров пользователя.
Пока: возвращает пустой список (skeleton) будет доработан до соответствия OpenAPI

🧠 Дальнейшие шаги
- Реализовать получение избранного из БД
- Добавить batch-запрос в B2B
- Реализовать CRUD избранного
- Добавить обработку ошибок
- Переключиться на PostgreSQL
- Финализировать Docker

Работа делится по блокам:

- GET /favorites — логика и агрегация
- B2B client — интеграция
- POST /favorites
- DELETE /favorites

📎 Ссылки
- Swagger: https://urfu2026-neomarket.github.io/neomarket-protocols/
- Репозиторий протоколов: neomarket-protocols