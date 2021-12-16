import sqlalchemy
from datetime import datetime
from werkzeug.security import generate_password_hash
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:admin@localhost/demo"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



class User(db.Model):
    __tablename__ = 'usuario'
    #__table_args__ = {"schema": "rafael"}
    id_usuario = db.Column(db.Integer, primary_key=True, index=True)
    nome = db.Column(db.String(64), index=True)
    cargo = db.Column(db.String(40), index=True)
    orgao = db.Column(db.String(40), index=True)
    matricula = db.Column(db.String(40), index=True)
    email = db.Column(db.String(40), index=True)
    data_hora_cadastro = db.Column(db.String(40), index=True)
    login = db.Column(db.String(40), unique=True, index=True)
    senha = db.Column(db.String(200), index=True)
    perfil = db.Column(db.String(40), index=True)


    def __init__(self, nome, cargo, orgao, matricula, email, data_hora_cadastro, login, senha, perfil) -> None:
        self.nome = nome
        self.cargo = cargo
        self.orgao = orgao
        self.matricula = matricula
        self.email = email
        self.data_hora_cadastro = data_hora_cadastro
        self.login = login
        self.senha = generate_password_hash(senha)
        self.perfil = perfil


    def __repr__(self) -> str:
        return f"{self.nome} possui {self.cargo}"
        