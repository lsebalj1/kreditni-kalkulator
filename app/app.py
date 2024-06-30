from flask import Flask
from app.routes import index, kalkulator
from app.database import create_tables
from app.routes.banka import banke_bp  
from . import setup

############# DEFINING APP AND DB ###############
app = setup._create_app()
db = setup.db

############# REGISTER BLUEPRINTS ####################
app.register_blueprint(banke_bp)
app.register_blueprint(kalkulator_bp)

############# ROUTES ####################
@app.route('/')
def _route_index():
    index_view = index._index()
    return index_view

@app.route('/kalkulator', methods=['GET', 'POST'])
def _route_kalkulator():
    kalkulator_route = kalkulator._kalkulator()
    return kalkulator_route

@app.route('/krediti', methods=['GET'])
def list_krediti():
    return kalkulator.list_krediti()

@app.route('/krediti/<int:id>', methods=['GET'])
def view_kredit(id):
    return kalkulator.view_kredit(id)

@app.route('/krediti/<int:id>/edit', methods=['GET', 'POST'])
def edit_kredit(id):
    return kalkulator.edit_kredit(id)

@app.route('/krediti/<int:id>/delete', methods=['POST'])
def delete_kredit(id):
    return kalkulator.delete_kredit(id)

############# RUN ####################
if __name__ == '__main__':
    print("Running")
    create_tables._create_tables(app, db)
    app.run(debug=True)
