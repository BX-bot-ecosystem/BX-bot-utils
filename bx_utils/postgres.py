import logging

import psycopg2
import os


class Postgres:
    def _connect(self):
        try:
            connection = psycopg2.connect(
                database=os.getenv("POSTGRES_DATABASE"),
                user=os.getenv("POSTGRES_USER"),
                password=os.getenv("POSTGRES_PASSWORD"),
                host=os.getenv("POSTGRES_HOST"),
                port=int(os.getenv("POSTGRES_PORT"))
            )
            return connection
        except (Exception, psycopg2.DatabaseError) as e:
            logging.error(e)
    
    def board(self):
        connection = self._connect()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT firstname, lastname, role, message FROM")
        except (Exception, ) as e:
            logging.error(e)
        finally:
            connection.close()
            
        


