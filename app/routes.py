from flask import render_template
from app import app
import app.utils.page_loader as page_loader
import app.utils.formatter as formatter
import re

@app.template_filter('card_id_img')
def card_id_img_filter(text):
    return formatter.format_card_image(text)

@app.template_filter('is_root_card')
def is_root_card(text):
    return re.fullmatch('[A-Z]{3}-[0-9]{3}', text)


@app.route('/')
def index():
    return page_loader.render_static_page('home')

@app.route('/thanks')
def thanks():
    return page_loader.render_static_page('thanks')

@app.route('/<lang>/thanks')
def thanks_lang(lang):
    return page_loader.render_static_page('thanks', lang=lang)

@app.route('/contact')
def contact():
    return page_loader.render_static_page('contact')

@app.route('/<lang>/contact')
def contact_lang(lang):
    return page_loader.render_static_page('contact', lang=lang)

@app.route('/legal')
def legal():
    return page_loader.render_static_page('legal')

@app.route('/<lang>/legal')
def legal_lang(lang):
    return page_loader.render_static_page('legal', lang=lang)

@app.route('/riotrules')
def known_issues():
    return page_loader.render_static_page('riotrules', title='Riot Rules', fullpath='knis/known_issues.html')

@app.route('/docs')
def official_documents():
    return page_loader.render_static_page('docs', title='Official Riot Documents')

@app.route('/sets/<rbset>')
def rbset(rbset):
    return page_loader.render_set(rbset)

@app.route('/<page_name>')
def page(page_name):
    return page_loader.render_guide(page_name)

@app.route('/<lang>/<page_name>')
def lang_page(lang, page_name):
    return page_loader.render_guide(page_name, lang=lang)