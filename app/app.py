from flask import Flask, render_template, request
from app.routes import index, kalkulator, banka
from app.database import create_tables
from . import setup





############# DEFINING APP AND DB ###############
app = setup._create_app()
db = setup.db




############# ROUTES ####################
@app.route('/')
def _route_index():
    index_view = index._index()
    return index_view

@app.route('/kalkulator', methods=['GET', 'POST'])
def _route_kalkulator():
    kalkulator_route = kalkulator._kalkulator()
    return kalkulator_route
    

@app.route('/banke')
def _route_banke():
    bank_route = banka._banke()
    return bank_route

############# RUN ####################
if __name__ == '__main__':
    print("Running")
    create_tables._create_tables(app,db)
    app.run(debug=True)
