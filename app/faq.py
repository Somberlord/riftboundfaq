import yaml
import app.file_utils as file_utils

FAQ_COMMON_ROOT = "faq_list"
FAQ_CARD_LIST = "cards"

def init():
    faq = FAQ.get_instance()
    filelist = file_utils.list_faq_files()
    for filepath in filelist:
        faq.load_file(filepath)


class FAQ():
    faq = dict()
    instance = None

    @staticmethod
    def get_instance():
        if FAQ.instance is None:
            FAQ.instance = FAQ()
        return FAQ.instance
    
    def load_file(self, file_path):
        with open(file_path, 'r') as file:
            file_data: dict = yaml.safe_load(file)
        if not FAQ_COMMON_ROOT in file_data:
            print(f'ERROR No {FAQ_COMMON_ROOT} in {file_path}')
            return
        for faq_entry in file_data[FAQ_COMMON_ROOT]:
            for card in faq_entry[FAQ_CARD_LIST]:
                if not card in self.faq:
                    self.faq[card] = list()
                self.faq[card].append(faq_entry)