from flask import render_template
from app import app
import app.page_loader as page_loader


@app.route('/')
def index():
    return page_loader.render_guide(page_loader.DEFAULT_LANGUAGE, 'home')

@app.route('/<page_name>')
def page(page_name):
    return page_loader.render_guide(page_loader.DEFAULT_LANGUAGE, page_name)

@app.route('/<lang>/<page_name>')
def lang_page(lang, page_name):
    return page_loader.render_guide(lang, page_name)