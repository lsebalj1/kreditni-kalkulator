from .. setup import db

class Banka(db.Model):
    __tablename__ = 'banka'
    id = db.Column(db.Integer, primary_key=True)
    naziv = db.Column(db.String(80), nullable=False)
    adresa = db.Column(db.String(200), nullable=False)
    broj_telefona = db.Column(db.String(20), nullable=True)  
    utjecaj_na_stopu = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Banka {self.naziv}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'naziv': self.naziv,
            'adresa': self.adresa,
            'broj_telefona': self.broj_telefona,
            'utjecaj_na_stopu': self.utjecaj_na_stopu
        }
