#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Define a MeituanSpider class allows you to fetch meituan
restaurants infos in haikou city.
'''

import csv
import json
import os

import requests
import pymysql

import random
import time

from pymongo import MongoClient
from py2neo import Graph, Node
from settings import headers,savePath,filename,mongoConf,collection,limit,neoConf



class MeituanSpider(object):
    '''
    MeituanSpider class allows you to fetch all data from meituan api website.

    :Usage:

    '''

    baseUrl = ("http://api.meituan.com/group/v4/deal/select/city/94/cate/1?"
                "sort=solds&hasGroup=true&mpt_cate1=1&offset={0}&limit={1}")
    modeList = ['txt','csv','mongodb', 'neo4j']
    fieldKey = ['店铺名称','页面id','类别','品牌名称','品牌id','品牌logo','评分',
                '平均价格','最低价格','所属地区','地区Id','纬度','经度','详细地址',
                '楼层','地铁站id','停车信息','优惠套餐情况','营业时间','联系电话',
                '累计售出份数','餐厅简介','特色菜','是否小吃','有无外卖','上周订单数',
                '历史订单数','wifi','支持预定']


    #美团海口地区美食爬虫
    def __init__(self, saveMode='txt'):
        '''
        The constructor of MeituanSpider classself.

        Creates an instance of MeituanSpider, takes in parameters saveMode and
        uses saveMode to initialize database(mysql or mongodb) or create file(
        txt or csv).

        :Args:
         - saveMode - str. Named keyword argument used to specialize which mode
         to save datas from meituan api. This arguments must be 'txt', 'csv' or
         'db'
        '''

        if saveMode not in self.modeList:
            raise RuntimeError('存储模式指定有误，请输入txt、csv或者mongodb')
        self.saveMode = saveMode

        if self.saveMode == 'mongodb':
            print('>>>> we are in mongodb.')
            self.database = MongoClient(mongoConf['host'],
                                        mongoConf['port'])[mongoConf['database']]
            self.database.authenticate(mongoConf['user'],
                                       mongoConf['password'])
            self.collection = self.database[collection]
        elif self.saveMode == 'neo4j':
            print('>>>> we are in neo4j.')
            self.connector = Graph(**neoConf)
        else:
            print('>>>> we are in files.')
            if not os.path.exists(savePath):
                os.makedirs(savePath)
            filePath = os.path.join(savePath,filename+'.'+self.saveMode)
            if not os.access(filePath, os.F_OK):
                with open(filePath, 'w', encoding='utf-8', newline='') as file:
                    if self.saveMode == 'csv':
                        csvwriter = csv.writer(file)
                        csvwriter.writerow(self.fieldKey)
            self.file = open(filePath, 'a', encoding='utf-8', newline='')
            if self.saveMode == 'csv':
                self.csvwriter = csv.writer(self.file)


    def run(self):
        i = 0
        acquiredCount = 0
        while True:
            url = self.baseUrl.format(str(i*limit), limit)
            itemlist = self.parse(url)
            if not itemlist:
                break
            for item in itemlist:
                self.save_item(item)
            acquiredCount += len(itemlist)
            print('已成功请求%d个商家信息'%((i+1)*limit))
            print('已成功获取%d个商家信息'%(acquiredCount))
            i += 1
            time.sleep(random.randint(2,5))


    def save_item(self,item):
        if self.saveMode == 'txt':
            for key,value in item.items():
                self.file.write(str(key)+':'+str(value) + '\n')
            self.file.write('\n\n-----------------------------\n\n\n')
        elif self.saveMode == 'csv':
            self.csvwriter.writerow(item.values())
        elif self.saveMode == 'mongodb':
            self.collection.insert_one(item)
        else:
            meituanShop = Node('Restaurant', **item)
            print(dict(meituanShop))
            self.connector.create(meituanShop)


    def parse(self,url):
        response = requests.get(url,headers=random.choice(headers))
        number = 0
        while True:
            try:
                info_dict = json.loads(response.text)
                info_list = info_dict['data']
                if info_list:
                    break
                else:
                    number += 1
                    if number >= 10:
                        return None
                    time.sleep(10)
                    response = requests.get(url, headers=random.choice(headers))
            except:
                number += 1
                if number >= 10:
                    return None
                time.sleep(10)
                response = requests.get(url, headers=random.choice(headers))

        itemlist = []
        for info in info_list:
            # 店铺名称
            name = info['poi']['name']
            # 页面id
            poiid = info['poi']['poiid']
            # 所属地区
            areaName = info['poi']['areaName']
            # 地区id
            areaId = info['poi']['areaId']
            # 详细地址
            addr = info['poi']['addr']
            # 纬度
            lat = info['poi']['lat']
            # 经度
            lng = info['poi']['lng']
            # 楼层
            floor = info['poi']['floor']
            # 地铁站id
            subwayStationId = info['poi']['subwayStationId']
            # 停车信息
            parking = info['poi']['parkingInfo']
            # 餐厅类别
            cateName = info['poi']['cateName']
            # 品牌名称
            brandName = info['poi']['brandName']
            # 品牌id
            brandId = info['poi']['brandId']
            # 品牌logo
            brandLogo = info ['poi']['brandLogo']
            # 优惠套餐情况
            abstracts = ''
            for abstract in info['poi']['payAbstracts']:
                # abstracts.append(abstract['abstract'])
                abstracts = abstracts + abstract['abstract'] + ';'

            # 评分
            avgScore = info['poi']['avgScore']
            # 平均价格
            avgPrice = info['poi']['avgPrice']
            # 最低价格
            lowestPrice = info['poi']['lowestPrice']
            # 营业时间
            openInfo = info['poi']['openInfo'].replace('\n',' ')
            # 联系电话
            phone = info['poi']['phone']
            # 累计售出份数
            historyCouponCount = info['poi']['historyCouponCount']
            # 餐厅简介
            introduction = info['poi']['introduction']
            # 特色菜
            featureMenus = info['poi']['featureMenus']
            # 是否小吃
            isSnack = info['poi']['isSnack']
            # 有无外卖
            isWaimai = info['poi']['isWaimai']
            # 上周订单数
            latestWeekCoupon = info['poi']['latestWeekCoupon']
            # 历史订单数
            historyCouponCount = info['poi']['historyCouponCount']
            # wifi
            wifi = info['poi']['wifi']
            # 支持预定
            isSupportAppointment = info['poi']['isSupportAppointment']

            item = {
                '店铺名称': name,
                '页面id':poiid,
                '类别': cateName,
                '品牌名称': brandName,
                '品牌id': brandId,
                '品牌logo': brandLogo,
                '评分': avgScore,
                '平均价格': avgPrice,
                '最低价格':lowestPrice,
                '所属地区': areaName,
                '地区Id': areaId,
                '纬度': lat,
                '经度': lng,
                '详细地址': addr,
                '楼层':floor,
                '地铁站id': subwayStationId,
                '停车信息': parking,
                '优惠套餐情况': abstracts,
                '营业时间': openInfo,
                '联系电话': phone,
                '累计售出份数': historyCouponCount,
                '餐厅简介': introduction,
                '特色菜': featureMenus,
                '是否小吃': isSnack,
                '有无外卖': isWaimai,
                '上周订单数': latestWeekCoupon,
                '历史订单数': historyCouponCount,
                'wifi': wifi,
                '支持预定': isSupportAppointment
            }

            itemlist.append(item)
        # 返回当前页面item列表
        return itemlist


    def __del__(self):
        '''
        The deconstructor of MeituanSpider class.

        Deconstructs an instance of MeituanSpider, closes MongoDB database and
        files.
        '''

        if self.saveMode == 'mongodb':
            print('>>>> closing mongodb.')
            # self.database.close()
        elif self.saveMode == 'neo4j':
            print('>>>> closing neo4j')

        else:
            print('>>>> closing file.')
            self.file.close()



# test:
if __name__ == '__main__':
    spider = MeituanSpider(saveMode='csv')
    spider.run()
