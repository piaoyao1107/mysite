import pymysql


def get_List(sql,args):
    """
    获取列表信息，查询操作
    :param sql:
    :param args:
    :return:
    """
    conn = pymysql.connect("localhost", "root", "Passw0rd", "mysite")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql,args)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def get_one(sql,args):
    """
    查询一条数据
    :param sql:
    :param args:
    :return:
    """
    conn = pymysql.connect("localhost", "root", "Passw0rd", "mysite")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result


def modify(sql,args):
    """
    更新、插入、删除等操作
    :param sql:
    :param args:
    :return:
    """
    conn = pymysql.connect("localhost", "root", "Passw0rd", "mysite")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    conn.commit()
    cursor.close()
    conn.close()


