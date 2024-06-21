from flask import Flask, render_template, request
from baza import create_app, db
from banka import Banka
from kredit import Kredit

app = create_app()

# Rute
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)