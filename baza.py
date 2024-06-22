from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kreditni_kalkulator.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app

'''

import sqlite3

def connect_to_database(db_file):
    conn = sqlite3.connect(db_file)
    return conn

def query_and_print(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()

def main():
    db_file = 'banka_krediti.db'
    conn = connect_to_database(db_file)

    query = "SELECT * FROM Kredit;"
    print("Executing query:", query)
    query_and_print(conn, query)

    conn.close()

if __name__ == "__main__":
    main()
'''
