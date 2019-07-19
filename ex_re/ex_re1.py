# -*- coding: utf-8 -*-
# 2019/06/24
# @Author: JeremyZ

import re
# "\w+-\d+", 'jlkk123-555' 一个由字母数字组成的字符串和一串由一个连字符隔开的数字
# "[A-Za-z]\w*", "sdj1354skdkj" 第一个字符为字母；其余字符可以是字符或者是数字
# "\d{3}-\d{3}-\d{4}", "123-456-7890"  美国电话号码格式
# "\w+@\w+\.com", "314067448@qq.com"  电子邮件格式
# "\d+(\.\d*)?", "22.55"  简单浮点数的字符串
# "(Mr?s?\.)?[A-Za-z]*[A-Za-z]+", "Mrs.li"  姓氏
# x = re.compile("\w+-\d+")
# # x = re.match()
# if x is not None:
#     # y = x.group()
#     print(x)
#
# site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
# pop_obj=site.pop('name')
# print(pop_obj)    # 输出 ：菜鸟教程
# print(site)