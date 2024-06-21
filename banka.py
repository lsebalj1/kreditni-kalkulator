from baza import db

class Banka(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    naziv = db.Column(db.String(80), nullable=False)
    adresa = db.Column(db.String(200), nullable=False)
    krediti = db.relationship('Kredit', backref='banka', lazy=True)
