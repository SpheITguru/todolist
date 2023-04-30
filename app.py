from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)
app.secret_key = 'mysecretkey'

# a list to store the todo items
todo_list = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    # check if the user is logged in
    if 'username' not in session:
        return redirect('/login')
    return render_template('dashboard.html', todo_list=todo_list)

@app.route('/add-item', methods=['POST'])
def add_item():
    # check if the user is logged in
    if 'username' not in session:
        return redirect('/login')
    todo_item = request.form['todo-item']
    todo_list.append(todo_item)
    return redirect('/dashboard')

@app.route('/delete-item/<int:index>')
def delete_item(index):
    # check if the user is logged in
    if 'username' not in session:
        return redirect('/login')
    todo_list.pop(index)
    return redirect('/dashboard')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # check if the username and password are valid
        if username == 'user' and password == 'pass':
            session['username'] = username
            return redirect('/dashboard')
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # add code to create a new user account in the database
        return redirect('/login')
    else:
        return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
