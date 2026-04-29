# LoopInf
LoopInf - видеоредактор, который преобразует обычное видео в бесшовное. Можно использовать для создания обоев на рабочем столе, например для Wallpaper Engine.

## Примеры работ
https://github.com/user-attachments/assets/bc7ad4f6-9e27-4d5f-b124-22212bd2d4fe

https://github.com/user-attachments/assets/07f7f609-afea-4b44-8d1c-dc94e21b95b9

Steam: https://steamcommunity.com/sharedfiles/filedetails/?id=3712129838


## Как запустить?

1. Запускаете ./output/main/main.exe или воспользуйтесь установкой для Linux или Windows

2. (Не обязательно) Откройте настройки, если хотите изменить следующие параметры:
    * ***Интервал*** (в кадрах) - минимальное требуемое кол-во повторяющихся кадров
    * ***Точность*** - допустимое отличие кадров друг от друга (1 - самая высокая точность)
    * ***Шаг*** (в кадрах) - на сколько кадров программа будет проходить по всему видео

3. Откройте нужное видео

4. Запустите поиск циклов

5. Скачивайте видео - готово.

## Установка (Linux)
У вас должны быть установлены [зависимости проекта](https://github.com/Dolens-Mortem/LoopInf#зависимости)

1. Клонирование репозитория 

```git clone https://github.com/Dolens-Mortem/LoopInf.git```

2. Создание виртуального окружения

```python3 -m venv venv```

3. Активация виртуального окружения

```source venv/bin/activate```

4. Установка зависимостей

```pip3 install -r requirements.txt```

5. Запуск скрипта

```python3 main.py```


## Установка (Windows)
У вас должны быть установлены [зависимости проекта](https://github.com/Dolens-Mortem/LoopInf#зависимости)

1. Клонирование репозитория 

```git clone https://github.com/Dolens-Mortem/LoopInf.git```

2. Создание виртуального окружения

```python3 -m venv venv```

3. Активация виртуального окружения

```venv/Scripts/activate```

4. Установка зависимостей

```pip3 install -r requirements.txt```

5. Запуск скрипта

```python3 main.py```
