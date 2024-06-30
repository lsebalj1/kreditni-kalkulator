from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.database.banka import Banka
from app.database.kredit import Kredit
from app.setup import db
from .. import setup
import datetime

kalkulator_bp = Blueprint('kalkulator', __name__)

@kalkulator_bp.route('/kalkulator', methods=['GET', 'POST'])
def kalkulator():
    db = setup.db
    bank_list = Banka.query.all()

    if request.method == 'POST':
        vrsta = request.form.get('vrsta')
        iznos = float(request.form.get('iznos'))
        kamatna_stopa = float(request.form.get('kamatna_stopa'))
        banka_id = int(request.form.get('banka_id'))
        banka = Banka.query.get(banka_id)
        datum_pocetka = datetime.datetime.now()
        trajanje = 240
        mjesecna_rata = 360
        status = "aktivan"
        duznik = "Gabrijel"

        if banka:
            utjecaj_stopa = banka.utjecaj_na_stopu
            adjusted_kamatna_stopa = kamatna_stopa + utjecaj_stopa

            kredit = Kredit(vrsta=vrsta, iznos=iznos, kamatna_stopa=adjusted_kamatna_stopa,
                            datum_pocetka=datum_pocetka, trajanje=trajanje, mjesecna_rata=mjesecna_rata,
                            status=status, duznik=duznik, banka_id=banka_id)
            trosak = kredit.izracunaj_trosak()

            if trosak is not None:
                db.session.add(kredit)
                db.session.commit()
                return render_template('kalkulator.html', trosak=trosak, banke=bank_list)
            else:
                error_message = 'Nije moguće izračunati trošak kredita. Provjerite unos.'
                return render_template('kalkulator.html', error_message=error_message, banke=bank_list)
        else:
            return render_template('kalkulator.html', error_message='Banka not found.', banke=bank_list)

    if request.method == 'GET':
        return render_template('kalkulator.html', banke=bank_list)

    return render_template('kalkulator.html', banke=bank_list)

@kalkulator_bp.route('/krediti', methods=['GET'])
def list_krediti():
    db = setup.db
    krediti = Kredit.query.all()
    return render_template('krediti.html', krediti=krediti)

@kalkulator_bp.route('/krediti/<int:id>', methods=['GET'])
def view_kredit(id):
    db = setup.db
    kredit = Kredit.query.get_or_404(id)
    return render_template('kredit.html', kredit=kredit)

@kalkulator_bp.route('/krediti/<int:id>/edit', methods=['GET', 'POST'])
def edit_kredit(id):
    db = setup.db
    kredit = Kredit.query.get_or_404(id)

    if request.method == 'POST':
        kredit.vrsta = request.form.get('vrsta')
        kredit.iznos = float(request.form.get('iznos'))
        kredit.kamatna_stopa = float(request.form.get('kamatna_stopa'))
        kredit.trajanje = int(request.form.get('trajanje'))
        kredit.mjesecna_rata = float(request.form.get('mjesecna_rata'))
        kredit.status = request.form.get('status')
        kredit.duznik = request.form.get('duznik')
        kredit.banka_id = int(request.form.get('banka_id'))

        try:
            db.session.commit()
            flash('Kredit uspjesno azuriran!', 'success')
            return redirect(url_for('kalkulator.view_kredit', id=kredit.id))
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating kredit: {str(e)}', 'danger')

    bank_list = Banka.query.all()
    return render_template('edit_kredit.html', kredit=kredit, banke=bank_list)

@kalkulator_bp.route('/krediti/<int:id>/delete', methods=['POST'])
def delete_kredit(id):
    db = setup.db
    kredit = Kredit.query.get_or_404(id)

    try:
        db.session.delete(kredit)
        db.session.commit()
        flash('Kredit deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting kredit: {str(e)}', 'danger')

    return redirect(url_for('kalkulator.list_krediti'))
