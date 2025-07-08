import os

TYPE_GUIDE='guide'
TYPE_SETS='sets'
LANG_FOLDER='lang'

BASE_PATH=os.path.join(os.getcwd(), 'app', 'templates')
BASE_DATA_PATH=os.path.join(os.getcwd(), 'app', 'data')

def lang_folder_exists(lang):
    lang_path = os.path.join(BASE_PATH, LANG_FOLDER, lang)
    return os.path.isdir(lang_path)


def template_file_exists(filepath):
    complete_filepath = os.path.join(BASE_PATH, filepath)
    return os.path.isfile(complete_filepath)


def list_files(lang, type):
    if type == TYPE_GUIDE:
        folder_path = os.path.join(BASE_PATH, LANG_FOLDER, lang, type)
        return list_folder_files(folder_path)
    elif type == TYPE_SETS:
        folder_path = os.path.join(BASE_DATA_PATH, type)
        return list_folder_files(folder_path)


def list_folder_files(folder_path):
    from pathlib import Path
    result = list()
    files = os.listdir(folder_path)
    for file in files:
        filepath = Path(file)
        filename = filepath.stem
        if not os.path.isdir(filepath):
            result.append(filename)
    return result



def list_faq_files():
    from pathlib import Path
    result = list()
    folder_path = os.path.join(BASE_DATA_PATH, 'faq')
    files = os.listdir(folder_path)
    for file in files:
        filepath = os.path.join(folder_path, file)
        result.append(filepath)
    return result