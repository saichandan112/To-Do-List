# List.py
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# In-memory database
todos = []

@app.route('/')
def home():
    return render_template('Website.html')

@app.route('/add_todo', methods=['POST'])
def add_todo():
    todo = request.json
    todos.append(todo)
    return jsonify({'status': 'Todo added', 'data': todo}), 201

@app.route('/get_todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200

@app.route('/delete_todo', methods=['POST'])
def delete_todo():
    todo_id = request.json.get('id')
    global todos
    todos = [todo for todo in todos if todo['id'] != todo_id]
    return jsonify({'status': 'Todo deleted'}), 200

@app.route('/toggle_complete', methods=['POST'])
def toggle_complete():
    todo_id = request.json.get('id')
    for todo in todos:
        if todo['id'] == todo_id:
            todo['completed'] = not todo['completed']
            break
    return jsonify({'status': 'Todo updated'}), 200

if __name__ == '__main__':
    app.run(debug=True)
