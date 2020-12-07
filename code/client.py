import socket
import math

HOST = '127.0.0.1'
PORT = 8993


def encodesitp(func, id=None, name=None, picpath=None):
    if (func == 'ADD'):
        picform = picpath.split(".")[-1]
        piclength = len(open(picpath, 'rb').read())
        sitp = str.encode(
            'ADD' + ' ' + 'Student_information' + ' ' + 'SITP/1.0' + '\n')
        sitp += str.encode(id) + str.encode(' ') + str.encode(name) + str.encode(
            ' ') + str.encode(picform) + str.encode(' ') + str.encode(str(piclength)) + str.encode('\n')
    elif (func == "DEL"):
        sitp = str.encode('DEL'+' '+'Student_information'+' '+'SITP/1.0'+'\n')
        sitp += str.encode(id) + str.encode('\n')
    else:
        sitp = str.encode(
            'GET' + ' ' + 'Student_information' + ' ' + 'SITP/1.0' + '\n')
        sitp += str.encode('\n')
    return sitp


def getstate(sitp):
    sitparray = sitp.split(str.encode('\n'))
    sitpinf = sitparray[0].split(str.encode(' '))
    return bytes.decode(sitpinf[1])


def getreason(sitp):
    sitparray = sitp.split(str.encode('\n'))
    sitpinf = sitparray[0].split(str.encode(' '))
    return bytes.decode(sitpinf[2])


def sendrequest(func, sitp):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        s.sendall(sitp)

        laterresponse = s.recv(1024)
        if (getstate(laterresponse) == "200"):
            s.sendall(encodesitp("END"))
            print('Success!')
        else:
            print('Error!')
        # print(bytes.decode(encodesitp("END")))

        finalresponse = s.recv(1024)
        if (getstate(finalresponse) == "200"):
            print('Exit successfully!')
        else:
            print('Error!')


def send_add_req(id, name, picpath):
    picform = picpath.split(".")[-1]
    try:
        picinf = open(picpath, 'rb').read()
    except IOError:
        print("File Not Found")
        return
    piclength = len(picinf)
    num = math.ceil(piclength / 1024)
    sitp = str.encode(
        'ADD' + ' ' + 'Student_information' + ' ' + 'SITP/1.0' + '\n')
    sitp += str.encode(id) + str.encode(' ') + str.encode(name) + str.encode(
        ' ') + str.encode(picform) + str.encode(' ') + str.encode(str(piclength)) + str.encode('\n')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(sitp)
        preresponse = s.recv(1024)

        if (getstate(preresponse) == "200"):
            print(
                'Connect successfully! Begin transfer picture with length of', piclength)
            for i in range(0, num):
                if (i != num - 1):
                    s.sendall(picinf[1024 * i:1024 * (i + 1)])
                else:
                    s.sendall(picinf[1024 * i:piclength])
        else:
            print(getreason(preresponse))
            print('Exit successfully!')
            return

        finalresponse = s.recv(1024)
        if (getstate(finalresponse) == "200"):
            print('Exit successfully!')
        else:
            print('Error!')


def send_del_req(id):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        sitp = str.encode('DEL'+' '+'Student_information'+' '+'SITP/1.0'+'\n')
        sitp += str.encode(id) + str.encode('\n')

        s.sendall(sitp)

        laterresponse = s.recv(1024)
        if (getstate(laterresponse) == "200"):
            print('Del successfully!')
        else:
            print('Error!')


def send_get_req(pageno):
    idArray = []
    nameArray = []
    pathArray = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        sitp = str.encode(
            'GET' + ' ' + 'Student_information' + ' ' + 'SITP/1.0' + '\n')
        sitp += str.encode(str(pageno)) + str.encode('\n')

        s.sendall(sitp)

        laterresponse = s.recv(1024)
        if (getstate(laterresponse) == "200"):
            print('Prepare to get!')
        else:
            print('Error!')
        while True:
            sitp = s.recv(1024)
            sitparray = sitp.split(str.encode('\n'))
            sitpinf = sitparray[0].split(str.encode(' '))
            sitpmethod = bytes.decode(sitpinf[0])
            if (sitpmethod == "NOP"):
                print("No inf to get")
                break

            sitpcontent = sitparray[1].split(str.encode(' '))

            id = bytes.decode(sitpcontent[0])
            idArray.append(id)
            name = bytes.decode(sitpcontent[1])
            nameArray.append(name)
            picform = bytes.decode(sitpcontent[2])
            piclength = int(bytes.decode(sitpcontent[3]))
            ctn = bytes.decode(sitpcontent[4])
            num = math.ceil(piclength / 1024)

            pic = str.encode("")
            print("The file will be", piclength, "bytes")
            s.sendall(str.encode(
                'SITP/1.0' + ' ' + '200' + ' ' + 'OK' + '\n'))
            for i in range(0, num):
                picsec = s.recv(1024)
                pic += picsec
            picpath = '/home/hatsunehan/文档/Lesson/计算机网络/实验课/PJ/clientroot/' + id + '.' + picform
            pathArray.append(picpath)
            ans = open(picpath, 'wb')
            ans.write(pic)
            s.sendall(str.encode(
                'SITP/1.0' + ' ' + '200' + ' ' + 'OK' + '\n'))
            print("receive successfully")
            if (ctn == "0"):
                print("get all")
                break
    while len(idArray) < 4:
        idArray.append("None")
        nameArray.append("None")
        pathArray.append(
            "/home/hatsunehan/文档/Lesson/计算机网络/实验课/PJ/serverroot/None.png")
    return [idArray, nameArray, pathArray]


# send_add_req("18301070018", "小李", "/home/hatsunehan/图片/深海初音.jpg")
# send_del_req("18300750006")

# print(send_get_req(3))

# sitp = encodesitp("ADD", "18300750006", "hxy",
#   '/home/hatsunehan/图片/初音未来壁纸_粉.png')
# print(len(sitp))
# sitparray = sitp.split(str.encode('\n'))
# print(bytes.decode(sitparray[1].split(str.encode(' '))[2]))
# sitpinf = sitparray[1].split(str.encode(' '))
# print(bytes.decode(sitpinf[3]))
