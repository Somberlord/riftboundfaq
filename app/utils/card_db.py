import json
import app.utils.file_utils as file_utils


CARD_DB_COMMON_ROOT = "items"

def init():
    card_db = CardDB.get_instance()
    filelist = file_utils.list_sets_files()
    if filelist is None:
        raise NotImplementedError
    for filepath in filelist:
        card_db.load_file(filepath)


class CardDB():
    card_db = dict()
    instance = None

    @staticmethod
    def get_instance():
        if CardDB.instance is None:
            CardDB.instance = CardDB()
        return CardDB.instance
    
    def load_file(self, file_path):
        with open(file_path, 'r') as file:
            file_data: dict = json.load(file)
        if not CARD_DB_COMMON_ROOT in file_data:
            print(f'ERROR No {CARD_DB_COMMON_ROOT} in {file_path}')
            return
        for card_entry in file_data[CARD_DB_COMMON_ROOT]:
            if 'id' in card_entry:
                self.card_db[card_entry['id']] = card_entry