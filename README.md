# Yandex Music Analytics

Пет-проект для анализа лайков в Yandex Music.

## Задачи

- [ ] Посчитать топ исполнителей, жанров, треков
- [ ] Визуализировать распределение по часам суток / дням недели
- [ ] Попробовать классифицировать треки по настроению (через API или BPM / energy)

## Интерес

Узнаешь о себе неожиданные паттерны.

## Расширение

Предсказать, какой жанр ты включишь завтра утром.

## Требования

- Python 3.7+

## Установка

1. Клонируйте репозиторий:
```bash
git clone <repository-url>
cd YM_anal
```

2. Создайте виртуальное окружение (рекомендуется):
```bash
python -m venv venv
source venv/bin/activate  # для macOS/Linux
# или
venv\Scripts\activate  # для Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Настройка

1. Скопируйте `.env.example` в `.env`:
```bash
cp .env.example .env
```

2. Откройте `.env` и укажите ваш токен Yandex Music:
```
YANDEX_MUSIC_TOKEN=your_token_here
```

Для получения токена см. [официальный гайд](https://yandex-music.readthedocs.io/en/main/token.html).

## Запуск

```bash
python main.py
```

