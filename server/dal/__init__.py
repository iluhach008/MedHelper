import psycopg2
from psycopg2 import extras
# Подключение к БД
conn = psycopg2.connect(dbname='is', user='postgres', password='root', host='localhost')
cursor = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)