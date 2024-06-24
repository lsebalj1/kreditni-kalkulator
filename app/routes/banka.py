from flask import Flask, render_template, request
from app.database.banka import Banka

def _banke():
    banke = Banka.query.all()
    return render_template('banke.html', banke=banke)