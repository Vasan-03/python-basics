mobilenum = input("Mobile-Num:")
res1 = len(mobilenum)
res2 = mobilenum.isdigit()
if mobilenum == "":
    print("please enter a number")
elif res1 == 10 and not res2:
    print("valid number")
elif not res2:
    print("ERROR:you typed words instead of number,please enter a number")
elif res1 < 10 or res1 > 10:
    print("ERROR:your number must be 10 digit")
else:
    print("ERROR:invalid number")
