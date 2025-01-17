import sqlite3
import random
from flask import Flask, session, render_template, request, g, Blueprint

app = Flask(__name__)
app.secret_key = "Mburu_Rionge"

@app.route("/")
def index():
    data = get_db()
    return str(data)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('grocery_list.db')
        cursor = db.cursor()
        cursor.execute("select * from groceries")
        all_data = cursor.fetchall()
        all_data = [str(val[0]) for val in all_data]
    return all_data

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run()