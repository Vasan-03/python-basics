# try:
#     a = int(input("Provide a number:"))
#     b = int(input("Provide a number:"))
#     print(a + b)
# except Exception as e:
#     print("error:", e)


# try:
#         mobilenum = input("Mobile-Num:")
#         res1 = len(mobilenum)
#         res2 = mobilenum.isdigit()
#         if mobilenum == "":
#             raise Exception("please enter a number")
#         elif res1 == 10 and res2 == True:
#             raise Exception("valid number")
#         elif res2 == False:
#             raise Exception("ERROR:you typed words instead of number,please enter a number")
#         elif res1 < 10 or res1 > 10:
#             raise Exception("ERROR:your number must be 10 digit")
#         else:
#             raise Exception("ERROR:invalid number")
# except Exception as e:
#         print(e)

# try:
#     fvar = open(r'C:\python-basics\test1','r')
# except Exception as e:
#     print(e,"lets create new file")
#     fvar = open(r'C:\python-basics\test1', 'w')
# finally:
#     fvar.close()


age = int(input("age:"))
def calculate(value):
  assert value>0,"age must be greater than 0"
  print(value)

calculate(age)



# age = int(input("age:"))
# try:
#     assert age>0,"hey boss please enter valid age"
#     print(age)
# except Exception as e:
#     print("err:",e)



