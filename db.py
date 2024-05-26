
import pyodbc
class DataBase:
    def __init__(self):
        self.conn = pyodbc.connect(r'DRIVER={SQL Server};SERVER=DESKTOP-6INPB5Q\SQLEXPRESS;DATABASE=Manage_Tasks;') 
        self.cursor = self.conn.cursor()

    def all_tasks(self):
        tasks = []
        query =  "SELECT * FROM Tasks"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            task = {}
            task['id'] = row[0]
            task['taskTitle'] = row[1]
            task['description'] = row[2]
            task['checked']= row[3]
            task['currentDate']= row[4]
            tasks.append(task)
        #self.cursor.close()
        #self.conn.close()
        return tasks

    def get_task(self,task_Id):
        task = {}
        query = f"select * from Tasks where Id = '{task_Id}'"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            task['id'] = row[0]
            task['taskTitle'] = row[1]
            task['description'] = row[2]
            task['checked']= row[3]
            task['currentDate']= row[4]
        #self.cursor.close()
        #self.conn.close()
        return task
        
    def add_task(self,id_task,title_task,desc_task,checked_task,date_task):
        query = f"INSERT INTO Tasks(Id,Title,Description,Checked,CurrentDate)VALUES('{id_task}','{title_task}','{desc_task}',{checked_task},'{date_task}')"
        self.cursor.execute(query)
        self.conn.commit()
        #self.cursor.close()
        #self.conn.close()

    def delete_task(self, id_task):
        query = f"DELETE FROM Tasks WHERE Id = '{id_task}'"
        self.cursor.execute(query)
        self.conn.commit()
        #self.cursor.close()
        #self.conn.close()

    def update_task(self,id,body):
        query = f"UPDATE Tasks SET Title='{body['Title']}',Description='{body['Description']}' WHERE Id = '{id}'"
        self.cursor.execute(query)
        self.conn.commit()
        #self.cursor.close()
        #self.conn.close() 

    def checked_task(self,id,checked_task):
        query = f"UPDATE Tasks SET Checked={checked_task} WHERE Id = '{id}'"
        self.cursor.execute(query)
        self.conn.commit()
        #self.cursor.close()
        #self.conn.close()
    
    def sort_tasks(self,s):
        tasks =[]
        query = ""
        if s:
            query = f"SELECT * FROM Tasks ORDER BY CurrentDate DESC"
        else:
            query = f"SELECT * FROM Tasks ORDER BY CurrentDate"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            task = {}
            task['id'] = row[0]
            task['taskTitle'] = row[1]
            task['description'] = row[2]
            task['checked']= row[3]
            task['currentDate']= row[4]
            tasks.append(task)
        #self.cursor.close()
        #self.conn.close()
        return tasks
        #self.cursor.close()
        #self.conn.close()
    
    def search_task(self,value):
        tasks = []
        query = f"SELECT * FROM Tasks WHERE (Title like '%{value}%') or (Description like '%{value}%')"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            task = {}
            task['id'] = row[0]
            task['taskTitle'] = row[1]
            task['description'] = row[2]
            task['checked']= row[3]
            task['currentDate']= row[4]
            tasks.append(task)
        return tasks
    
db = DataBase()
#print(db.search_task("up"))
#print(db.sort_tasks())
#db.checked_task(id='bb57160d011445e2b02c41e4',checked_task=0)
#db.update_task(id='bb57160d011445e2b02c41e4',body={'Title':'other title','Description':'hello there is new desc in town'})
#print(db.get_task('Bring Food to my dog'))