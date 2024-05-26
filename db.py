import pyodbc

class DataBase:
    def __init__(self):
        self.connection_string = r'DRIVER={SQL Server};SERVER=DESKTOP-6INPB5Q\SQLEXPRESS;DATABASE=Manage_Tasks;'
    def _connect(self):
        return pyodbc.connect(self.connection_string)

    def all_tasks(self):
        try:
            conn = self._connect()
            cursor = conn.cursor()
            tasks = []
            query =  "SELECT * FROM Tasks"
            cursor.execute(query)
            for row in cursor.fetchall():
                task = {
                    'id': row[0],
                    'taskTitle':row[1],
                    'description':row[2],
                    'checked':row[3],
                    'currentDate':row[4]
                }
                tasks.append(task)
            return tasks
        except Exception as e:
            print(f"Error retrieving all tasks: {e}")
            return None
        finally:
            conn.close()
        
    def get_task(self,task_Id):
        try:
            conn = self._connect()
            cursor = conn.cursor()
            task = {}
            query = f"select * from Tasks where Id = '{task_Id}'"
            cursor.execute(query)
            for row in cursor.fetchall():
                task = {
                    'id':row[0],
                    'taskTitle':row[1],
                    'description':row[2],
                    'checked':row[3],
                    'currentDate':row[4]
                }
            return task
        except Exception as e:
            print(f"Error get task: {e}")
            return None
        finally:
            conn.close()
        
        
    def add_task(self,id_task,title_task,desc_task,checked_task,date_task):
        try:
            conn = self._connect()
            cursor = conn.cursor()
            query = f"INSERT INTO Tasks(Id,Title,Description,Checked,CurrentDate)VALUES('{id_task}','{title_task}','{desc_task}',{checked_task},'{date_task}')"
            cursor.execute(query)
            conn.commit()
        except Exception as e:
            print(f"Error in adding task: {e}")
            return False
        finally:
            conn.close()

    def delete_task(self, id_task):
        try:
            conn = self._connect()
            cursor = conn.cursor()
            query = f"DELETE FROM Tasks WHERE Id = '{id_task}'"
            cursor.execute(query)
            conn.commit()
        except Exception as e:
            print(f"Error deleteting task: {e}")
            return False
        finally:
            conn.close()
    def update_task(self,id,body):
        try:
            conn = self._connect()
            cursor = conn.cursor()
            query = f"UPDATE Tasks SET Title='{body['Title']}',Description='{body['Description']}' WHERE Id = '{id}'"
            cursor.execute(query)
            conn.commit()
        except Exception as e:
            print(f"Error updating task: {e}")
            return False 
        finally:
            conn.close()

    def checked_task(self,id,checked_task):
        try:
            conn = self._connect()
            cursor = conn.cursor()
            query = f"UPDATE Tasks SET Checked={checked_task} WHERE Id = '{id}'"
            cursor.execute(query)
            conn.commit()
        except Exception as e:
            print(f"Error change status of task: {e}")
            return False 
        finally:
            conn.close()    
    def sort_tasks(self,s):
        try:
            conn = self._connect()
            cursor = conn.cursor()
            tasks =[]
            query = ""
            if s:
                query = f"SELECT * FROM Tasks ORDER BY CurrentDate DESC"
            else:
                query = f"SELECT * FROM Tasks ORDER BY CurrentDate"
            cursor.execute(query)
            for row in cursor.fetchall():
                task = {
                    'id':row[0],
                    'taskTitle':row[1],
                    'description':row[2],
                    'checked':row[3],
                    'currentDate':row[4]
                }
                tasks.append(task)
            return tasks
        except Exception as e:
            print(f"Error sort tasks: {e}")
            return None
        finally:
            conn.close()        
    
    def search_task(self,value):
        try:
            conn = self._connect()
            cursor = conn.cursor()
            tasks = []
            query = f"SELECT * FROM Tasks WHERE (Title like '%{value}%') or (Description like '%{value}%')"
            cursor.execute(query)
            for row in cursor.fetchall():
                task = {
                    'id':row[0],
                    'taskTitle':row[1],
                    'description':row[2],
                    'checked':row[3],
                    'currentDate':row[4]
                }
                tasks.append(task)
            return tasks
        except Exception as e:
            print(f"Error searching: {e}")
            return None
        finally:
            conn.close()
    
db = DataBase()
