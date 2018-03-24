from spider import MT_spider

# save_mode ：txt存储为txt文件，csv存储为csv文件，db存储在mysql数据库中，无输入默认为txt

# spider = MT_spider(save_mode='txt')
spider = MT_spider(save_mode='csv')
# spider = MT_spider(save_mode='db')

spider.run()