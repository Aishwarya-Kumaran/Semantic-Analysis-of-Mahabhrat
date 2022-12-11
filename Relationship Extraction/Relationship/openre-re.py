from openie import StanfordOpenIE
import pandas as pd
# https://stanfordnlp.github.io/CoreNLP/openie.html#api
# Default value of openie.affinity_probability_cap was 1/3.
properties = {
    'openie.affinity_probability_cap': 2 / 3,
}

import nltk
from nltk.tokenize import sent_tokenize
nltk.download('punkt')

# df1 = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\FYP\\books\\chap-1.csv")
# df2 = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\FYP\\books\\chap-2.csv")
# df3 = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\FYP\\books\\chap-3.csv")
# df4 = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\FYP\\books\\chap-4.csv")
#df5 = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\FYP\\books\\chap-5.csv")
df = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\FYP\\books\\chap-10.csv")
# df7 = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\FYP\\books\\chap-7.csv")
# df8 = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\FYP\\books\\chap-8.csv")
# df9 = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\FYP\\books\\chap-9.csv")
# df10 = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\FYP\\books\\chap-10.csv")
# df11 = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\FYP\\books\\chap-11.csv")
#df = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\FYP\\Events\\Abhimanyu\\abi-sentences.csv")
# df13 = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\FYP\\books\\chap-13.csv")
# df14 = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\FYP\\books\\chap-14.csv")
# df15 = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\FYP\\books\\chap-15.csv")
# df16 = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\FYP\\books\\chap-16.csv")
# df17 = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\FYP\\books\\chap-17.csv")
# df18 = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\FYP\\books\\chap-18.csv")



# book_list = ["06","07","08"]
# # book_list = ["07"]
# sen_list = []
# for i in book_list:
#   book_path = file_path + i + ".txt"
#   #print(book_path)
  
# frame =  [df12, df13, df14, df15, df16, df17, df18]
# df = pd.concat(frame)
#   f = open(book_path, "r")
#   s = f.read()
#   temp = sent_tokenize(s)
#   for x in temp:
#     sen_list.append(x)
# print(sen_list[100])
# sen_list = sen_list[100:150]
subject = []
object = []
relation = []
document = []
k = 0
with StanfordOpenIE(properties=properties) as client:
    for text in df['sentence']: 
        # print('Text: %s.' % text)
        k+=1
        if(k%100 == 0):
            print(k)
        for triple in client.annotate(text):
            subject.append(triple['subject'])
            object.append(triple['object'])
            relation.append(triple['relation'])
            document.append(text)
file = {"document": document, "subject":subject, "relation": relation, "object": object}
df = pd.DataFrame(file) 
    
df.to_csv('chapter_10.csv') 

