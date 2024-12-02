from flask import Flask, render_template, redirect, url_for, request, session
from tinydb import TinyDB, Query
from app.models import MenuItem  # Importe o modelo MenuItem

# Conexão com o banco de dados TinyDB
db = TinyDB('db.json')
menu_table = db.table('menu')

# Criando uma instância do Flask
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessário para usar sessões


# Rota de índice (página inicial com o cardápio)
@app.route('/')
def index():
    menu_items = MenuItem.get_all_items()
    return render_template('index.html', menu_items=menu_items)


# Rota para adicionar itens ao carrinho
@app.route('/add_to_cart/<int:item_id>/<int:quantity>')
def add_to_cart(item_id, quantity):
    item = next((x for x in menu_table.all() if x['id'] == item_id), None)
    if item:
        cart = session.get('cart', [])
        cart_item = next((x for x in cart if x['id'] == item_id), None)
        if cart_item:
            cart_item['quantity'] += quantity
        else:
            cart.append({'id': item_id, 'name': item['name'], 'price': item['price'], 'quantity': quantity,
                         'image': item['image']})
        session['cart'] = cart
    return redirect(url_for('cart'))


# Rota para o carrinho
@app.route('/cart')
def cart():
    cart = session.get('cart', [])
    total = sum(item['price'] * item['quantity'] for item in cart)
    return render_template('cart.html', cart=cart, total=total)


# Rota para remover item do carrinho
@app.route('/remove_from_cart/<int:item_id>')
def remove_from_cart(item_id):
    cart = session.get('cart', [])
    cart = [item for item in cart if item['id'] != item_id]
    session['cart'] = cart
    return redirect(url_for('cart'))


# Rota para o checkout (formulário de endereço)
@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        # Processar o endereço e finalizar compra
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        zip_code = request.form['zip_code']

        # Aqui você pode processar a compra (armazenar o pedido, enviar e-mail, etc.)
        return redirect(url_for('order_success'))

    return render_template('checkout.html')


# Rota para sucesso do pedido
@app.route('/order_success')
def order_success():
    # Limpar o carrinho após a compra
    session.pop('cart', None)
    return render_template('order_success.html')


if __name__ == '__main__':
    app.run(debug=True)
