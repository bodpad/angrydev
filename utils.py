from tinydb import TinyDB


def load_dictioanry_from_text_file(file_path):
    """
    Функция загружает словарь в бд из файла
    """
    db = TinyDB('db.json')
    with open(file_path) as data_file:
        db.purge()
        for line in data_file:
            word, occurrences = line.split()
            db.insert({'word': word, 'occurrences': int(occurrences)})