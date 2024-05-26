from flask import Flask, render_template,request,url_for,redirect,abort, jsonify,make_response
from db import DataBase
import datetime
import uuid

app = Flask(__name__, template_folder="templates")
tasks = DataBase()

def create_success_response(message, data=None):
    response_data = {
        'message': message
    }
    if data is not None:
        response_data['data'] = data
    return make_response(jsonify(response_data), 200)
# Custom error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    response = make_response(jsonify({"error": "Not found"}), 404)
    return response

# Custom error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    response = make_response(jsonify({"error": "Internal server"}), 500)
    return response

@app.route("/")
def index():
    try:
        if tasks is None:
            abort(404)
        sort = request.args.get('sorted')
        if sort:
            return render_template("index.html",tasks = tasks.sort_tasks(sort),sorted = not sort)
        else:
            return render_template("index.html",tasks = tasks.all_tasks())
    except Exception as e:
        print(f"Error in index route: {e}")
        abort(500)
    finally:
        create_success_response


@app.route("/add",methods=["POST"])
def add():
    try:
        id_task = str(uuid.uuid4().hex)[:24]
        current_datetime = datetime.datetime.utcnow()
        current_datetime_str = current_datetime.strftime("%Y%m%d")
        tasktitle = request.form['taskTitle']
        description = request.form['description']
        tasks.add_task(id_task,tasktitle,description,0,current_datetime_str)
        return redirect(url_for("index"))
    except:
        abort(500)
    finally:
        create_success_response


@app.route("/edit/<string:id>",methods=["GET","POST"])
def edit(id):
    try:
        task = tasks.get_task(id)
        return render_template("edit.html",task=task)
    except:
        abort(500)
    finally:
        create_success_response
        
    
@app.route("/editTask/<string:id>",methods=["POST"])
def editTask(id):
    tasktitle = request.form['taskTitle']
    description = request.form['description']
    tasks.update_task(id,body={'Title':tasktitle,'Description':description})
    return redirect(url_for("index"))

@app.route("/status/<string:id>")
def status(id):
    try:
        task = tasks.get_task(id)
        match task['checked']:
            case 0:
                tasks.checked_task(id,1)
            case 1:
                tasks.checked_task(id,0)
        return redirect(url_for("index"))
    except:
        abort(500)
    finally:
        create_success_response

@app.route("/delete/<string:id>")
def delete(id):
    try:
        tasks.delete_task(id)
        return redirect(url_for("index"))
    except:
        abort(500)
    finally:
        create_success_response

@app.route("/sort/<string:s>")
def sort(s):
        try:
            if s == 'DESC':
                return render_template("index.html",tasks = tasks.sort_tasks(False),sorted = False)
            else:
                return render_template("index.html",tasks = tasks.sort_tasks(True),sorted = True)
        except:
            abort(500)
        finally:
            create_success_response

@app.route("/search",methods=["POST"])
def search():
    try:
        search_value = request.form['search']
        search_results = tasks.search_task(search_value)
        return render_template("index.html",tasks=search_results)
    except:
        abort(500)
    finally:
        create_success_response


if __name__ == '__main__':
    app.run(port=int("3000"),debug=True)