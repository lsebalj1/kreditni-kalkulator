from baza import get_connection
from Kredit import Kredit

class Banka:
    def __init__(self, id, naziv, adresa, krediti):
        self.id = id
        self.naziv = naziv
        self.adresa = adresa
        self.krediti = krediti 

    @classmethod
    def iz_baze(cls, db_path, banka_id):
        conn = get_connection(db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT banka_id, naziv, adresa FROM banka WHERE id = ?", (banka_id,))
        banka_row = cursor.fetchone()
        
        if banka_row is None:
            raise ValueError(f"Nema podataka za banku s ID-om: {banka_id}")

        id, naziv, adresa = banka_row

        cursor.execute("SELECT kredit_id, vrsta, kamatna_stopa, iznos FROM krediti WHERE banka_id = ?", (id,))
        krediti_rows = cursor.fetchall()

        krediti = []
        for kredit_id, vrsta, kamatna_stopa, iznos in krediti_rows:
            kredit = Kredit(kredit_id, vrsta, kamatna_stopa, iznos)
            krediti.append(kredit)

        conn.close()

        return cls(id, naziv, adresa, krediti)

    def __str__(self):
        krediti_str = "\n".join([str(kredit) for kredit in self.krediti])
        return (f"Banka(ID: {self.id}, Naziv: {self.naziv}, Adresa: {self.adresa})\nKrediti:\n{krediti_str}")
