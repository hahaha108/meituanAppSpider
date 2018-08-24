# meituanAppSpider
美团APP爬虫，可获取指定城市范围内所有美食店铺信息，包含店铺名称、类别、评分、所属片区、经纬度、详细地址、优惠套餐情况、营业时间、联系电话、累计售出份数、餐厅简介、特色菜......
<br>
可指定存储方式，有txt，csv，mysql数据库三种方式可供选择

## 一、使用方法
可参照run.py<br>
1.创建一个MT_spider，可指定存储模式，默认为txt
```python
spider = MT_spider(save_mode='csv')
```
2.调用run方法
```python
spider.run()
```

## 二、注意事项
1.默认设置有随机2~5秒爬取间隔，建议不要修改<br>
2.若有需要文件存储名称、路径以及数据库设置项可在settings.py中修改<br>
3.默认爬取城市为深圳，由于美团APP的api中城市信息根据id传输，若要修改城市，只需修改spider.py下base_url中city/后面的数字即可
```python
http://api.meituan.com/group/v4/deal/select/city/30/cate/1?sort=solds&hasGroup=true&mpt_cate1=1&offset={0}&limit=100
```
1为北京，10为上海，20为广州，30为深圳，253为襄阳，其他的可抓包获取

## 三、结果
美团美食商家：深圳23540家；北京24964家；上海28380家；广州21709家；而襄阳只有2851家....
![](https://i.imgur.com/LoLI43n.jpg)
<br>
各地的美食偏好情况分析：<br>
1.深圳：最爱牛肉、牛肉丸、三文鱼、豆腐、水果
![](https://i.imgur.com/0IVWR6E.jpg)
<br>
2.北京：最爱牛肉、五花肉、三文鱼、酸梅汤、羊蝎子、宫保鸡丁
![](https://i.imgur.com/KLaLet1.jpg)
<br>
3.上海：最爱三文鱼、牛肉、酸菜鱼、红烧肉、提拉米苏
![](https://i.imgur.com/JxJV0Df.jpg)
<br>
4.襄阳：表示四线小城市没吃过三文鱼这种高端产品，不过牛肉还是不错的，还有火锅、干锅什么的也很nice
![](https://i.imgur.com/jyRQPWb.jpg)

本程序仅供编程学习之用，请勿用于商业
