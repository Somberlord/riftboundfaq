import os

TYPE_GUIDE='guide'
LANG_FOLDER='lang'

BASE_PATH=os.path.join(os.getcwd(), 'app', 'templates')

def lang_folder_exists(lang):
    lang_path = os.path.join(BASE_PATH, LANG_FOLDER, lang)
    print(lang_path)
    return os.path.isdir(lang_path)

def template_file_exists(filepath):
    complete_filepath = os.path.join(BASE_PATH, filepath)
    return os.path.isfile(complete_filepath)

def list_files(lang, type):
    folder_path = os.path.join(BASE_PATH, LANG_FOLDER, lang, type)
    from pathlib import Path
    result = list()
    files = os.listdir(folder_path)
    for file in files:
        filepath = Path(file)
        filename = filepath.stem
        if filename == 'home':
            result.insert(0, filename)
        elif filename != 'base' and not os.path.isdir(filepath):
            result.append(filename)
    return result