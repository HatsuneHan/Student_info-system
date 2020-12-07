import pymysql
import math


def add_db_handler(id, name, picpath):
    db = pymysql.connect("localhost", "hatsunehan", "qwer1234", "student")
    cursor = db.cursor()
    sql = "INSERT INTO student_info (id,name,path) VALUES('%s','%s','%s')" % (
        id, name, picpath)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        return 0
    db.close()
    return 1


def del_db_handler(id):
    db = pymysql.connect("localhost", "hatsunehan", "qwer1234", "student")
    cursor = db.cursor()
    sql = "DELETE FROM student_info WHERE id = '%s'" % (id)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        return 0
    db.close()
    return 1


def get_db_handler(pageno):
    nameArray = []
    pathArray = []
    idArray = []
    db = pymysql.connect("localhost", "hatsunehan", "qwer1234", "student")
    cursor = db.cursor()
    sql = "SELECT * FROM student_info"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            idArray.append(row[0])
            nameArray.append(row[1])
            pathArray.append(row[2])
    except:
        print("Error: unable to fetch data")
        return 0
    # print(idArray)
    # print(nameArray)
    # print(pathArray)
    db.close()
    if (pageno * 4 - 3 > len(idArray)):
        return [[], [], []]
    else:
        return [idArray[pageno*4-4:min(pageno*4, len(idArray))], nameArray[pageno*4-4:min(pageno*4, len(idArray))], pathArray[pageno*4-4:min(pageno*4, len(idArray))]]


# print(add_db_handler('18300750006', '韩晓宇', '/home'))
# del_db_handler('18300750101')
# get_db_handler()
