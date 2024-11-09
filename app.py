from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

@app.route('/', methods=["GET"])
def hello():
    todo_list = Todo.query.all()
    return render_template("index.html", todo_list = todo_list)

if __name__ == "__main__":
    with app.app_context():  # Push the application context
        db.create_all()       # Create tables in the database
        new_todo = Todo(title = 'todo 1', complete = False)
        db.session.add(new_todo)
        db.session.commit()
    app.run(debug=True)
