# -*- coding: utf-8 -*-

'''
meituan api spider's global variables settings.
'''


# HTTP Request headers infos setting variables:
headers = [
    {
        'User-Agent': 'AiMeiTuan /Xiaomi-4.4.2-MI 6 -720x1280-240-5.5.4-254-863254010002128-qqcpd',
        'Host': 'api.meituan.com',
        'Connection': 'Keep-Alive'
    },
    {
        'User-Agent': 'AiMeiTuan /HUAWEI-4.4.2-HUAWEI MLA-AL10-720x1280-240-5.5.4-254-863254010002128-qqcpd',
        'Host': 'api.meituan.com',
        'Connection': 'Keep-Alive'
    }
]

# limit setting variable used to limit numbers of restaurants in one request:
limit = 25

# Data storage path and filename(.csv or .txt file) setting variables:
savePath = './meituanRestaurantsInfos'
filename = 'HaikouRestaurants'

# MySQL table name and MySQL Database setting variables:
tableName = 'HaikouMeituan'
sqlConf = {
      'host': '127.0.0.1',
      'port': 3306,
      'user': 'root',
      'passwd': '123456',
      'db': 'mtdb',
      'charset': 'utf8',
   }

# MongoDB collection name and MongoDB Database setting variables:
collection = 'HaikouMeituanCleaned'
mongoConf = {
    'host': 'localhost', 'port': 27017, 'database': 'test',
    'user': 'test', 'password': 'Crz437991'
}

# Neo4j graph database setting variables:
neoConf = {"host": "localhost", "port": 7687, "password": "Crz437991"}
