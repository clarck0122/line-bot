
"""
Reference
https://devcenter.heroku.com/articles/heroku-postgresql#connecting-in-python
"""

import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

class Heroku_DB():

    def __init__(self):
        """ Connect to the PostgreSQL database server """
        try:
            # read connection parameters
            # params = config()
    
            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
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
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()
                print('Database connection closed.')

if __name__ == "__main__":
    conn = Heroku_DB()
    print("close")