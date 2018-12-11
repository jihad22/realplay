from flask import Blueprint 

bp = Blueprint('player', __name__)

#selnjutnya import isi dari direktori auth ini
from app.player import player