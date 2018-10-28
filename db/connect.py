
"""
Reference
https://devcenter.heroku.com/articles/heroku-postgresql#connecting-in-python
"""

import os
import psycopg2
from pympler import tracker




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
        # finally:
        #     if self.conn is not None:
        #         self.conn.close()
        #         print('Database connection closed.')

    def execute_SQL(self, SQL, args):
        """ query data from the vendors table """
        try:

            # conn = psycopg2.connect(**params)
            # self.conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    
            # create a cursor
            self.cur = self.conn.cursor()

            self.cur.execute(SQL, args)
            print("The number of parts: ", self.cur.rowcount)
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

    def AddUser(self, user_id, display_name, picture_url, status_message):

        try:    
            # create a cursor
            self.cur = self.conn.cursor()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        


if __name__ == "__main__":
    
    memory_tracker = tracker.SummaryTracker()
    conn = Heroku_DB()
    # memory_tracker = tracker.SummaryTracker()
    print("test conn finish")
    rows = conn.execute_SQL("select * from userinfo",[])
    if rows != None:
        print("not null, len(rows)={}".format(len(rows)))
        for row in rows:
            print (row)


    # rows = conn.execute_SQL("select * from user_test")
    # if rows != None:
    #     print("not null, len(rows)={}".format(len(rows)))
    #     for row in rows:
    #         print (row)
    # print("test query finish")
    # memory_tracker.print_diff()

    test1 = conn.IsExistUser("test5566")
    
    test2 = conn.IsExistUser("ta")

    print("test1={},test2={}".format(test1, test2))
