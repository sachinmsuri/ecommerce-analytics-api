from flask import Flask
from flask_restx import Api
from .config.config import config_dict
from .analytics.views import analytics_namespace
from .utils import db
from .models.order_line import OrderLine
from .models.order import Order
from .models.product_promotion import ProductPromotion
from .models.product import Product
from .models.promotion import Promotion
from .models.vendor_commissions import VendorCommissions

def create_app(config=config_dict['DEV']):
    '''
    Function to instantiate Flask Application and 
    add the namepaces too the application.
    A shell is also created to to allow users to 
    create the database the tables within the database.

        Parameters:
                config (dict): Config specifciation depending 
                                if we are running a test 
                                or development environement.
        Returns:
                Instance of Flask Application (FLASK)
                   
    '''

    app=Flask(__name__)   

    app.config.from_object(config)

    db.init_app(app)

    api=Api(
        app,
        title='eCommerce API',
        description=('REST API for eCommerce Store')
    )

    api.add_namespace(analytics_namespace)

    #Shell to access/create database
    @app.shell_context_processor
    def make_shell_context():
        return {
            'db':db,
            'Order':Order,
            'OrderLine':OrderLine,
            'Product': Product,
            'ProductPromotion': ProductPromotion,
            'Promotion': Promotion,
            'VendorCommissions': VendorCommissions,
        }

    return app

