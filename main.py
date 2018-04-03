#!/usr/bin/env python3

from langdetect import detect
import jieba
from googletrans import Translator
translator = Translator(service_urls=[
      'translate.google.com',
    ])

text = "EBPP，ODM支持，2015-10-01T12：30：00.000 + 0000，ODM支持，我的账户问题，登录，访问问题/安全性支持"
seg_list = jieba.lcut(text, cut_all=False)

print("\nLanguage is "+detect(text)+"\n")


print("Original: "+text)
print("Cut up:\t" + "/ ".join(seg_list))
translations = translator.translate(seg_list, dest='en')

for translation in translations:
	print(translation.origin, ' -> ', translation.text)
