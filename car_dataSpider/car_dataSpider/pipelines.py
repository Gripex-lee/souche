# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class CarDataspiderPipeline(object):
    def process_item(self, item, spider):
        return item

class MysqlPipeline(object):
    '''
    插入mysql数据库
    '''
    def __init__(self):
        self.conn =pymysql.connect(host='localhost',port=3306,user='root',passwd='liwenwu.610',db='cardata',use_unicode=True, charset="utf8")
        self.cursor = self.conn.cursor()

    def process_item(self,item,spider):
        insert_sql = '''
        insert into che(title,time,milestone,gGB,price,new_price) VALUES (%s,%s,%s,%s,%s,%s)
        '''

        self.cursor.execute(insert_sql,(item["title"],item["time"],item["milestone"],item["gGB"],item["price"],item["new_price"]))
        self.conn.commit()

#,li_cheng,start_time,emission,own_time,use_type,nian_jian,bao_xian,vendor,car_type,car_color,sets,displacement,transmission,fuel,drive_mode,oil_cost
#,item["li_cheng"],item["start_time"],item["emission"],item["own_time"],item["use_type"],item["nian_jian"],item["bao_xian"],item["vendor"],item["car_type"],item["car_color"],item["sets"],item["displacement"],item["transmission"],item["fuel"],item["drive_mode"],item["oil_cost"]

# create table che(price varchar(300),li_cheng varchar(300),start_time varchar(300),emission varchar(300),own_time varchar(300),use_type varchar(300),nian_jian varchar(300),bao_xian varchar(300),vendor varchar(300),car_type varchar(300),car_color varchar(300),sets varchar(300),displacement varchar(300),transmission varchar(300),fuel varchar(300),drive_mode varchar(300),oil_cost varchar(300));

#create table souche(brand char(200),time char(200),milestone char(200),gGB char(200),env char(200),displacement char(200),oil char(200),fadongji char(200),price char(200),new_price char(200));