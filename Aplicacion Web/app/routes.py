from app import app
from flask import render_template
from app.forms import Problema

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

def honorarios(honorario):
    iva=0.16
    R_IVA=0.106666
    R_ISR=0.10
    subtotal=honorario+(honorario*iva)
    neto=subtotal-(honorario*R_IVA)-(honorario*R_ISR)
    return neto

@app.route("/problema", methods=["GET", "POST"])
def problema():
    form=Problema()
    if form.validate_on_submit():
        msj="El calculo neto es: "+str(honorarios(form.honorario.data))
        return render_template("problemaRespuesta.html", form=form,msj=msj)
    return render_template("problema.html", form=form)
