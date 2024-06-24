from flask import Flask, render_template, request
from app.database.banka import Banka
from app.database.kredit import Kredit


def _create_tables(app, db):
    with app.app_context():
        print("Stvaranje tablica")
        db.create_all()

        banka_data = [
            ('Erste', 'Jadranski trg 3A, 51000 Rijeka', '0800 7890', 0.5),
            ('OTP Banka', 'Domovinskog rata 61 Split', '0800 210 021', 0.7),
            ('PBZ', 'Radnička cesta 50, 10000 Zagreb', '01 636 0000', 0.6),
            ('HPB', 'Jurišićeva ulica 4,  Zagreb', '0800 472 472 ', 0.8),
            ('Addiko Bank', 'Slavonska avenija 6 , Zagreb', '01 6030 000', 0.9),
            ('Raiffeisen', 'Magazinska cesta 69, Zagreb', '01 / 4566-466', 0.4),
            ('IKB', 'Ernesta Miloša 1, Umag', '052 702 400', 0.3)
        ]

        banks = {}
        for data in banka_data:
            banka = Banka(
                naziv=data[0],
                adresa=data[1],
                broj_telefona=data[2],
                utjecaj_na_stopu=data[3]
            )
            db.session.add(banka)
            db.session.flush()  
            banks[data[0]] = banka.id  

        kredit_data = [
            ('Hipotekarni', 3.5, 200000.00, '2022-01-01', 240, 1200.00, 'aktivan', 'Ivan Horvat', 'Erste'),
            ('Auto', 5.0, 25000.00, '2023-03-01', 60, 500.00, 'aktivan', 'Ana Kovač', 'OTP Banka'),
            ('Studentski', 2.0, 15000.00, '2021-09-01', 36, 420.00, 'aktivan', 'Marko Marić', 'PBZ'),
            ('Hipotekarni', 4.0, 180000.00, '2020-06-01', 240, 1100.00, 'zatvoren', 'Petra Novak', 'HPB'),
            ('Auto', 5.5, 22000.00, '2022-11-01', 48, 480.00, 'aktivan', 'Luka Perić', 'Addiko Bank')
        ]

        for data in kredit_data:
            banka_name = data[8]
            if banka_name in banks:
                kredit = Kredit(
                    vrsta=data[0],
                    kamatna_stopa=data[1],
                    iznos=data[2],
                    #datum_pocetka=datetime.strptime(data[3], '%Y-%m-%d').date(),
                    trajanje=data[4],
                    mjesecna_rata=data[5],
                    status=data[6],
                    duznik=data[7],
                    banka_id=banks[banka_name]
                )
                db.session.add(kredit)
            else:
                print(f"Banka '{banka_name}' not found.")

        db.session.commit()
        print("Initial data inserted.")
