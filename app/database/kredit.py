from app.setup import db
from datetime import date

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
    banka_id = db.Column(db.Integer, db.ForeignKey('banka.id'), nullable=False)

    def __repr__(self):
        return f'<Kredit {self.vrsta}>'

    def izracunaj_trosak(self):
        monthly_rate = self.kamatna_stopa / 100 / 12 if self.kamatna_stopa is not None else 0
        total_payments = self.trajanje if self.trajanje is not None else 0

        if monthly_rate > 0 and total_payments > 0:
            mjesecna_rata = (self.iznos * monthly_rate) / (1 - (1 + monthly_rate) ** -total_payments)
        elif total_payments > 0:
            mjesecna_rata = self.iznos / total_payments
        else:
            mjesecna_rata = 0

        total_cost = mjesecna_rata * total_payments
        return total_cost
    