from flask import Flask, render_template, request
from baza import create_app, db
from banka import Banka
from kredit import Kredit

app = create_app()

# Rute
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/kalkulator', methods=['GET', 'POST'])
def kalkulator():
    if request.method == 'POST':
        vrsta = request.form.get('vrsta')
        iznos = float(request.form.get('iznos'))
        kamatna_stopa = float(request.form.get('kamatna_stopa'))
        banka_id = int(request.form.get('banka_id'))  

        banka = Banka.query.get(banka_id)

        if banka:
            utjecaj_stopa = banka.utjecaj_na_stopu
            adjusted_kamatna_stopa = kamatna_stopa + utjecaj_stopa

            kredit = Kredit(vrsta_kredita=vrsta, iznos=iznos, kamatna_stopa=adjusted_kamatna_stopa, banka_id=banka_id)
            trosak = kredit.izracunaj_trosak()

            return render_template('kalkulator.html', trosak=trosak)
        else:
            return render_template('kalkulator.html', error_message='Banka not found.')

    return render_template('kalkulator.html')

@app.route('/banke')
def banke():
    banke = Banka.query.all()
    return render_template('banke.html', banke=banke)

if __name__ == '__main__':
    app.run(debug=True)
