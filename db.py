import sqlite3

class Database:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        sql="""
        CREATE TABLE IF NOT EXISTS students(
            id Integer Primary Key,
            name text,
            age text,
            dob text,
            email text,
            gender text,
            contact text,
            address text
            
            )
        """
        
        self.cur.execute(sql)
        self.con.commit()
        
    #insert
    def insert(self,name,age,dob,email,gender,contact,address):
        self.cur.execute("insert into students values(NULL,?,?,?,?,?,?,?)",(name,age,dob,email,gender,contact,address))
        self.con.commit()
        
    #fetch
    def fetch(self):
        self.cur.execute("SELECT * from students")
        rows=self.cur.fetchall()
        return rows
    
    #delete
    def remove(self,id):
        self.cur.execute("delete from students where id=?",(id,))
        self.con.commit()
        
    #update
    def update(self,id,name,age,dob,email,gender,contact,address):
        self.cur.execute("update students set name=?, age=?, dob=?, email=?, gender=?, contact=?, address=? where id=?",(name,age,dob,email,gender,contact,address,id))
        self.con.commit()





        
s=Database("students.db")