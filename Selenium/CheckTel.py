# 第二章/checkTel.py
"""
本实例实现对手机号进行电信运营商以及有效内容判断

"""
tel = input("please input telephone number")

if len(tel) == 11:
    if tel.isdigit():
        if tel.startswith("139") or tel.startswith("187"):
            print("China Mobile")
        elif tel.startswith("156") or tel.startswith("177"):
            print("中国联通")
        else:
            print("中国电信")
    else:
        print("你的手机号存在特殊符号")
else:
    print("你的手机号位数不正确")
