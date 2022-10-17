from ..utils import db
from datetime import datetime

class OrderLine(db.Model):
    """
    OrderLine model contains the product information
    for each order showing the products bought by a 
    customer in each order (an order can have multiple
    products bought) along with details around how much money 
    was money paid for each product including the amount of 
    VAT, discount and any promotion applied to each product.    

    ...

    Columns
    -------
    order_id : int 
        id of the order placed
        (Foreign Key -> Model=Order, Column=id)
    product_id: int
        id of product bought in order
        (Foreign Key -> Model=Product, Column=id)
    product_description: str
        description of product bought
    product_price: int
        original price of of product
    product_vat_rate: float
        vat applied to product in order
    discount_rate: float
        discount rate applied to product in order
    quantity: int
        Number of products bought in order
    full_price_amount: int
        total price paid for product
    discounted_amount: float
        total real value discounted from product
    vat_amount: float
        total real vat amount placed on product
    total_amount: float
        full price of product after discount and 
        vat applied to order
    """

    __tablename__='OrderLine'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('Order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('Product.id'), nullable=False)
    product_description = db.Column(db.String(250))
    product_price = db.Column(db.Integer)
    product_vat_rate = db.Column(db.Float)
    discount_rate = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    full_price_amount = db.Column(db.Integer)
    discounted_amount = db.Column(db.Integer)
    vat_amount = db.Column(db.Float)
    total_amount = db.Column(db.Float)

    def __repr__(self):
        return f'<Order ID: {self.id}>'
