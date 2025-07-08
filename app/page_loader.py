from flask import render_template, abort
from app.faq import FAQ
import app.file_utils as file_utils
import json

DEFAULT_LANGUAGE='en'

NAVDATA_PAGE_NAME = 'page_name'

def render_guide(page_name, lang=DEFAULT_LANGUAGE):
    if not file_utils.lang_folder_exists(lang):
        lang=DEFAULT_LANGUAGE
    file_path = f'lang/{lang}/guide/{ page_name }.html'
    if not file_utils.template_file_exists(file_path):
        abort(404, description=f"File {page_name} not found on server")
    else:
        nav_data = get_pages(lang)
        nav_data[NAVDATA_PAGE_NAME] = page_name
        nav_data['folder'] = file_utils.TYPE_GUIDE
        title = page_name.replace('_',' ').title()
        return render_template(file_path, title=title, navlist=nav_data)
    
def get_pages(lang):
    nav_data = dict()
    nav_data[file_utils.TYPE_GUIDE] = file_utils.list_files(lang, file_utils.TYPE_GUIDE)
    nav_data[file_utils.TYPE_SETS] = file_utils.list_files(lang, file_utils.TYPE_SETS)
    return nav_data

def render_static_page(page_name, lang=DEFAULT_LANGUAGE, title=None, fullpath=None):
    nav_data = get_pages(lang)
    nav_data[NAVDATA_PAGE_NAME] = page_name
    if fullpath is None:
        fullpath = f'lang/{lang}/{page_name}.html'
    if title is None:
        title = page_name.replace('_',' ').title()
    return render_template(fullpath, title=title, navlist=nav_data)


def render_set(rbset, lang=DEFAULT_LANGUAGE):
    if not file_utils.lang_folder_exists(lang):
        lang=DEFAULT_LANGUAGE
    file_path = f'lang/{lang}/set.html'
    if not file_utils.template_file_exists(file_path):
        abort(404, description=f"File {rbset} not found on server")
    else:
        f = open(f'app/data/sets/{rbset}.json')
        rbset_data = json.load(f)
        nav_data = get_pages(lang)
        nav_data['folder'] = file_utils.TYPE_SETS
        nav_data[NAVDATA_PAGE_NAME] = rbset
        faq = FAQ.get_instance()
        return render_template(file_path, title=f'Set {rbset}', rbset=rbset_data, faq=faq.faq, navlist=nav_data)