import os

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'kamu-tidak-akan-pernah-bisa_masuk_selama_key_ini_tidak_dirubah'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://root:@localhost/realplay'
    SQLALCHEMY_TRACK_MODIFICATIONS = False