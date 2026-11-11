import sqlite3
from flask import Flask,render_template,request,redirect,url_for,abort
app = Flask(__name__)
DATABASE = 'todos.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn
@app.route('/')
def get_todos():
    try:
        conn = get_db()
        cursor =conn.cursor()
        cursor.execute("SELECT * FROM todos ORDER NY id ASC")
        todos = cursor.fetchall()
    except sqlite3.Error as e:
        app.logger.error(f"DB error in get_todos:{e}")
        abort(500)
    finally:
        if conn:
            conn.close()
    return render_template('todos.html', todos=todos)

#def find_todo(todo_id):

if __name__== '__main__':
    app.run(debug=True)