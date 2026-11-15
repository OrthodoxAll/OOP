# OOP

Проект с классами `Product` и `Category`, а также загрузкой данных из JSON.

## Структура проекта

```
src/
├── category.py   # класс Category
├── product.py    # класс Product
└── utils.py      # чтение JSON и создание объектов
tests/
├── conftest.py       # общие фикстуры
├── test_category.py  # тесты Category
├── test_product.py   # тесты Product
└── test_utils.py     # тесты работы с JSON
data/
└── products.json     # данные о товарах
```

## Установка

```bash
poetry install --with dev,lint
```

## Запуск тестов

Запуск всех тестов с отчётом о покрытии:

```bash
poetry run pytest
```

Конфигурация `pytest`/`coverage` находится в `pyproject.toml`:
тесты запускаются с `--cov=src`, а сборка падает, если покрытие ниже 75%.

## Отчёт о покрытии

После запуска тестов отчёт доступен в двух видах:

- в консоли — таблица с покрытием по файлам (`--cov-report=term-missing`);
- в браузере — `htmlcov/index.html` (подробный HTML-отчёт).

## Что проверяют тесты

- корректность инициализации объектов `Product` (все атрибуты, типы, разные наборы данных);
- корректность инициализации объектов `Category` (в том числе пустой список товаров);
- подсчёт количества продуктов (`Category.product_count`);
- подсчёт количества категорий (`Category.category_count`);
- создание категорий и товаров из JSON-файла.
