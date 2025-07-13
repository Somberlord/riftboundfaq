from flask import Flask

app = Flask(__name__)

from app import routes
from app.utils import faq, card_db

faq.init()
card_db.init()



