# -*- coding: utf-8 -*-

from app import app, db
from app.models import User, Book, Log, Role

app_ctx = app.app_context()
app_ctx.push()
db.create_all()
Role.insert_roles()

admin = User(name=u'root', email='root@gmail.com', password='password', major='administrator',
			 headline=u"Administrator", about_me=u"Bibliotecario.")
user1 = User(name=u'Marcelo', email='teste@gmail.com', password='123456',
			 major='Engenharia de Computação', headline=u"Estudante")


#book1 = Book(title=u"Python", subtitle=u"Python Fluente: Programação Clara, Concisa e Eficaz ", author=u"Luciano Ramalho", isbn='9787115373991',
#			 tags_string=u"Computação, Programação, Engenharia", image='https://images-na.ssl-images-amazon.com/images/I/51Ov4P3XiEL._SX357_BO1,204,203,200_.jpg',
#			 summary=u'A simplicidade de Python permite que você se torne produtivo rapidamente, porém isso muitas vezes significa que você não estará usando tudo que ela tem a oferecer. Com este guia prático, você aprenderá a escrever um código Python eficiente e idiomático aproveitando seus melhores recursos – alguns deles, pouco conhecidos. O autor Luciano Ramalho apresenta os recursos essenciais da linguagem e bibliotecas de Python mostrando como você pode tornar o seu código mais conciso, mais rápido e mais legível ao mesmo tempo.'
#)

db.session.add_all([admin, user1])
db.session.commit()

app_ctx.pop()