from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', navlist=get_pages())

@app.route('/<page_name>')
def page(page_name):
    return render_template(f'{ page_name }.html', title=page_name, navlist=get_pages())

def get_pages():
    import os
    from pathlib import Path
    result = list()
    current_dir = os.getcwd()
    base_dir = os.path.join(current_dir, 'app', 'templates')
    files = os.listdir(base_dir)
    for file in files:
        filename = Path(file).stem
        if filename != 'base':
            result.append(filename)
    return result
    