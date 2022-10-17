from ..utils import db
from datetime import date

class VendorCommissions(db.Model):
    """
    VendorCommissions model contains information about the 
    commissions taken by each vendor during a sale of a product,
    with the table showing the Vendor ID along with the commsision 
    rate and the date the information was added to the database.
    ...

    Columns
    -------
    date : datetime 
        Unique ID of each promotion offered
    vendor_id: int
        Unique ID of each vendor
    rate: float
        Commission rate applied to each vendor
    """

    __tablename__='VendorCommissions'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    date = db.Column(db.DateTime, default=date.today())
    vendor_id = db.Column(db.Integer, nullable=False)
    rate = db.Column(db.Float)

    def __repr__(self):
        return f'<Vendor ID: {self.vendor_id}>'
