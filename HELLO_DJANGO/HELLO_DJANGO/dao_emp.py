import pymysql

class DaoEmp:
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3305, user='root', passwd='python', db='python', charset='utf8')
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
    
    def selectList(self):
        sql = "SELECT * FROM emp"
        self.curs.execute(sql)
        
        list = self.curs.fetchall()
        return list
    
    def selectOne(self,e_id):
        sql = f"""SELECT * FROM emp WHERE e_id={e_id}"""
        self.curs.execute(sql)
        
        emp = self.curs.fetchall()#fetchone으로도 가능
        return emp[0]
    
    def insert(self,e_id,e_name,sex,addr):
        sql = f"""INSERT INTO emp(e_id,e_name,sex,addr) 
                  VALUES('{e_id}','{e_name}','{sex}','{addr}')"""
        self.curs.execute(sql)
        cnt = self.curs.rowcount
        
        self.conn.commit()
        return cnt
    
    def update(self,e_id,e_name,sex,addr):
        sql = f"""UPDATE emp SET e_name = '{e_name}',sex = '{sex}', addr = '{addr}'
                   WHERE e_id = '{e_id}'"""
        self.curs.execute(sql)
        cnt = self.curs.rowcount
        self.conn.commit()
        return cnt
    
    def delete(self,e_id):
        sql = f"""DELETE FROM emp
                   WHERE e_id = '{e_id}'"""
        self.curs.execute(sql)
        cnt = self.curs.rowcount
        self.conn.commit()
        return cnt
    
    def __del__(self):
        self.curs.close()
        self.conn.close()
       
if __name__ == '__main__':
    de = DaoEmp()
    
    #list = de.selectList()
    #print("list",list)
    
    #emp = de.selectOne('1')
    #print("emp",emp)
    
    cnt = de.delete('6')
    print("cnt",cnt)
    