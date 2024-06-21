from baza import db

class Kredit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    banka_id = db.Column(db.Integer, db.ForeignKey('banka.id'), nullable=False)
    vrsta_kredita = db.Column(db.String(80), nullable=False)
    kamatna_stopa = db.Column(db.Float, nullable=False)
    iznos = db.Column(db.Float, nullable=False)

    def izracunaj_trosak(self):
        return self.iznos + (self.iznos * (self.kamatna_stopa / 100))