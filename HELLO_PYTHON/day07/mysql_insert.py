import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3305, user='root', passwd='python', db='python', charset='utf8')

curs = conn.cursor()
sql = """INSERT INTO 
            emp(e_id,e_name,sex,addr) 
         VALUES('4','4','4','4')""" #줄바꿈 가능

curs.execute(sql)
conn.commit()

curs.close()
conn.close()