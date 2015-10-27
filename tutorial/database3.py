


import sqlite3

conn = sqlite3.connect('mytest.db')
cursor = conn.cursor()
sql = ''' select * from students'''
results = cursor.execute(sql)
all_students = results.fetchall()
print(all_students)


