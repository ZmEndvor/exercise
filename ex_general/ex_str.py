# -*- coding: utf-8 -*-
# 2019/06/20
# @Author: JeremyZ

s = "abcdabcd1234uiopppl"
# x = filter(lambda x,y: x if y not in s else s, s)
# ss = list(set(s))
# ss.sort(key=s.index)
# x = "".join(ss)
# list(set(s)).sort(key=s.index)
# print(s)
# x = [1,2,99,3,4,5]
# y = [2,3,4,5,6]
# x.extend(y)
# print(list(set(x)))
y = []
l = [y.append(i) for i in s if i not in y]
print("".join(y))