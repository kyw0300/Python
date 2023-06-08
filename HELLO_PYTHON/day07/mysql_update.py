import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3305, user='root', passwd='python', db='python', charset='utf8')

e_id = '6'
e_name = '9'
sex = '9'
addr = '9'

curs = conn.cursor()
sql = f"""UPDATE emp SET e_name = '{e_name}',sex = '{sex}', addr = '{addr}'
            WHERE e_id = '{e_id}'""" #줄바꿈 가능
print("sql",sql)

cnt = curs.execute(sql)
#print(cnt)
print("cnt",curs.rowcount) #rowcount 쓰는게 더 좋다.
conn.commit()

curs.close()
conn.close()