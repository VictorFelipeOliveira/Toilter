from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user
from app import app, db, lm

from app.models.tables import User
from app.models.forms import LoginForm

@lm.user_loader
def load_user(id):
	return User.query.filter_by(id=id).first()

@app.route("/index/<user>")
@app.route("/")
def index(user=None):
	return render_template('index.html', user=user)

@app.route("/about")
@app.route("/sobre")
def sobre():
	return "Sobre o Desenvolvedor"

@app.route("/login", methods=["GET","POST"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user and user.password == form.password.data:
			login_user(user)
			flash("User Logged.")
			return redirect(url_for("index"))
		else:
			flash("Login Invalid.")
	else:
		print (form.errors)
	return render_template('login.html', form=form)

@app.route("/logout", methods=["GET","POST"])
def logout():
	logout_user()
	flash("Logged out")
	return redirect(url_for("index"))


@app.route("/teste/<info>")
@app.route("/teste", defaults={"info": None})
def teste(info):
	# r.name = "Victor F."
	# r.name = "Victor F."
	# r = User.query.filter_by(username="felipe").first()
	# db.session.delete(r)
	# db.session.commit()
	# db.session.add(r)
	# #Cadastro de Registros
	# i = User("felipe" , "123", "felipe","felipe@uol.com")
	# db.session.add(i)
	# db.session.commit()
	return "Teste efetuado"