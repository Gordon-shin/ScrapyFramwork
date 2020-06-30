import json
import os
import urllib.request
import time
from http.client import HTTPMessage
from tqdm import tqdm

import requests

with open('doutula.json', encoding='utf-8')as f:
    while True:
        line = f.readline()
        if not line:
            print('结束')
            break
        js = json.loads(line)
        urls = js['pic_urls']
        article = js['article']
        date = js['date']
        i = 0
        for url in urls:
            filetype = str(url).split('.')[-1]
            if filetype:
                filename = (str(article) + '_' + str(date) + '_' + str(i) + '.' + str(filetype)).replace("?","_")
                filepath = 'doutulafiles/' + filename
                print(filename)
                if not os.path.exists(filepath):
                    try:
                      response = requests.get(url, stream=True,timeout=5)
                    except Exception as e:
                        print(e)
                    print(response.status_code)
                    print(len(response.content))
                    if response.status_code == 200:
                        with open(filepath,"wb") as img:
                            img.write(response.content)
                        #result = urllib.request.urlretrieve(url, 'doutulafiles/' + filename)[-1]
                        #assert isinstance(result,HTTPMessage)
                        #print(result.get)
                        i += 1;
                    else:
                        print('请求失败'+str(response.status_code))
        #time.sleep(1)