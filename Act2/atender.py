import numpy as np
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Datos iniciales de clientes
nombres_iniciales = [
    "Ana García",
    "Carlos López",
    "María Rodríguez",
    "Luis Martínez",
    "Sofía Hernández"
]

# Crear array estructurado de NumPy para la cola
dtype = [('turno', int), ('nombre', 'U50')]
cola = np.empty(len(nombres_iniciales), dtype=dtype)

# Asignar turnos y nombres usando NumPy
cola['turno'] = np.arange(1, len(nombres_iniciales) + 1)
cola['nombre'] = nombres_iniciales

@app.route('/')
def index():
    # Convertir array de NumPy a lista de diccionarios para la plantilla
    clientes = [{'turno': row['turno'], 'nombre': row['nombre']} for row in cola]
    return render_template('index.html', clientes=clientes)

@app.route('/atender')
def atender_cliente():
    global cola
    if len(cola) > 0:
        # Eliminar primer elemento usando NumPy
        cola = np.delete(cola, 0)
    return redirect(url_for('index'))

# Nueva ruta para agregar clientes
@app.route('/agregar', methods=['POST'])
def agregar_cliente():
    global cola
    nombre = request.form['nombre']
    
    # Determinar el próximo turno
    if len(cola) > 0:
        proximo_turno = cola['turno'][-1] + 1
    else:
        proximo_turno = 1
    
    # Crear nuevo cliente y agregar a la cola
    nuevo_cliente = np.array([(proximo_turno, nombre)], dtype=dtype)
    cola = np.concatenate((cola, nuevo_cliente))
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)