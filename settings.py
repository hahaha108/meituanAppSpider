
# 请求头信息
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

# 用于设置csv、txt文件的存储路径和文件名
save_path = './美团商家信息'
filename = '深圳商家'


# 设置表名，数据库信息
table_name = 'SZ_meituan'
db_conf = {
      'host': '127.0.0.1',
      'port': 3306,
      'user': 'root',
      'passwd': '123456',
      'db': 'mtdb',
      'charset': 'utf8',
   }
