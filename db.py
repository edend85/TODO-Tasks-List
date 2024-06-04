import pyodbc
import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()
class DataBase:
    def __init__(self):
        self.connection_string = {
            'dbname': os.getenv('DB_NAME'),
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASS'),
            'host': os.getenv('DB_HOST'),
            'port': os.getenv('DB_PORT')
            }
        self.create_table()

    def _connect(self):
        try:
            return psycopg2.connect(**self.connection_string)
        except Exception as e:
            print(f"Error connecting to database: {e}")
            raise
    
    def create_table(self):
        try:
            conn = self._connect()
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS "Tasks" (
                    "id" varchar(50) PRIMARY KEY NOT NULL,
                    "title" VARCHAR(255) NOT NULL,
                    "description" TEXT NOT NULL,
                    "checked" BOOLEAN NOT NULL DEFAULT FALSE,
                    "current_date" DATE NOT NULL
                )
            """)
            conn.commit()
        except Exception as e:
            print(f"Error creating table: {e}")
            raise
        finally:
            conn.close()

    def all_tasks(self):
        try:
            conn = self._connect()
            print(conn)
            cursor = conn.cursor()
            tasks = []
            query =  "SELECT * FROM \"Tasks\""
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
            query = f"select * from \"Tasks\" where \"id\" = '{task_Id}'"
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
            query = f"INSERT INTO \"Tasks\"(\"id\",\"title\", \"description\", \"checked\", \"current_date\")VALUES('{id_task}','{title_task}','{desc_task}',{checked_task},'{date_task}')"
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
            query = f"DELETE FROM \"Tasks\" WHERE \"id\" = '{id_task}'"
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
            query = f"UPDATE \"Tasks\" SET \"title\"='{body['title']}',\"description\"='{body['description']}' WHERE \"id\" = '{id}'"
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
            query = f"UPDATE \"Tasks\" SET \"checked\"={checked_task} WHERE \"id\" = '{id}'"
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
                query = f"SELECT * FROM \"Tasks\" ORDER BY \"current_date\" DESC"
            else:
                query = f"SELECT * FROM \"Tasks\" ORDER BY \"current_date\" "
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
            query = f"SELECT * FROM \"Tasks\" WHERE (\"title\" like '%{value}%') or (\"description\" like '%{value}%')"
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
#print(db.all_tasks())
#print(db.get_task("bb57160d011445e2b02c41e4"))
#print(db.add_task("bb57160d011445e2b02c41e2","review the budget","one of my tasks in the morning is to make lunches for everyone in the family Verb I have been tasked by the host with bringing the pies for Thanksgiving this year.",False,"08/08/2024"))
#print(db.delete_task("bb57160d011445e2b02c41e2"))
#db.checked_task("bb57160d011445e2b02c41e4",True)
#print(db.update_task("bb57160d011445e2b02c41e5",body={"title":"Team Meeting","description":"Attend the weekly team meeting to discuss project updates"}))
#print(db.search_task("to"))
print(db.sort_tasks(False))
#print(db.sort_tasks(True))
