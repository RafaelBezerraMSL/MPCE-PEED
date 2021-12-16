from flask import render_template, redirect, request, sessions, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy.sql.operators import exists
from project_demo.forms import LoginForm, ProcForm
from project_demo.setup import app, db, table
from werkzeug.security import check_password_hash

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.query(table).filter_by(nome = form.username.data).first()
        print(user.nome)
        print(user.cargo)
        if user is not None:
            if check_password_hash(user.senha, form.password.data):
                #return f"{user.username} cpf is {user.cpf}"
                return redirect(url_for("procedimentos_ativos", username=user.nome, cargo=user.cargo))
    
    return render_template('login.html', form=form)

@app.route('/procedimentos_ativos')
def procedimentos_ativos():
    return render_template('current_procedures.html', username=request.args.get('username'), cpf=request.args.get('cargo'))

@app.route('/novo_procedimento')
def novo_procedimento():
    form = ProcForm()

    return render_template("novo_procedimento.html")

if __name__=="__main__":
    app.run(debug=True)