import sys, pymysql

# 创建数据库

db = pymysql.connect(host=sys.argv[1], user=sys.argv[2], password=sys.argv[3], port=int(sys.argv[4]))

cursor = db.cursor()

# 按顺序传入7个参数，mysql地址，用户名，密码，端口号， 数据库名，表名，表关键字（不包含ID）
keys = ''
for key in sys.argv[7].split(' '):
    if key == sys.argv[7].split(' ')[-1]:
        keys += key + ' VARCHAR(20)'
    else:
        keys += key + ' VARCHAR(20),'

sql = "CREATE TABLE IF NOT EXISTS " + sys.argv[6] + " (ID VARCHAR(20) PRIMARY KEY, " + keys + ")"

try:
    # 执行sql语句
    cursor.execute("CREATE DATABASE IF NOT EXISTS {0}".format(sys.argv[5]))
    cursor.execute("USE {0}".format(sys.argv[5]))
    cursor.execute(sql)
    # 执行sql语句
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# 关闭数据库连接
db.close()
