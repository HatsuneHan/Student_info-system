import socket
from threadpool import ThreadPoolManager
import math
import os
import shutil
import sys
import re
from mydb import *
HOST = '127.0.0.1'
PORT = 8993

thread_pool = ThreadPoolManager(5)


def getstate(sitp):
    sitparray = sitp.split(str.encode('\n'))
    sitpinf = sitparray[0].split(str.encode(' '))
    return bytes.decode(sitpinf[1])


def getreason(sitp):
    sitparray = sitp.split(str.encode('\n'))
    sitpinf = sitparray[0].split(str.encode(' '))
    return bytes.decode(sitpinf[2])


def add_handler(id, name, picform, piclength, connection):
    if (id == None or name == None or picform == None or piclength == None or piclength == 0):
        connection.sendall(str.encode(
            'SITP/1.0' + ' ' + '400' + ' ' + 'Bad Request' + '\n'))
        return

    num = math.ceil(piclength / 1024)
    pic = str.encode("")
    print("The file will be", piclength, "bytes")
    connection.sendall(str.encode(
        'SITP/1.0' + ' ' + '200' + ' ' + 'OK' + '\n'))
    for i in range(0, num):
        picsec = connection.recv(1024)
        pic += picsec
    picpath = '/home/hatsunehan/文档/Lesson/计算机网络/实验课/PJ/serverroot/'+id+'.'+picform
    ans = open(picpath, 'wb')
    ans.write(pic)
    connection.sendall(str.encode(
        'SITP/1.0' + ' ' + '200' + ' ' + 'OK' + '\n'))
    print("receive successfully")
    add_db_handler(id, name, picpath)


def del_handler(id, connection):
    if (id == None):
        connection.sendall(str.encode(
            'SITP/1.0' + ' ' + '400' + ' ' + 'Bad Request' + '\n'))
        return
    del_db_handler(id)
    L = [x for x in os.listdir(
        '/home/hatsunehan/文档/Lesson/计算机网络/实验课/PJ/serverroot')]
    for name in L:
        if re.match(id, name) != None:
            os.remove('/home/hatsunehan/文档/Lesson/计算机网络/实验课/PJ/serverroot/'+name)
    connection.sendall(str.encode(
        'SITP/1.0' + ' ' + '200' + ' ' + 'OK' + '\n'))
    print("delete successfully")


def get_handler(connection, pageno):

    connection.sendall(str.encode(
        'SITP/1.0' + ' ' + '200' + ' ' + 'OK' + '\n'))

    infArray = get_db_handler(pageno)
    idArray = infArray[0]
    nameArray = infArray[1]
    pathArray = infArray[2]

    print(len(idArray))
    if (len(idArray) == 0):
        sitp = str.encode(
            'NOP' + ' ' + 'Student_information' + ' ' + 'SITP/1.0' + '\n' + '\n')
        connection.sendall(sitp)

    for i in range(0, len(idArray)):
        id = idArray[i]
        name = nameArray[i]
        picpath = pathArray[i]
        if (i == len(idArray) - 1):
            ctn = "0"
        else:
            ctn = "1"
        picform = picpath.split(".")[-1]
        try:
            picinf = open(picpath, 'rb').read()
        except:
            print("File Not Found")
            return
        piclength = len(picinf)
        num = math.ceil(piclength / 1024)
        sitp = str.encode(
            'ANS' + ' ' + 'Student_information' + ' ' + 'SITP/1.0' + '\n')
        sitp += str.encode(id) + str.encode(' ') + str.encode(name) + str.encode(
            ' ') + str.encode(picform) + str.encode(' ') + str.encode(str(piclength)) + str.encode(' ') + str.encode(ctn) + str.encode('\n')
        connection.sendall(sitp)
        preresponse = connection.recv(1024)
        if (getstate(preresponse) == "200"):
            print(
                'Connect successfully! Begin transfer picture with length of', piclength)
            for i in range(0, num):
                if (i != num - 1):
                    connection.sendall(picinf[1024 * i:1024 * (i + 1)])
                else:
                    connection.sendall(picinf[1024 * i:piclength])
        else:
            print(getreason(preresponse))
            print('Exit successfully!')
            return
        finalresponse = connection.recv(1024)
        if (getstate(finalresponse) == "200"):
            print('Transfer successfully!')
        else:
            print('Error!')


def exc_handler(connection):
    connection.sendall(str.encode('SITP/1.0' + ' ' +
                                  '400' + ' ' + 'Bad Request' + '\n'))


def request_handler(index, sock, connection):
    try:
        print("begin connection %d" % index)
        connection.settimeout(50)
        while True:
            sitp = connection.recv(1024)
            sitparray = sitp.split(str.encode('\n'))
            sitpinf = sitparray[0].split(str.encode(' '))
            sitpmethod = bytes.decode(sitpinf[0])

            if (sitpmethod == "ADD"):
                sitpcontent = sitparray[1].split(str.encode(' '))
                add_handler(bytes.decode(sitpcontent[0]), bytes.decode(sitpcontent[1]), bytes.decode(sitpcontent[2]),
                            int(bytes.decode(sitpcontent[3])), connection)  # all type bytes
                break
            elif (sitpmethod == "DEL"):
                sitpcontent = sitparray[1].split(str.encode(' '))
                del_handler(bytes.decode(sitpcontent[0]), connection)
                break
            elif (sitpmethod == "GET"):
                sitpcontent = sitparray[1].split(str.encode(' '))
                get_handler(connection, int(sitpcontent[0]))
                break
            else:
                exc_handler(connection)
                break

    except socket.timeout:
        print("time out")

    print("closing connection %d" % index)
    connection.close()


if __name__ == "__main__":
    print("Server is starting")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(5)
    print("Server is listening port " + str(PORT) + ", with max connection 5")
    index = 0
    while True:
        connection, address = sock.accept()
        index += 1
        thread_pool.add_job(request_handler, *(index, sock, connection))
        if index > 20:
            break
