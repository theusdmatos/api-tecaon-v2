# -*- coding:utf-8 -*-
from app.models import Book
from flask_pagedown.fields import PageDownField
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms import ValidationError
from wtforms.validators import Length, DataRequired, Regexp


class EditBookForm(FlaskForm):
    isbn = StringField(u"ISBN",
                       validators=[DataRequired(),
                                   Regexp('[0-9]{13,13}', message=u"O ISBN deve ter 13 dígitos")])
    title = StringField(u"Titulo",
                        validators=[DataRequired(), Length(1, 128, message=u"")])
    origin_title = StringField(u"Titulo Original", validators=[Length(0, 128, message=u"")])
    #subtitle = StringField(u"Subtitulo", validators=[Length(0, 128, message=u"Maximum 128 characters!")])
    author = StringField(u"Autor", validators=[Length(0, 128, message=u"")])
    #translator = StringField(u"Tradutor",
    #                         validators=[Length(0, 64, message=u"Maximum 64 characters!")])
    publisher = StringField(u"Editora", validators=[Length(0, 64, message=u"")])
    image = StringField(u"Capa", validators=[Length(0, 128, message=u"")])
   # pubdate = StringField(u"Data de publicação", validators=[Length(0, 32, message=u"Maximum 32 characters!")])
    tags = StringField(u"Tags", validators=[Length(0, 128, message=u"")])
    pages = IntegerField(u"Nº de páginas")
   # price = StringField(u"Preço", validators=[Length(0, 64, message=u"Maximum 64 characters!")])
   # binding = StringField(u"Binding", validators=[Length(0, 16, message=u"Maximum 16 characters!")])
    numbers = IntegerField(u"Quantidade", validators=[DataRequired()])
    summary = PageDownField(u"Resumo")
    #catalog = PageDownField(u"Catálogo")
    submit = SubmitField(u"Salva e adiconar livro")


class AddBookForm(EditBookForm):
    def validate_isbn(self, filed):
        if Book.query.filter_by(isbn=filed.data).count():
            raise ValidationError(u'O mesmo ISBN já existe e não pode ser inserido. Verifique cuidadosamente se o livro está em estoque.')


class SearchForm(FlaskForm):
    search = StringField(validators=[DataRequired()])
    submit = SubmitField(u"Search")


