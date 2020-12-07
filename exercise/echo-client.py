import socket
import math

HOST = '127.0.0.1'
PORT = 8992

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    picpath = '/home/hatsunehan/图片/初音未来壁纸_粉.png'
    sp = open(picpath, 'rb').read()
    piclength = len(sp)
    num = math.ceil(piclength / 1024)
    s.sendall(str.encode("ADD Student_info SITP/1.0" +
                         '\n' + "18300750006 韩晓宇 "+str(piclength)+'\n'))
    print("ADD Student_info SITP/1.0" +
          '\n' + "18300750006 韩晓宇 "+str(piclength)+'\n')
    data = s.recv(1024)
    if data == str.encode("allowed"):
        for i in range(0, num):
            if (i != num - 1):
                s.sendall(sp[1024 * i:1024 * (i + 1)])
            else:
                s.sendall(sp[1024 * i:piclength])
    data = s.recv(1024)
    if (data == str.encode("finished")):
        s.sendall(str.encode("end"))
