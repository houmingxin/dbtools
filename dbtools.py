import pymysql

def query(sql):
    """
        方法：python连接查询数据库
        参数：
            sql： "select * from t_user where id = 255"
        返回值：
            ((1, username, passsword, ..), (2, username2, passsword2, ..),)
    """
    # 步骤1. 连接并且打开对应的数据库
    db = pymysql.connect(host="118.24.105.78",user="root", password="1qaz!QAZ123***123", db="ljtestdb")
    # 步骤2：获取查询窗口：游标
    cur = db.cursor()
    # 步骤3：执行sql语句
    cur.execute(sql)
    # 步骤4：获取对应的结果
    res = cur.fetchall()
    # 步骤5：关闭数据
    db.close()
    
    return res


def commit(sql):
    """
        方法：python连接增删改数据库
        参数：
            sql： 
        返回值：
            ((1, username, passsword, ..), (2, username2, passsword2, ..),)
    """
    # 步骤1. 连接并且打开对应的数据库
    db = pymysql.connect(host="118.24.105.78",user="root", password="1qaz!QAZ123***123", db="ljtestdb")
    # 步骤2：获取查询窗口：游标
    cur = db.cursor()
    # 步骤3：执行sql语句
    cur.execute(sql)
    # 步骤4：获取对应的结果
    db.commit()
    # 步骤5：关闭数据
    db.close()
    