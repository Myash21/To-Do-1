from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

@app.route('/', methods=["GET"])
def hello():
    return render_template("index.html")

@app.route('/add', methods = ['POST'])
def add():
    pass

if __name__ == "__main__":
    with app.app_context():  # Push the application context
        db.create_all()       # Create tables in the database
    app.run(debug=True)
