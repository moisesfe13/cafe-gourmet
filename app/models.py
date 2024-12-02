from tinydb import TinyDB, Query

# Conexão com o banco de dados TinyDB
db = TinyDB('db.json')
menu_table = db.table('menu')  # Tabela para os itens do menu
CartItem = db.table('cart_items')  # Tabela para os itens do carrinho

class MenuItem:
    def __init__(self, id, name, price, description, image, stock):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.image = image
        self.stock = stock

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'image': self.image,
            'stock': self.stock
        }

    @staticmethod
    def get_all_items():
        # Retorna todos os itens do cardápio
        return [
            MenuItem(item['id'], item['name'], item['price'], item['description'], item['image'], item['stock'])
            for item in menu_table.all()
        ]

    @staticmethod
    def add_default_items():
        # Checa se já existem produtos no banco de dados, senão, insere os produtos padrão
        if len(menu_table) == 0:
            menu_data = [
                {'id': 1, 'name': 'Expresso', 'price': 5.00, 'description': 'Café forte e concentrado.', 'image': 'cafe1.png', 'stock': 50},
                {'id': 2, 'name': 'Cappuccino', 'price': 7.00, 'description': 'Café com leite e espuma.', 'image': 'cafe2.png', 'stock': 30},
                {'id': 3, 'name': 'Latte', 'price': 8.00, 'description': 'Café com leite vaporizado.', 'image': 'cafe3.png', 'stock': 20},
                {'id': 4, 'name': 'Mocha', 'price': 9.00, 'description': 'Café com chocolate e leite.', 'image': 'cafe4.png', 'stock': 15},
                {'id': 5, 'name': 'Macchiato', 'price': 6.00, 'description': 'Café com um pouco de leite.', 'image': 'cafe5.png', 'stock': 40},
                {'id': 6, 'name': 'Café Gelado', 'price': 7.50, 'description': 'Café gelado com gelo.', 'image': 'cafe6.png', 'stock': 25},
                {'id': 7, 'name': 'Chá Gelado', 'price': 5.50, 'description': 'Chá refrescante gelado.', 'image': 'cafe7.png', 'stock': 30},
                {'id': 8, 'name': 'Flat White', 'price': 8.00, 'description': 'Leite vaporizado com café expresso.', 'image': 'cafe8.png', 'stock': 18},
                {'id': 9, 'name': 'Café Americano', 'price': 5.00, 'description': 'Café com mais água.', 'image': 'cafe9.png', 'stock': 50},
                {'id': 10, 'name': 'Affogato', 'price': 10.00, 'description': 'Café expresso com sorvete de baunilha.', 'image': 'cafe10.png', 'stock': 10},
            ]
            menu_table.insert_multiple(menu_data)  # Insere os itens no banco

# Chama a função para adicionar os itens padrões ao banco, se necessário
MenuItem.add_default_items()
