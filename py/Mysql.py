#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pymysql
import sys

class MySQL(object):
    def __init__(self):
        """MySQL Database initialization """
        #try:
        self.conn = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='fygg', charset='utf8')
        print(self.conn)
        #except MySQLdb.Error as e:
        #errormsg = 'Cannot connect to server\nERROR (%s): %s' % (e.args[0], e.args[1])
        #print(errormsg)
        self.cursor = self.conn.cursor()

    def query(self, sql):
        """  Execute SQL statement """
        s=0
        try:
            #print(sql)
            s=self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
        if s!=0 and s!=-1:
            return 1
        return 0

    def show(self, sql):
        """ Return the results after executing SQL statement """
        self.cursor.execute(sql)
        return list(self.cursor.fetchall())

    def __del__(self):
        """ Terminate the connection """
        self.conn.close()
        self.cursor.close()

