#encoding: utf-8
import MySQLdb
class DealFile:
    """
    处理各种文件
    """
    def __init__(self):
        self.db = MySQLdb.connect("localhost", "root", "pass", "cee", charset="utf8")
        self.cursor = self.db.cursor()

    def read_oneline(self, filename):
        """
        读取文件数据
        :param filename:文件名字
        :return: 逐行返回数据
        """
        with open(filename, "r") as f:
            for line in f.readlines():
                yield line

    def insert_mysql_online(self, table, key, value):
        """
        将每行数据插入数据库
        :return:
        """
        string_key = ""
        for x in key:
            string_key += x+","
        string_key = string_key[0:-1]

        string_value = ""
        for x in value:
            string_value += '"'+x+'"'+','
        string_value = string_value[0:-1]

        sql = 'INSERT INTO %s (%s) VALUES (%s)' % (table, string_key, string_value)

        flag = self.cursor.execute(sql)
        self.db.commit()
        if(flag):
            return "success"

        #print sql

    def deal_file_insert_mysql(self, table, filename, key):
        """
        逐行处理数据并插入数据库
        :param filename:
        :return:
        """
        list = []
        list_new = []
        for line in self.read_oneline(filename):
            list = line.split(',')
            for x in list:
                list_new.append(x.strip())
            print self.insert_mysql_online(table, key, list_new)
            # print list_new
            list_new = []


if  __name__ == "__main__":
    filename = '../geshengfenshu/1.csv'
    table = 'think_major_info'
    key = [ "major_cn_name", "major_province_ch_name", "major_class", "major_max", "major_min", "major_aver", "major_year", "major_lever"]
    d = DealFile()
    d.deal_file_insert_mysql(table,filename, key)

