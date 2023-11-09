import os
import signal


def do_fork():
    new_child = os.fork()
    if new_child < 0:
        return do_fork()
    return new_child


def get_string(arr):
    return str(arr)[2:-3]


def read(pipe):
    data1 = b""
    while True:
        sign = os.read(pipe, 1)
        data1 += sign
        if sign == b"\n":
            return data1
        if sign == b"":
            return -1


def proceduredHandler(s, f):
    print("Procedured: ", procedured)


p1r, p1w = os.pipe()
p02r, p02w = os.pipe()
p20r, p20w = os.pipe()

childPid = do_fork()
if childPid == 0:
    os.dup2(p1w, 1)
    os.execl("producer", "producer")
os.close(p1w)

childPid = do_fork()
if childPid == 0:
    os.dup2(p02r, 0)
    os.dup2(p20w, 1)
    os.execl("/usr/bin/bc", "bc")
os.close(p02r)
os.close(p20w)

procedured = 0
signal.signal(10, proceduredHandler)

while True:
    data = read(p1r)
    if data == -1:
        exit(0)
    os.write(p02w, data)
    data2 = read(p20r)
    print(get_string(data) + " = " + get_string(data2))
    procedured += 1
