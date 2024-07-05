import threading


def square(num):
    for i in num:
        print(i * i)


def cube(num):
    for i in num:
        print(i * i * i)


l1 = [1, 2, 3, 4, 5, 6]

t1 = threading.Thread(target=square, args=(l1,))
t2 = threading.Thread(target=cube, args=(l1,))

t1.start()
t2.start()

t1.join()
t2.join()

print("done")
