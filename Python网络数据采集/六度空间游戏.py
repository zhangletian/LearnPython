from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql

coon = pymysql.connect(host = '127.0.0.1',unix_socket = '/tmp/mysql.sock',
						user = 'root',passwd = None,db = 'mysql',charset = 'utf8')
cur = conn.cursor()
cur.execute('USE wikipedia')

def 
