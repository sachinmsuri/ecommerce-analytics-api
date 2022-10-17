from ..utils import db
from datetime import date

class ProductPromotion(db.Model):
    """
    ProductPromotion model contains information about the 
    promotion applied to each product, with the table showing
    the promotion_id applied to each product_id and when 
    the promotion was created.
    ...

    Columns
    -------
    date : datetime 
        Date promotion was created
    product_id: int
        ID of product that promotion is applied to
        (Foreign Key -> Model=Product, Column=id)
    promotion_id: int
        ID of promotion that is applied to product
        (Foreign Key -> Model=Promotion, Column=id)

    """

    __tablename__='ProductPromotion'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    date = db.Column(db.DateTime, default=date.today())
    product_id = db.Column(db.Integer, db.ForeignKey('Product.id'), nullable=False)
    promotion_id = db.Column(db.Integer, db.ForeignKey('Promotion.id'), nullable=False)

    def __repr__(self):
        return f'<Promotion ID: {self.promotion_id}>'
