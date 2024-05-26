from flask import Flask, render_template,request,url_for,redirect
from db import DataBase
import datetime
import uuid

app = Flask(__name__, template_folder="templates")
tasks = DataBase()

@app.route("/")
def index():
    sort = request.args.get('sorted')
    if sort:
        return render_template("index.html",tasks = tasks.sort_tasks(sort),sorted = not sort)
    return render_template("index.html",tasks = tasks.all_tasks())


@app.route("/add",methods=["POST"])
def add():
    id_task = str(uuid.uuid4().hex)[:24]
    current_datetime = datetime.datetime.utcnow()
    current_datetime_str = current_datetime.strftime("%Y%m%d")
    tasktitle = request.form['taskTitle']
    description = request.form['description']
    tasks.add_task(id_task,tasktitle,description,0,current_datetime_str)
    return redirect(url_for("index"))

@app.route("/edit/<string:id>",methods=["GET","POST"])
def edit(id):
    task = tasks.get_task(id)
    print(task)
    return render_template("edit.html",task=task)
        
    
@app.route("/editTask/<string:id>",methods=["POST"])
def editTask(id):
    tasktitle = request.form['taskTitle']
    description = request.form['description']
    tasks.update_task(id,body={'Title':tasktitle,'Description':description})
    return redirect(url_for("index"))

@app.route("/status/<string:id>")
def status(id):
    task = tasks.get_task(id)
    match task['checked']:
        case 0:
             tasks.checked_task(id,1)
        case 1:
            tasks.checked_task(id,0)
    return redirect(url_for("index"))

@app.route("/delete/<string:id>")
def delete(id):
    tasks.delete_task(id)
    return redirect(url_for("index"))

@app.route("/sort/<string:s>")
def sort(s):
        if s == 'DESC':
            return render_template("index.html",tasks = tasks.sort_tasks(False),sorted = False)
        else:
            return render_template("index.html",tasks = tasks.sort_tasks(True),sorted = True)

@app.route("/search",methods=["POST"])
def search():
    search_value = request.form['search']
    search_results = tasks.search_task(search_value)
    return render_template("index.html",tasks=search_results)


if __name__ == '__main__':
    app.run(debug=True)