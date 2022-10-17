from ..utils import db

class Product(db.Model):
    """
    Product model contains information regarding the product,
    showing the Unique ID of each product along with a 
    description of the product.

    ...

    Columns
    -------
    id : int 
        Unique ID of each product that can be ordered
        (Primary Key)
    description: str
        Description of product
    """

    __tablename__='Product'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    description = db.Column(db.String(250))

    def __repr__(self):
        return f'<Product ID : {self.id}>'
