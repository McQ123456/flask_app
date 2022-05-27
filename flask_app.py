from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('signup.html')
    
@app.route('/create')
def create():
    con = sqlite3.connect('login.db')
    cur = con.cursor()
    cur.execute("""CREATE TABLE user(
                   username VARCHAR(20) NOT NULL PRIMARY KEY,
                   password VARCHAR(20) NOT NULL)
                """)
    return 'table created'

@app.route('/signup', method['post'])
def signup():
    con = sqlite3.connect

@app.route('/signup', methods=['post'])
def signup():
    con = sqlite3.connect('login.db')
    cur = con.cursor()
    cur.execute("INSERT INTO user(username,password) VALUES (?,?)",
                   (request.form['un'], request.form['pw']))


@app.route('/create')
def create():
    con = sqlite3.connect('login.db')
    cur = con.cursor()
    cur.execute("""CREATE TABLE user(
                   username VARCHAR(20) NOT NULL PRIMARY KEY,
                   password VARCHAR(20) NOT NULL)
                """)
    return 'table created'

@app.route('/insert')
def insert():
    con = sqlite3.connect('login.db')
    cur = con.cursor()
    cur.execute("""INSERT INTO user(username, password)
                    VALUES("bob","123")
                """)
    con.commit()
    return 'insert!'

@app.route('/select')
def select():
    con = sqlite3.connect('login.db')
    cur = con.cursor()
    cur.execute("select * FROM user")
    rows = cur.fetcha11()
    return str(rows)

