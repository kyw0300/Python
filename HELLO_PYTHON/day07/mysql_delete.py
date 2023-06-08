import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3305, user='root', passwd='python', db='python', charset='utf8')

e_id = '6'

curs = conn.cursor()
sql = f"""DELETE FROM emp
            WHERE e_id = '{e_id}'""" #줄바꿈 가능
print("sql",sql)

cnt = curs.execute(sql)
#print(cnt)
print(curs.rowcount) #rowcount 쓰는게 더 좋다.
conn.commit()

curs.close()
conn.close()