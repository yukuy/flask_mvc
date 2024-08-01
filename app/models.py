from app import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45))
    correo = db.Column(db.String(200))
    clave = db.Column(db.String(200))
    telefono = db.Column(db.BigInteger)
    facturas = db.relationship('Factura', backref='usuario', lazy=True)

class Repuestos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45))
    cantidad = db.Column(db.Integer)
    precio = db.Column(db.Integer)
    foto = db.Column(db.String(200))
    marca_id = db.Column(db.Integer, db.ForeignKey('marca.id'), nullable=False)
    marca = db.relationship('Marca', backref='repuestos', lazy=True)

class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45))
    modelo = db.Column(db.String(45))
    serie = db.Column(db.String(45))

class Factura(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date)
    total = db.Column(db.Integer)
    idUsuarios = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    detalles = db.relationship('DetalleFactura', backref='factura', lazy=True)

class DetalleFactura(db.Model):
    idfactura = db.Column(db.Integer, db.ForeignKey('factura.id'), primary_key=True)
    idrepuestos = db.Column(db.Integer, db.ForeignKey('repuesto.id'), primary_key=True)
    cantida = db.Column(db.Integer)
    precioU = db.Column(db.Integer)
    subtotal = db.Column(db.Integer)
    nombreR = db.Column(db.String(45))
