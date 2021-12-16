from postgresql_test import db, User
from datetime import datetime

now = datetime.now()

db.create_all()

rafael = User('Rafael', 'Desenvolvedor', 'Unifor', '54239711', 'rafael@teste.com', now.strftime("%d/%m/%Y %H:%M:%S"), 'rafaellogin', 'rafaelpassword', 'Perfil')

pablo = User('Pablo', 'Desenvolvedor', 'Unifor', '35489521', 'pablo@teste.com', now.strftime("%d/%m/%Y %H:%M:%S"), 'pablologin', 'pablopassword', 'Perfil')

db.session.add_all([pablo])
db.session.commit()

print(pablo)