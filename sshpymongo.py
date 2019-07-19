# -*- coding: utf-8 -*-
# 2019/05/17
# @Author: JeremyZ

import datetime
import pymongo
import pytz
from sshtunnel import SSHTunnelForwarder

tz = pytz.timezone("Asia/Shanghai")
now = datetime.datetime.now()

def get_mongo_client():
    server = SSHTunnelForwarder(
        ('47.96.88.150', 22),
        ssh_pkey="C:/Users/46765/.ssh/id_rsa",
        ssh_username='root',
        # remote_bind_address=('dds-bp10002287a4b5741.mongodb.rds.aliyuncs.com', 3717))
        remote_bind_address=('172.16.27.232', 27017))
    server.start()

    client = pymongo.MongoClient('127.0.0.1', server.local_bind_port)
    mongo_database = client.admin
    # db = mongo_database.authenticate('zhaozhiming', '123456')
    return client

client = get_mongo_client()
collection = client.ebox
x = collection.community.find({})
for i in x:
    print(i)

client.close()