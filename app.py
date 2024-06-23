from flask import Flask, render_template, request
from baza import create_app, db
from banka import Banka
from kredit import Kredit  

app = create_app()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/kalkulator', methods=['GET', 'POST'])
def kalkulator():
    banke = Banka.query.all() 

    if request.method == 'POST':
        vrsta_kredita = request.form.get('vrsta_kredita')
        iznos = float(request.form.get('iznos'))
        kamatna_stopa = float(request.form.get('kamatna_stopa'))
        banka_id = int(request.form.get('banka_id'))  

        banka = Banka.query.get(banka_id)

        if banka:
            utjecaj_stopa = banka.utjecaj_na_stopu
            adjusted_kamatna_stopa = kamatna_stopa + utjecaj_stopa

            kredit = Kredit(vrsta_kredita=vrsta_kredita, iznos=iznos, kamatna_stopa=adjusted_kamatna_stopa, banka_id=banka_id)
            trosak = kredit.izracunaj_trosak()

            db.session.add(kredit)
            db.session.commit()

            return render_template('kalkulator.html', trosak=trosak, banke=banke)
        else:
            return render_template('kalkulator.html', error_message='Banka not found.', banke=banke)

    return render_template('kalkulator.html', banke=banke)

@app.route('/banke')
def banke():
    banke = Banka.query.all()
    return render_template('banke.html', banke=banke)

if __name__ == '__main__':
    from banka import Banka
    from kredit import Kredit

    with app.app_context():
        kredit_data = [
            ('Hipotekarni', 3.5, 200000.00, '2022-01-01', 240, 1200.00, 'aktivan', 'Ivan Horvat'),
            ('Auto', 5.0, 25000.00, '2023-03-01', 60, 500.00, 'aktivan', 'Ana Kovač'),
            ('Studentski', 2.0, 15000.00, '2021-09-01', 36, 420.00, 'aktivan', 'Marko Marić'),
            ('Hipotekarni', 4.0, 180000.00, '2020-06-01', 240, 1100.00, 'zatvoren', 'Petra Novak'),
            ('Auto', 5.5, 22000.00, '2022-11-01', 48, 480.00, 'aktivan', 'Luka Perić')
        ]

        for data in kredit_data:
            kredit = Kredit(
                vrsta_kredita=data[0],
                kamatna_stopa=data[1],
                iznos=data[2],
                datum_pocetka=data[3],
                trajanje=data[4],
                mjesecna_rata=data[5],
                status=data[6],
                duznik=data[7]
            )
            db.session.add(kredit)

        banka_data = [
            ('Erste', 'Jadranski trg 3A, 51000 Rijeka', '0800 7890', 0.5),
            ('OTP Banka', 'Domovinskog rata 61 Split', '0800 210 021', 0.7), 
            ('PBZ', 'Radnička cesta 50, 10000 Zagreb', '01 636 0000', 0.6),
            ('HPB', 'Jurišićeva ulica 4,  Zagreb', '0800 472 472 ', 0.8),
            ('Addiko Bank', 'Slavonska avenija 6 , Zagreb', '01 6030 000', 0.9),
            ('Raiffeisen', 'Magazinska cesta 69, Zagreb', '01 / 4566-466', 0.4),
            ('IKB', 'Ernesta Miloša 1, Umag', '052 702 400', 0.3)
        ]

        for idx, data in enumerate(banka_data):
            banka = Banka(
                naziv=data[0],
                adresa=data[1],
                broj_telefona=data[2],
                utjecaj_na_stopu=data[3],
                kredit_id=idx + 1  
            )
            db.session.add(banka)

        db.session.commit()

    app.run(debug=True)