import pymysql

# 打开数据库连接
db = pymysql.connect(host="localhost", user="root", password="tjx158589", database="tiaokan2", charset="utf8")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT baidu_url , code from baidu_data")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchall()
from util.BaiduYunTransfer.BaiduYunTransfer import BaiduYunTransfer

for d in data:
    print(d[0],d[1])
    # BaiduYunTransfer.teat(d[0],d[1],'/teat')


# 关闭数据库连接
db.close()