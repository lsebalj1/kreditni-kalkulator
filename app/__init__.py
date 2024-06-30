# app/routes/__init__.py

from .routes.index import _index
from .routes.kalkulator import _kalkulator
from .routes.banka import _banke
from .database.banka import Banka
from .database.kredit import Kredit
from .database.create_tables import _create_tables
from .setup import _create_app

from flask import Blueprint


from .kalkulator import kalkulator_bp
from .banka import banke_bp

__all__ = ['kalkulator_bp', 'banke_bp']
