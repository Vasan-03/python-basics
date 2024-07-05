# def vasan():
#     print("hi vasan")

# vasan()

#using arguments

# def vasan(x,y):
#     print(x+y)
#
# vasan(1,2)

#if function is in return statement,this is the way for calling function

def vasan(x,y):
    print("hi")
    return x+y
#
#
# res = vasan(1,2)
# print(res)

#multiple return values

# def vasan(x,y,z):
#     res1 = (x + y + z)
#     res2 = (x - y - z)
#     res3 = (x + y - z)
#     return res1,res2,res3
#
# res=vasan(1,2,3)
# print(res)

#local and global variable concept

# any variable created outside the function is global Variable
#
# place = "bengaluru"
# def vasan(x,y):
#     print("place:",place)
#     return x+y
# res = vasan(1,2)
# print(res)

# any variable created inside the function is Local Variable

# def vasan(x,y):
#     place = "bengaluru"
#     print("place:",place)
#     return x+y
# res = vasan(1,2)
# print(res)

#we can use local variable as global variable using keyword global

# def vasan(x,y):
#     global name
#     name = "sathish"
#     place = "bengaluru"
#     print("place:",place)
#     return x+y
# res = vasan(1,2)
# print(res)
# print(name)

# types of UDF

# 1. required and positional arg

# def test(x,y,z):
#     res = x + y + z
#     return res
#
# res = test(20,10,5)
# print(res)

# # 2. required and non positional keyword  arg

# def test(x,y,z):
#     res = x + y + z
#     return res
#
# res = test(y = 'kumar',z = 'yadav', x = 'santhosh')
# print(res)

# 3. default arg func

# def test(x=200,y=300,z=500):
#     res = x + y + z
#     return res
#
# res = test()
# print(res)

# 4. variable length arg func
# Var length arg should always be at last

# def vasan(*x):
#     print(x)
# vasan(1,2,3)

# def vasan(*x):
#     print(x[0])
# vasan(1,2,3)

# def vasan(**data):
#     print(data)
# vasan(name="vasan",age=20)

# def vasan(**data):
#     print(data["name"])
# vasan(name="vasan",age=20)



