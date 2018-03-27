import csv
import  matplotlib.pyplot as plt
import jieba
import numpy as np
from PIL import Image
# import wordcloud
from wordcloud import WordCloud, STOPWORDS,ImageColorGenerator

file = open('./美团商家信息/北京商家.csv','r',encoding='utf-8')
rows = csv.reader(file)
text = ''
for row in rows:
    # print(row)
    if row[-1] != '':
        text += row[-1] + '，'
print(text)
text=text.replace("免费","").replace("到家","").replace("送货","").replace("店同城","").replace("生日蛋糕","")
text=text.replace("上门","").replace("预定","").replace("预订","").replace("配送","").replace("英寸","").replace("代金券","")
wordlist=jieba.cut_for_search(text)
space_list=" ".join(wordlist)#链接词语
backgroud=np.array(Image.open("bj.jpg")) #背景图片
mywordcloud=WordCloud(width=1200, height=1200,background_color="#B0E0E6", #背景颜色
                      margin=1,
                      mask=backgroud,#写字用的背景图，从背景图取颜色
                      max_words=200,  #最大词语数量
                      stopwords=STOPWORDS, #停止的默认词语
                      font_path="zy.otf", #字体
                      max_font_size=200, #最大字体尺寸
                      random_state=50,#随机角度
                      scale=2).generate(space_list) #生成词云

image_color=ImageColorGenerator(backgroud) #生成词云的颜色
plt.imshow(mywordcloud) #显示词云
plt.axis("off") #关闭保存
plt.show()

