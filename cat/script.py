from builtins import PythonFinalizationError

if __name__ == '__main__':
    # 5
    language = "123456789"
    # 8
    language1 = "123456789"
    # a = language[-7::2]#每两个元素取第一个元素
    # print(a)
    # b = language[-1:-7:-1]
    # print(b)
    # c =language[-7:-1:-1]
    # print(c)      #?????
    # d = language[-7::-1]
    # print(d)
    # print(len(language))

    # q = int(language[5::1])
    # w = int(language1[8::])
    # e = int(q+w)
    # print("q="+str(q))
    # print("w="+str(w))
    # print("e="+str(e))
    #
    # print("q+w="+str(int(language[5::1])+(int(language1[8::]))))
    # s = str("1111")
    # s1 = f"11111"
    # print(s)
    # # print("q+w="+11)
    users = ["Linda","Brian"]
    users.append("Jennfer")
    print(users)
    users.insert(2,"Kim")
    print(users)
    del users[3]
    print(users)
    print(len(users))
    print("Linda" in users)
    print(sorted(users))
    print("free" in "Python is free")


