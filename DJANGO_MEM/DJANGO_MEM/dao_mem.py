import pymysql

class DaoMem:
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3305, user='root', passwd='python', db='python', charset='utf8')
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
    
    def selectList(self):
        sql = "SELECT * FROM mem"
        self.curs.execute(sql)
        
        list = self.curs.fetchall()
        return list
    
    def selectOne(self,e_id):
        sql = f"""SELECT * FROM mem WHERE m_id={e_id}"""
        self.curs.execute(sql)
        
        mem = self.curs.fetchall()#fetchone으로도 가능
        return mem[0]
    
    def insert(self,m_id,m_name,tel,address):
        sql = f"""INSERT INTO mem(m_id,m_name,tel,address) 
                  VALUES('{m_id}','{m_name}','{tel}','{address}')"""
        self.curs.execute(sql)
        cnt = self.curs.rowcount
        
        self.conn.commit()
        return cnt
    
    def update(self,m_id,m_name,tel,address):
        sql = f"""UPDATE mem SET m_name = '{m_name}',tel = '{tel}', address = '{address}'
                   WHERE m_id = '{m_id}'"""
        self.curs.execute(sql)
        cnt = self.curs.rowcount
        self.conn.commit()
        return cnt
    
    def delete(self,m_id):
        sql = f"""DELETE FROM mem
                   WHERE m_id = '{m_id}'"""
        self.curs.execute(sql)
        cnt = self.curs.rowcount
        self.conn.commit()
        return cnt
    
    def __del__(self):
        self.curs.close()
        self.conn.close()
       
if __name__ == '__main__':
    de = DaoMem()
    
    #list = de.selectList()
    #print("list",list)
    
    #emp = de.selectOne('1')
    #print("emp",emp)
    
    #cnt = de.delete('6')
    #print("cnt",cnt)
    