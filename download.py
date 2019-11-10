import json
import os

import requests


def download(url, file_name):
    with open(file_name, 'wb') as handle:
        response = requests.get(url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)

    print(file_name)


if __name__ == '__main__':
    with open('output.json', encoding='utf-8') as data_file:
        try:
            files = os.listdir('output')
        except FileNotFoundError:
            os.mkdir('output')
            files = os.listdir('output')

        files.sort()
        if len(files) > 0:
            last_file_name = files[-1].split('.')[0]
            last_file_name = int(last_file_name.split('_')[0]) + 1
        else:
            last_file_name = 0

        data = json.load(data_file)
        for i in range(0, len(data)):
            urls = data[i]['img_urls']
            for url in urls:
                if not url:
                    continue
                last_file_name = last_file_name + 1
                try:
                    download(url, "output/" + str('%06d' % (last_file_name + i)) + f"_{data[i]['likes']}.jpg")
                except Exception as e:
                    print(repr(e))
