import os
import random
import json
import logging

logging.basicConfig(level=logging.DEBUG)

# Текущую директория
# root_dir = os.getcwd()
root_dir = '/home/anowd/FoodBot' # for Pi

# Функция получения рецепта по букве папки
def get_recipe(folder_name):

    # Полный путь к указанной папке
    folder_path = os.path.join(root_dir, folder_name)

    # Проверяем, существует ли папка
    if not os.path.exists(folder_path):
        print("Нет такой папки")
    
    else:
        # Получаем список всех файлов JSON в папке
        json_files = [file for file in os.listdir(folder_path) if file.endswith('.json')]

        if not json_files:
            print("В папке нет JSON файлов.")
        
        else:
            # Выбираем случайный JSON файл
            random_file = random.choice(json_files)
            random_file_path = os.path.join(folder_path, random_file)

            # Открываем и загружаем JSON файл
            with open(random_file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

                # Пытаемся получить нужные ключи из JSON
                title = data.get('title', 'Нет ключа title')
                ingredients = data.get('ingredients', 'Нет ключа ingredients')
                directions = data.get('directions', 'Нет ключа directions')

                # Возвращаем значения ключей
                resultMap = {
                    "Titel": f"{title}",
                    "Ingredients": f"{ingredients}",
                    "Directions": f"{directions}"
                }

                return resultMap

#Get a recipe titel
def get_recipe_titel(letterChar):
    titel = get_recipe(letterChar)["Titel"]
    return titel
###################
