import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3305, user='root', passwd='python', db='python', charset='utf8')

e_id = '6'
e_name = '6'
sex = '6'
addr = '6'

curs = conn.cursor()
sql = f"""INSERT INTO
            emp(e_id,e_name,sex,addr)
         VALUES('{e_id}','{e_name}','{sex}','{addr}')""" #줄바꿈 가능
#print("sql",sql)
cnt = curs.execute(sql)
#print(cnt)
print(curs.rowcount)
conn.commit()

curs.close()
conn.close()