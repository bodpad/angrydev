import sys
from flask import Flask, request
from tinydb import TinyDB, Query
from utils import load_dictioanry_from_text_file

app = Flask(__name__)
db = TinyDB('db.json')
q = Query()


@app.route("/", methods=['GET'])
def index():

    term = request.args.get('term', '')  # Часть искомого слова

    # Находим все слова начинающиеся с 'term'
    result = db.search(q.word.matches('^%s' % term))

    if len(result) == 0:
        return 'Not found'

    # Сортируем результат поиска по кол-ву вхождений (по убыванию) и лексикографически
    result = sorted(result, key=lambda x: (-x['occurrences'], x['word']))

    if len(result) > 10:
        # Если существует больше десяти возможных вариантов,
        # то вывести нужно лишь первые десять из них.
        result = result[:10]

    return "\n".join(item['word'] for item in result)


if __name__ == '__main__':

    filepath = sys.argv[1]  # Путь к текстовому файлу, содержащему словарь

    port = sys.argv[2]  # Номер порта

    # Загружаем словарь в бд из файла, содержащий словарь
    load_dictioanry_from_text_file(filepath)

    # Запускаем сервер
    app.run(host='127.0.0.1', port=port)