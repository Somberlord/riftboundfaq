from flask import render_template, abort
import app.file_utils as file_utils

DEFAULT_LANGUAGE='en'

def render_guide(lang, page_name):
    if not file_utils.lang_folder_exists(lang):
        lang=DEFAULT_LANGUAGE
    file_path = f'lang/{lang}/guide/{ page_name }.html'
    if not file_utils.template_file_exists(file_path):
        abort(404, description=f"File {page_name} not found on server")
    else:
        return render_template(file_path, title=page_name, navlist=get_pages(lang))
    
def get_pages(lang):
    return file_utils.list_files(lang, file_utils.TYPE_GUIDE)
    