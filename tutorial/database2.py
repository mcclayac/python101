import sqlite3

conn = sqlite3.connect('mytest.db')

cursor = conn.cursor()

sqlString = '''insert into students2
  (name, username, id) values
  ('Jannet', 'janjan02', 12)'''


#sql = '''insert into students
#  (name, username, id) values
#  (:st_name, :st_username, 11)'''
print(sqlString)
cursor.execute(sqlString)


#cursor.execute(sql,
#               {'st_name': 'Jacob',
#                'st_username': 'Starweather'})
               #,
               # 'id_num:': 45})

cursor.close()


#print(errorCode)


