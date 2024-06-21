
from baza import db

class Kredit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vrsta = db.Column(db.String(80), nullable=False)
    kamatna_stopa = db.Column(db.Float, nullable=False)
    iznos = db.Column(db.Float, nullable=False)
    datum_pocetka = db.Column(db.Date, nullable=False)
    trajanje = db.Column(db.Integer, nullable=False)
    mjesecna_rata = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    duznik = db.Column(db.String(100), nullable=False)

    def repr(self):
        return f'<Kredit {self.vrsta}>'
    
    