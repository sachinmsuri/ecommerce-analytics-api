from ..utils import db
from datetime import date

class Order(db.Model):
    """
    Order model contains information about each order placed,
    showing a unique order ID along with the ID of 
    the customer who placed the order, the date of the order
    and the ID of the vendor selling the product.

    ...

    Columns
    -------
    id : int 
        Unique ID of each order placed.
        (Primary Key)
    created_at: datetime
        Date and time order was placed.
    vendor_id: int
        ID of vendor selling product.
    customer_id: int
        ID of customer selling product.
    """

    __tablename__='Order'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=date.today())
    vendor_id = db.Column(db.Integer)
    customer_id = db.Column(db.Integer)

    def __repr__(self):
        return f'<Order ID: {self.id}>'
