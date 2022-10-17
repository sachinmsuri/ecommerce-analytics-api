from ..utils import db

class Promotion(db.Model):
    """
    Promotion model contains information about each 
    promotiom, showing a unique ID for each promotion along 
    with a description of the promotion.

    ...

    Columns
    -------
    id : int 
        Unique ID of each promotion offered
        (Primary Key)
    description: str
        Description of promotion
    """

    __tablename__='Promotion'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    description = db.Column(db.String(250))

    def __repr__(self):
        return f'<Promotion ID: {self.id}>'
