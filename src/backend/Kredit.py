class Kredit:
    def __init__(self, id, vrsta, kamatna_stopa, iznos):
        self.id = id
        self.vrsta = vrsta
        self.kamatna_stopa = kamatna_stopa
        self.iznos = iznos

    def __str__(self):
        return (f"Kredit(ID: {self.id}, Vrsta: {self.vrsta}, Kamatna stopa: {self.kamatna_stopa}%, "
                f"Iznos: {self.iznos})")
