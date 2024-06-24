from flask import Flask, render_template, request
from app.database.banka import Banka

def _banke():
    try:
        bank_list = Banka.query.all()
        return render_template('banke.html', banke=bank_list)
    except Exception as ex:
        print("Exception occured in _banke", ex)
        return f"An error occurred when getting banks.,{ex} ", 500
