from PIL import Image, UnidentifiedImageError
import os
import shutil
import random


def convert_images_to_grayscale_and_remove_invalid(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for file_name in os.listdir(source_folder):
        if file_name.endswith('.jpg'):
            file_path = os.path.join(source_folder, file_name)
            try:
                with Image.open(file_path) as img:
                    grayscale_img = img.convert('L')
                    grayscale_img.save(os.path.join(destination_folder, file_name))
            except UnidentifiedImageError:
                # Usuń plik, który nie może być zidentyfikowany jako obraz
                os.remove(file_path)
                print(f"Usunięto nieprawidłowy plik obrazu: {file_path}")


def copy_files_and_change_name(new_data_folder):
    files = os.listdir(new_data_folder)
    random.shuffle(files)

    for i, file in enumerate(files):
        file_path = os.path.join(new_data_folder, file)
        new_file_path = f'./data3/{i:05d}.jpg'
        shutil.copy(file_path, new_file_path)


def change_names_in_folder(folder_path):
    files = os.listdir(folder_path)

    for i, file in enumerate(files):
        old_path = os.path.join(folder_path, file)
        new_path = os.path.join(folder_path, f'{i:05d}.jpg')
        os.rename(old_path, new_path)


source_folder = './data5/color'  # Zastąp ścieżką do folderu color
destination_folder = './data5/gray'  # Zastąp ścieżką do folderu gray
new_data_folder = './dataset'

# change_names_in_folder(source_folder)
convert_images_to_grayscale_and_remove_invalid(source_folder, destination_folder)
# copy_files_and_change_name(new_data_folder)
