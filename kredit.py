from baza import db

class Kredit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    banka_id = db.Column(db.Integer, db.ForeignKey('banka.id'), nullable=False)
    vrsta_kredita = db.Column(db.String(80), nullable=False)
    kamatna_stopa = db.Column(db.Float, nullable=False)
    iznos = db.Column(db.Float, nullable=False)

    def izracunaj_trosak(self):
        return self.iznos + (self.iznos * (self.kamatna_stopa / 100))

'''
testiranje baze
import mysql.connector
import mysql

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='banka_krediti'
)

cursor = conn.cursor()

def insert_kredit(vrsta, kamatna_stopa, iznos, datum_pocetka, trajanje, mjesecna_rata, status, duznik):
    sql = """
    INSERT INTO Kredit (vrsta, kamatna_stopa, iznos, datum_pocetka, trajanje, mjesecna_rata, status, duznik) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (vrsta, kamatna_stopa, iznos, datum_pocetka, trajanje, mjesecna_rata, status, duznik)
    cursor.execute(sql, values)
    conn.commit()
    print("Novi kredit je unesen.")

def fetch_all_banke():
    cursor.execute("SELECT * FROM Banka")
    result = cursor.fetchall()
    for row in result:
        print(row)

def update_kamatna_stopa(kredit_id, nova_kamatna_stopa):
    sql = "UPDATE Kredit SET kamatna_stopa = %s WHERE kredit_id = %s"
    values = (nova_kamatna_stopa, kredit_id)
    cursor.execute(sql, values)
    conn.commit()
    print("Kamatna stopa je ažurirana.")

def delete_kredit(kredit_id):
    sql = "DELETE FROM Kredit WHERE kredit_id = %s"
    values = (kredit_id,)
    cursor.execute(sql, values)
    conn.commit()
    print("Kredit je obrisan.")

insert_kredit('Osobni', 4.2, 50000.00, '2023-01-15', 48, 1050.00, 'aktivan', 'Maja Sever')
fetch_all_banke()
update_kamatna_stopa(1, 3.8)
#delete_kredit(2)


cursor.close()
conn.close()
'''