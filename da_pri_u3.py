import sqlite3
cn=sqlite3.connect('vtp.db')
print('connect sucess')
cur=cn.cursor()
q="create table sybcaa(cid,name,loc)"
cn.execute(q)
print('table created')
cn.commit()