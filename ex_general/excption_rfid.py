# -*- coding: utf-8 -*-
# 2019/05/15
# @Author: JeremyZ

import datetime
import pymysql
import pytz
from sshtunnel import SSHTunnelForwarder
from pymysql.cursors import DictCursor

# db = pymysql.Connect(host='172.16.27.236', user='root', passwd='123456', db='factdb', port=3306)
# cur = db.cursor(DictCursor)
#
# now_1=datetime.datetime.now(pytz.timezone("Asia/Shanghai")).replace(hour=0, minute=0, second=0) - datetime.timedelta(days=1)
# now_2=datetime.datetime.now(pytz.timezone("Asia/Shanghai")).replace(hour=23, minute=59, second=59) - datetime.timedelta(days=1)
#
# x={}
# y = []
# for i in range(100):
#     sql = "select * from dim_rfid_check where eog_created_at is between %s and %s and if_error=%s limit 1000 offset %s"
#     cur.execute(sql, (now_1, now_2, 1, i))
#     excptions = cur.fetchall()
#     for j in excptions:
#         if j['rfid'] not in x:
#             x[j['rfid']] = [j]
#             y.append(j)
#         else:
#             for m in x[j['rfid']]:
#                 if m['tor_id'] != j['tor_id']:
#                     x[j['rfid']].append(j)
#                     y.append(j)
#
#     if len(excptions) == 0:
#         break
# print(y)





