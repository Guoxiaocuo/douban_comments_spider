import jieba
from wordcloud import WordCloud

class comments():
    def jieba_(self):
        content = open('doubanComments_JueJi.csv', 'r', encoding='utf-8').read()
        word_list = jieba.cut(content)
        word = []
        for i in word_list:
            with open('停用词库.txt') as f:
                meaningless_file = f.read().splitlines()
                f.close()
            if i not in meaningless_file:
                word.append(i.replace(' ', ''))
        global word_cloud
        word_cloud = ','.join(word)
        print(word_cloud)

    def word_cloud(self):
        #cloud_mask 用来设置词云图背景图片的
        #cloud_mask = np.array(Image.open('qianxi.jpg'))
        wc = WordCloud(
            background_color='white',
            #mask=cloud_mask,
            max_words=200,
            font_path='./fonts/simhei.ttf',
            min_font_size=5,
            max_font_size=100,
            width=800,
            height=600
        )
        global word_cloud
        x = wc.generate(word_cloud)
        image = x.to_image()
        image.show()
        wc.to_file('pic_douban.png')


# 创建类对象
comments = comments()
# 对豆瓣电影短评进行分词处理
comments.jieba_()
# 生成词云图
comments.word_cloud()