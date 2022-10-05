import os
import urllib.request
import urllib.parse

test_word = '林檎'
url = f'http://dict.youdao.com/dictvoice?le=jap&type=3&audio={urllib.parse.quote(test_word)}'
#url = r'http://dict.youdao.com/dictvoice?le=jap&type=3&audio=%E3%81%BE%E3%81%82%E3%81%BE%E3%81%82'
print(url)
urllib.request.urlretrieve(url, filename='test.mp3')
