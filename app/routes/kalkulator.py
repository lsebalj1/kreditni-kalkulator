from flask import Flask, render_template, request
from app.database.banka import Banka
from app.database.kredit import Kredit
from .. import setup



def _kalkulator():
    
    db = setup.db   
    banke = Banka.query.all()

    if request.method == 'POST':
        vrsta = request.form.get('vrsta')
        iznos = float(request.form.get('iznos'))
        kamatna_stopa = float(request.form.get('kamatna_stopa'))
        banka_id = int(request.form.get('banka_id'))

        banka = Banka.query.get(banka_id)

        if banka:
            utjecaj_stopa = banka.utjecaj_na_stopu
            adjusted_kamatna_stopa = kamatna_stopa + utjecaj_stopa

            kredit = Kredit(vrsta=vrsta, iznos=iznos, kamatna_stopa=adjusted_kamatna_stopa, banka_id=banka_id)
            trosak = kredit.izracunaj_trosak()

            if trosak is not None:  
                db.session.add(kredit)
                db.session.commit()
                return render_template('kalkulator.html', trosak=trosak, banke=banke)
            else:
                error_message = 'Nije moguće izračunati trošak kredita. Provjerite unos.'
                return render_template('kalkulator.html', error_message=error_message, banke=banke)
        else:
            return render_template('kalkulator.html', error_message='Banka not found.', banke=banke)
        
    if request.method == 'GET':
       return render_template('kalkulator.html', banke=banke)