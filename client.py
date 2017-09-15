import sys
import requests


if __name__ == '__main__':
    host = sys.argv[1]
    port = sys.argv[2]
    uri = 'http://%s:%s/' % (host, port)

    while True:
        term = input()

        if not term:
            continue

        r = requests.get(uri, params={'term': term})
        print(r.text)
