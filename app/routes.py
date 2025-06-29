from flask import render_template
from app import app
import app.page_loader as page_loader


@app.route('/')
def index():
    return page_loader.render_guide(page_loader.DEFAULT_LANGUAGE, 'home')

@app.route('/thanks')
def thanks():
    return thanks_lang(page_loader.DEFAULT_LANGUAGE)

@app.route('/<lang>/thanks')
def thanks_lang(lang):
    return render_template(f'lang/{lang}/thanks.html', title='Thanks', navlist=page_loader.get_pages(lang))

@app.route('/contact')
def contact():
    return contact_lang(page_loader.DEFAULT_LANGUAGE)

@app.route('/<lang>/contact')
def contact_lang(lang):
    return render_template(f'lang/{lang}/contact.html', title='Contact', navlist=page_loader.get_pages(lang))

@app.route('/legal')
def legal():
    return legal_lang(page_loader.DEFAULT_LANGUAGE)

@app.route('/<lang>/legal')
def legal_lang(lang):
    return render_template(f'lang/{lang}/legal.html', title='Legal', navlist=page_loader.get_pages(lang))

@app.route('/knownissues')
def known_issues():
    return render_template(f'knis/known_issues.html', title='Know Issues', navlist=page_loader.get_pages(page_loader.DEFAULT_LANGUAGE))

@app.route('/<page_name>')
def page(page_name):
    return page_loader.render_guide(page_loader.DEFAULT_LANGUAGE, page_name)

@app.route('/<lang>/<page_name>')
def lang_page(lang, page_name):
    return page_loader.render_guide(lang, page_name)