"""Flask web application for warehouse management"""
from flask import Flask, render_template, request, redirect, url_for, jsonify
from varasto import Varasto

app = Flask(__name__)

# In-memory storage for inventories
inventories = {}

@app.route('/')
def index():
    """Main dashboard showing all inventories"""
    return render_template('index.html', inventories=inventories)

@app.route('/inventory/create', methods=['POST'])
def create_inventory():
    """Create a new inventory"""
    name = request.form.get('name', '').strip()
    capacity = request.form.get('capacity', type=float, default=0)

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    if name in inventories:
        return jsonify({'error': 'Inventory already exists'}), 400

    if capacity <= 0:
        return jsonify({'error': 'Capacity must be positive'}), 400

    inventories[name] = Varasto(capacity)
    return redirect(url_for('index'))

@app.route('/inventory/<name>/edit', methods=['POST'])
def edit_inventory(name):
    """Edit an existing inventory name"""
    if name not in inventories:
        return jsonify({'error': 'Inventory not found'}), 404

    new_name = request.form.get('new_name', '').strip()
    if not new_name:
        return jsonify({'error': 'New name is required'}), 400

    if new_name != name and new_name in inventories:
        return jsonify({'error': 'An inventory with that name already exists'}), 400

    # Rename by moving the varasto to a new key
    if new_name != name:
        inventories[new_name] = inventories.pop(name)

    return redirect(url_for('index'))

@app.route('/inventory/<name>/delete', methods=['POST'])
def delete_inventory(name):
    """Delete an inventory"""
    if name in inventories:
        del inventories[name]
    return redirect(url_for('index'))

@app.route('/inventory/<name>/add', methods=['POST'])
def add_to_inventory(name):
    """Add items to an inventory"""
    if name not in inventories:
        return jsonify({'error': 'Inventory not found'}), 404

    amount = request.form.get('amount', type=float, default=0)

    if amount <= 0:
        return jsonify({'error': 'Amount must be positive'}), 400

    inventories[name].lisaa_varastoon(amount)
    return redirect(url_for('index'))

@app.route('/inventory/<name>/remove', methods=['POST'])
def remove_from_inventory(name):
    """Remove items from an inventory"""
    if name not in inventories:
        return jsonify({'error': 'Inventory not found'}), 404

    amount = request.form.get('amount', type=float, default=0)

    if amount <= 0:
        return jsonify({'error': 'Amount must be positive'}), 400

    inventories[name].ota_varastosta(amount)
    return redirect(url_for('index'))

@app.route('/api/inventories')
def get_inventories():
    """Get all inventories as JSON"""
    result = {}
    for name, varasto in inventories.items():
        result[name] = {
            'capacity': varasto.tilavuus,
            'balance': varasto.saldo,
            'available': varasto.paljonko_mahtuu()
        }
    return jsonify(result)

if __name__ == '__main__':
    # Add some example inventories
    inventories['Juice'] = Varasto(100.0, 50.0)
    inventories['Beer'] = Varasto(100.0, 20.2)
    inventories['Milk'] = Varasto(50.0, 10.0)

    app.run(debug=True, host='0.0.0.0', port=5000)
