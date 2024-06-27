from flask import Blueprint, render_template, request, jsonify, send_file
from app.database.banka import Banka
from app.setup import db

banke_bp = Blueprint('banke', __name__)

@banke_bp.route('/banke', methods=['GET'])
def _banke():
    try:
        bank_list = Banka.query.all()
        return render_template('banke.html', banke=bank_list)
    except Exception as ex:
        print("Exception occurred in _banke", ex)
        return f"An error occurred when getting banks: {ex}", 500

@banke_bp.route('/api/banke/<int:id>', methods=['GET'])
def get_banka(id):
    try:
        banka = Banka.query.get_or_404(id)
        return jsonify(banka.to_dict())
    except Exception as ex:
        print("Exception occurred in get_banka", ex)
        return jsonify(error=str(ex)), 500

@banke_bp.route('/api/banke', methods=['POST'])
def create_banka():
    try:
        data = request.json
        new_banka = Banka(
            naziv=data['naziv'],
            adresa=data['adresa'],
            broj_telefona=data.get('broj_telefona'),
            utjecaj_na_stopu=data['utjecaj_na_stopu']
        )
        db.session.add(new_banka)
        db.session.commit()
        return jsonify(new_banka.to_dict()), 201
    except Exception as ex:
        print("Exception occurred in create_banka", ex)
        return jsonify(error=str(ex)), 500

@banke_bp.route('/api/banke/<int:id>', methods=['PUT'])
def update_banka(id):
    try:
        data = request.json
        banka = Banka.query.get_or_404(id)
        banka.naziv = data.get('naziv', banka.naziv)
        banka.adresa = data.get('adresa', banka.adresa)
        banka.broj_telefona = data.get('broj_telefona', banka.broj_telefona)
        banka.utjecaj_na_stopu = data.get('utjecaj_na_stopu', banka.utjecaj_na_stopu)
        db.session.commit()
        return jsonify(banka.to_dict())
    except Exception as ex:
        print("Exception occurred in update_banka", ex)
        return jsonify(error=str(ex)), 500

@banke_bp.route('/api/banke/<int:id>', methods=['DELETE'])
def delete_banka(id):
    try:
        banka = Banka.query.get_or_404(id)
        db.session.delete(banka)
        db.session.commit()
        return '', 204
    except Exception as ex:
        print("Exception occurred in delete_banka", ex)
        return jsonify(error=str(ex)), 500


