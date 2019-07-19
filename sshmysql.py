# -*- coding: utf-8 -*-
# 2019/05/17
# @Author: JeremyZ

import datetime
import pymysql
import pytz
from sshtunnel import SSHTunnelForwarder
from pymysql.cursors import DictCursor

tz = pytz.timezone("Asia/Shanghai")
now = datetime.datetime.now()

with SSHTunnelForwarder(
        ("47.96.88.150", 22),  # B机器的配置
        ssh_password='',
        ssh_pkey="C:/Users/46765/.ssh/id_rsa",
        ssh_username='root',
        remote_bind_address=('172.16.27.236', 3306)) as server:  # A机器的配置

    db_connect = pymysql.connect(host='127.0.0.1',  # 此处必须是是127.0.0.1
                                 port=server.local_bind_port,
                                 user='root',
                                 passwd="123456",
                                 db='factdb')

    sql = "select * from canopy"

    cur = db_connect.cursor(DictCursor)
    cur.execute(sql, )
    db_connect.commit()
    x = cur.fetchall()
    for i in x:
        print(i)
    db_connect.close()