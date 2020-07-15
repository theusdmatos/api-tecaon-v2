# -*- coding:utf-8 -*-
from app import db
from app.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms import ValidationError
from wtforms.validators import Email, Length, DataRequired, EqualTo


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message=u"Por favor entre com seu email"), Length(1, 64), Email(message=u"E-mail incorreto")])
    password = PasswordField(u'Senha', validators=[DataRequired(message=u"Por favor entre com sua senha!")])
    remember_me = BooleanField(u"Manter conectado", default=True)
    submit = SubmitField(u'Entrar')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message=u"Por favor entre com seu email!"), Length(1, 64), Email(message=u"E-mail incorreto")])
    name = StringField(u'Registro acadêmico (RA)', validators=[DataRequired(message=u"Por favor entre com seu RA"), Length(4, 20, message="Digite um nome de usuário entre 4-20 caracteres!")])
    password = PasswordField(u'Senha', validators=[DataRequired(message=u"Por favor entre com uma senha!"), Length(6, 32, message="Digite uma senha entre 6-32 caracteres!")])
    password2 = PasswordField(u'Confirmar Senha', validators=[DataRequired(message=u"Por favor entre confirme sua senha!"), EqualTo('password', message=u'As senhas não coincidem!')])
    submit = SubmitField(u'Registrar')

    def validate_email(self, filed):
        if User.query.filter(db.func.lower(User.email) == db.func.lower(filed.data)).first():
            raise ValidationError(u'O email já foi registrado!')

