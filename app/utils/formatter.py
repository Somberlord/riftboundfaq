import re
from app.utils.card_db import CardDB

def format_card_image(string: str):
    # Find cards occurence in string
    regex = r'\[([A-Z]{3}-[0-9]{3}a?)]'
    cards = re.findall(regex, string)
    result_str = string
    card_db = CardDB.get_instance().card_db
    for card in cards:
        print(cards)
        if card in card_db:
            result_str = replace_card_with_html(result_str, card_db[card])
    return result_str

def replace_card_with_html(string: str, card_data):
    card_id = card_data['id']
    card_title = card_data['title']
    inner_span = f'<span class="card-image-preview"><img src="https://cdn.piltoverarchive.com/cards/{ card_id }.webp" ' \
    f'alt="{ card_title }" style="max-width:200px; max-height:300px; display:block;" /></span>'
    icon_str = f'<a href="https://cdn.piltoverarchive.com/cards/{ card_id }.webp" target="_blank" class="card-link-with-preview"><img class="might-icon" src="/static/images/zoom.webp" data-light="/static/images/zoom.webp" ' \
    f'data-dark="/static/images/zoom_darkmode.webp" alt="Zoom" style="height:1em; vertical-align:middle;">{inner_span}</a>'
    replace_str = f'<i>{card_title}</i> {icon_str}'
    new_string = string.replace(f'[{card_data['id']}]', replace_str)
    return new_string