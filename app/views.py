import os
from flask import request, render_template, redirect, url_for, flash
from app import app, db
from app.models import Repuestos, Factura, Marca
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static', 'images')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    print("Cargando la página de inicio...")
    return render_template('index.html')

@app.route('/repuestos')
def repuestos_list():
    repuestos = Repuestos.query.all()
    return render_template('repuestos_list.html', repuestos=repuestos)

@app.route('/factura/<int:id>')
def factura_detail(id):
    factura = Factura.query.get(id)
    return render_template('factura.html', factura=factura)

# Ruta para agregar un nuevo repuesto
@app.route('/repuesto/add', methods=['GET', 'POST'])
def add_repuesto():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        cantidad = request.form.get('cantidad')
        precio = request.form.get('precio')
        file = request.files.get('foto')
        marca_id = request.form.get('marca_id')

        if not nombre or not cantidad or not precio or not marca_id:
            flash('Todos los campos son requeridos.')
            return redirect(url_for('add_repuesto'))

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            foto = filename
        else:
            foto = None

        nuevo_repuesto = Repuestos(
            nombre=nombre,
            cantidad=int(cantidad),
            precio=int(precio),
            foto=foto,
            marca_id=int(marca_id)
        )
        db.session.add(nuevo_repuesto)
        db.session.commit()
        flash('Repuesto agregado exitosamente.')
        return redirect(url_for('repuestos_list'))

    marcas = Marca.query.all()
    return render_template('add_repuesto.html', marcas=marcas)

# Ruta para editar un repuesto existente
@app.route('/repuesto/edit/<int:id>', methods=['GET', 'POST'])
def edit_repuesto(id):
    repuesto = Repuestos.query.get(id)
    if not repuesto:
        flash('Repuesto no encontrado.')
        return redirect(url_for('repuestos_list'))

    if request.method == 'POST':
        repuesto.nombre = request.form.get('nombre')
        repuesto.cantidad = request.form.get('cantidad')
        repuesto.precio = request.form.get('precio')
        file = request.files.get('foto')
        repuesto.marca_id = request.form.get('marca_id')

        if not repuesto.nombre or not repuesto.cantidad or not repuesto.precio or not repuesto.marca_id:
            flash('Todos los campos son requeridos.')
            return redirect(url_for('edit_repuesto', id=id))

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            repuesto.foto = filename

        db.session.commit()
        flash('Repuesto actualizado exitosamente.')
        return redirect(url_for('repuestos_list'))

    marcas = Marca.query.all()
    return render_template('edit_repuesto.html', repuesto=repuesto, marcas=marcas)

# Ruta para eliminar un repuesto
@app.route('/repuesto/delete/<int:id>', methods=['POST'])
def delete_repuesto(id):
    repuesto = Repuestos.query.get(id)
    if not repuesto:
        flash('Repuesto no encontrado.')
        return redirect(url_for('repuestos_list'))

    db.session.delete(repuesto)
    db.session.commit()
    flash('Repuesto eliminado exitosamente.')
    return redirect(url_for('repuestos_list'))
