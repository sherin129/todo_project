from flask import Flask,render_template,request,redirect,url_for,abort
app= Flask(__name__)
todos = [
        {'id':1,'task':'learn Flask'},
        {'id':2,'task':'build project'},
        {'id':3,'task':'deploy the app'},
        ]
next_id = 4

def find_todo(todo_id):
    for todo in todos:
        if todo['id']== todo_id:
            return todo
    abort(404)

@app.route('/')
def get_todos():
   
    return render_template('todos.html',todos=todos)

@app.route('/add',methods=['POST'])
def add_todo():
    global next_id
    task= request.form.get('task','').strip()
    if task:
        todos.append({'id': next_id,'task':task})
        next_id += 1
    return redirect(url_for('get_todos'))

@app.route('/edit/<int:todo_id>', methods=['GET','POST'])
def edit_todo(todo_id):
    todo = find_todo(todo_id)
    if request.method =='POST':
        task = request.form.get('task','').strip()
        if task:
            todo['task']=task
        return redirect(url_for('get_todos'))
    return render_template('edit.html',todo=todo)
@app.route('/delete/<int:todo_id>',methods=['POST'])
def delete_todo(todo_id):
    todo = find_todo(todo_id)
    todos.remove(todo)
    return redirect(url_for('get_todos'))

if __name__ =='__main__':
    app.run(debug=True)
    