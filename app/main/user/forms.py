# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, DataRequired, URL
from flask_pagedown.fields import PageDownField
from flask_wtf.file import FileField, FileAllowed
from app import avatars


class EditProfileForm(FlaskForm):
    name = StringField(u'Nome', validators=[DataRequired(), Length(1, 64, message=u"")])
    major = StringField(u'Posição', validators=[Length(0, 128, message=u"")])
    headline = StringField(u'Apresente-se em uma frase', validators=[Length(0, 32, message=u"")])
    about_me = PageDownField(u"Sobre min")
    submit = SubmitField(u"Salvar alterações")


class AvatarEditForm(FlaskForm):
    avatar_url = StringField('', validators=[Length(1, 100, message=u""), URL(message=u"")])
    submit = SubmitField(u"Save")


class AvatarUploadForm(FlaskForm):
    avatar = FileField('', validators=[FileAllowed(avatars, message=u"Upload uma imagem sua!")])
