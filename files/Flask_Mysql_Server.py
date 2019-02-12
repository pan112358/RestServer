#!flask/bin/python

from flask import Flask, abort, make_response, request

import pymysql, sys

app = Flask(__name__)


@app.route('/api/targets/<id>/<key>', methods=['GET'])
def get_response(id,key):
    db = pymysql.connect(host=sys.argv[1], user=sys.argv[2], password=sys.argv[3], port=int(sys.argv[4]),
                         database=sys.argv[5])
    cursor = db.cursor()
    # 按顺序传入7个参数，mysql地址，用户名，密码，端口号， 数据库名，表名，表关键字(不包含id)
    try:
        # 执行sql语句
        cursor.execute("SELECT {0} FROM {1} WHERE ID={2}".format(key, sys.argv[6], id))
        result = cursor.fetchall()
        if result[0][0]==None:
            return 'None'
        else:
            return result[0][0]

    except:
        return 'error'
    # 关闭数据库连接
    db.close()
    return result


@app.route('/api/targets/<id>', methods=['POST','PUT'])
def post_result(id):
    db = pymysql.connect(host=sys.argv[1], user=sys.argv[2], password=sys.argv[3], port=int(sys.argv[4]),
                         database=sys.argv[5])
    cursor = db.cursor()
    keys = ''
    values = ''
    for key in sys.argv[7].split(' '):
        value=request.form.get(key)
        if value==None:
            continue
        else:
            keys += key + ','
            values += value + ','
    keys=keys+'id'
    values=values+id
    sql = "REPLACE INTO {0} ({1}) VALUES ({2}) ".format(sys.argv[6],keys,values)
    cursor.execute(sql)
    db.commit()
    return 'success'
    db.close()


@app.route('/api/targets/<id>', methods=['DELETE'])
def delete(id):
    db = pymysql.connect(host=sys.argv[1], user=sys.argv[2], password=sys.argv[3], port=int(sys.argv[4]),
                         database=sys.argv[5])
    cursor = db.cursor()
    sql = "DELETE FROM {0} WHERE ID={1}".format(sys.argv[6],id)
    cursor.execute(sql)
    db.commit()
    return 'success'
    db.close()


if __name__ == '__main__':

    app.run(debug=True)

