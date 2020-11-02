from . import *
import sys
from app import form ,productsform ,foraboutus
from app.products import Products
from app.special import Special
from app.edit import Edit


@app.route("/", methods=['GET','POST'])
def homePAge():
    # query_form = form.QueryForm()
    # # if query_form.form.validate():
    # products = Products.query.all()
    admin = "546147282"
    key = flask.session.get('admin')
    if str(key) == admin :
        admin = str(key)
    else:
        admin = ''
    products =Products.query.filter(Products.kind == 1)
    hotcoffe = Products.query.filter(Products.kind == 2)
    juice = Products.query.filter(Products.kind == 3)
    special = Special.query.all()
    aboutq = Edit.query.all()
    if request.method == 'GET':
        return render_template('index.html' ,admin = admin ,products =products ,hotcoffe=hotcoffe ,juice=juice ,special =special,about=aboutq)


@app.route("/add_product", methods=['GET','POST'])
def add_product():
    Form = productsform.AddProduct()
    db.create_all()
    db.session.commit()
    Form.validate()
    if flask.request.method == "POST":
        if Form.name.data != None and Form.price.data != None and Form.image.data != None:
            product = Products(Form.name.data, Form.price.data, Form.des.data, Form.image.data ,Form.kind.data)
            try:
                db.session.add(product)
                db.session.commit()
            except Exception as e:
                print(str(e.args)[120:][:-5])
                return flask.render_template("addproduct.html", form=Form, e=str(e.args)[120:][:-5])
            except:
                print("Unexpected error:", sys.exc_info()[0])
                return flask.render_template("addproduct.html", form=Form, e=sys.exc_info()[0])
            return flask.redirect('/')
    return flask.render_template("addproduct.html", form=Form)


@app.route("/add_specialProduct", methods=['GET','POST'])
def add_specialProduct():
    Form = productsform.AddProduct()
    db.create_all()
    db.session.commit()
    Form.validate()
    if flask.request.method == "POST":
        if Form.name.data != None and Form.price.data != None and Form.image.data != None:
            product = Special(Form.name.data, Form.price.data, Form.des.data, Form.image.data ,Form.kind.data)
            try:

                db.session.add(product)
                db.session.commit()
            except Exception as e:
                print(str(e.args)[120:][:-5])
                return flask.render_template("addproduct.html", form=Form, e=str(e.args)[120:][:-5])
            except:
                print("Unexpected error:", sys.exc_info()[0])
                return flask.render_template("addproduct.html", form=Form, e=sys.exc_info()[0])
            return flask.redirect(url_for('homePAge'))
    return flask.render_template("addproduct.html", form=Form)

@app.route("/Editaboutus" ,methods=['GET', 'POST'])
def Editaboutus():
    Form= foraboutus.Edit()
    db.create_all()
    db.session.commit()
    Form.validate()
    if flask.request.method == "POST":
        if Form.description.data != None and Form.description2.data != None:
            edit = Edit(Form.description.data, Form.description2.data,Form.description3.data)
            try:
                db.session.query(Edit).delete()
                db.session.add(edit)
                db.session.commit()
            except Exception as e:
                print(str(e.args)[120:][:-5])
                return flask.render_template("Edit-about.html", form=Form, e=str(e.args)[120:][:-5])
            except:
                print("Unexpected error:", sys.exc_info()[0])
                return flask.render_template("Edit-about.html", form=Form, e=sys.exc_info()[0])
            return flask.redirect('/')
    return flask.render_template("Edit-about.html", form=Form)