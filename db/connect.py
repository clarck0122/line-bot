
"""
Reference
https://devcenter.heroku.com/articles/heroku-postgresql#connecting-in-python
"""

import os
import psycopg2
from pympler import tracker
import datetime
import time

# get API Keys from Heroku Postgresql
DATABASE_URL = os.environ['DATABASE_URL']

class Heroku_DB():

    def __init__(self):
        """ Connect to the PostgreSQL database server """
        try:
            # read connection parameters
            # params = config()
    
            # connect to the PostgreSQL server
            print("Connecting to the PostgreSQL database...{}".format(DATABASE_URL))
            # conn = psycopg2.connect(**params)
            self.conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    
            # create a cursor
            self.cur = self.conn.cursor()
            
        # execute a statement
            print('PostgreSQL database version:')
            self.cur.execute('SELECT version()')
    
            # display the PostgreSQL database server version
            db_version = self.cur.fetchone()
            print(db_version)
        
        # close the communication with the PostgreSQL
            self.cur.close()
            self.cur = None
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()
                # print('Database connection closed.')

    def Reconnect(self):
        print("Reconnect...")
        self.conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        self.cur = self.conn.cursor()

    def execute_SQL(self, SQL, args):
        """ query data from the vendors table """
        try:
            # create a cursor
            self.cur = self.conn.cursor()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            self.Reconnect()

        try:
            self.cur.execute(SQL, args)
            # print("The number of parts: ", self.cur.rowcount)
            # row = self.cur.fetchone()
            rows = self.cur.fetchall()
    
            # close the communication with the PostgreSQL
            self.cur.close()
            self.cur = None
            return rows

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


    def IsExistUser(self, user_id):
        # rows = self.execute_SQL("SELECT count(*) FROM userinfo WHERE user_id LIKE %s", [ user_id + '%' ])
        rows = self.execute_SQL("SELECT count(*) FROM userinfo WHERE user_id = %s", [ user_id ])

        if rows == None:
            return False
        else:        
            return rows[0][0] == 1

    def GetUserInfo(self, user_id):
        # rows = self.execute_SQL("SELECT count(*) FROM userinfo WHERE user_id LIKE %s", [ user_id + '%' ])
        rows = self.execute_SQL("SELECT user_id, display_name, picture_url, status_message FROM userinfo WHERE user_id = %s", [ user_id ])
        
        return rows[0]

    def AddUser(self, user_id, display_name , picture_url , status_message ):
        
        if not display_name: display_name = ""
        if not picture_url: picture_url = ""
        if not status_message: status_message = ""

        try:    
            # create a cursor
            self.cur = self.conn.cursor()
            

        except (Exception) as error:
            print(error)
            self.Reconnect()
        
        try:
            print(datetime.datetime.now())
            ts = time.time()
            SQL = "INSERT INTO userinfo (user_id, display_name, picture_url, status_message) VALUES (%s, %s, %s, %s)"
            self.cur.execute(SQL, [user_id, display_name, picture_url, status_message])
            self.conn.commit()

            self.cur.close()
            self.cur = None

        except (Exception, psycopg2.DatabaseError) as error:
            self.conn.rollback()
            print(error)


    def UpdateUser(self, user_id, display_name, picture_url, status_message):

        if not display_name: display_name = ""
        if not picture_url: picture_url = ""
        if not status_message: status_message = ""

        try:    
            # create a cursor
            self.cur = self.conn.cursor()            

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            self.Reconnect()

        try:
            SQL = "UPDATE userinfo SET display_name = %s, picture_url = %s, status_message = %s, createdate=%s WHERE user_id = %s"
            self.cur.execute(SQL, [display_name, picture_url, status_message, datetime.datetime.now(), user_id])
            self.conn.commit()

            self.cur.close()
            self.cur = None
            
        except (Exception, psycopg2.DatabaseError) as error:
            self.conn.rollback()
            print(error)

        # finally:
        #     if self.conn is not None:
        #         self.conn.close()



if __name__ == "__main__":
    
    memory_tracker = tracker.SummaryTracker()
    conn = Heroku_DB()

    # test1 = conn.IsExistUser("test5566")
    
    # test2 = conn.IsExistUser("ta")

    # print("test1={},test2={}".format(test1, test2))

    

    conn.AddUser('test20181104-1','大慶', 'http://ptt.cc/black', '歲月就像把殺豬刀')
    conn.conn.close()    
    conn.AddUser('test20181104-2','大慶', 'http://ptt.cc/black', '歲月就像把殺豬刀')

    conn.UpdateUser('test20181104-1','大慶', 'http://ptt.cc/black', '測試')
    conn.conn.close()    
    conn.UpdateUser('test20181104-2','大慶', 'http://ptt.cc/black', '測試')

    # conn.UpdateUser('test1234', '阿偉', 'http://ptt.cc/black', '放管中x4')

    # test3 = conn.GetUserInfo('test5566')
    # print("test3={}".format(test3))

    # conn.AddUser('test12357','大慶', None, None)