from baza import db

class Banka(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    naziv = db.Column(db.String(80), nullable=False)
    adresa = db.Column(db.String(200), nullable=False)
    broj_telefona = db.Column(db.String(20), nullable=True)  
    utjecaj_na_stopu = db.Column(db.Float, nullable=False)
    kredit_id = db.Column(db.Integer, db.ForeignKey('kredit.id'), nullable=True)  
    krediti = db.relationship('Kredit', backref='banka', lazy=True)

    def repr(self):
        return f'<Banka {self.naziv}>'
    