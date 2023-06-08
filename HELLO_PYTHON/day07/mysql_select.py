import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3305, user='root', passwd='python', db='python', charset='utf8')

curs = conn.cursor()
sql = "SELECT * FROM emp"

curs.execute(sql)
rows = curs.fetchall()
print(rows)

curs.close()
conn.close()
