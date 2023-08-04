import psycopg2
from psycopg2 import pool

def connect_db():
  try:
    db_pool = pool.SimpleConnectionPool(1, 20, user='ecommerce', password='ecommerce', host='127.0.0.1', database='ecommerce')

    return db_pool

  except (Exception, psycopg2.DatabaseError) as e:
    print('Cannot connect to database', e)