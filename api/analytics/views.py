from flask_restx import Namespace
from flask_restx import Resource
from flask import jsonify
from flask import make_response
from flask import abort
from ..utils import db
from ..models.order_line import OrderLine
from ..models.order import Order
from ..models.product_promotion import ProductPromotion
from ..models.vendor_commissions import VendorCommissions
import pandas as pd
from datetime import datetime
from datetime import timedelta
from sqlalchemy import select, join, and_, cast, Date
from .calculate import Calculate

analytics_namespace = Namespace(
    'analytics',
    description='Retrieve analytics from orders'
)

@analytics_namespace.route('/daily/<string:date>')
@analytics_namespace.doc(
    description=('For a given day retrive analytics showing '
                'information around customers, orders placed, '
                'pricing, promotions and commsisions.')
)
class OrderAnalytics(Resource):
    """
    Class to create an GET end-point allowing users 
    to query analytics based on a given day
    showing analyutics based on order totals, customers, 
    discountes applied,average orders totals,
    commissions and promotions.

    This class calls another class called Calculate to
    make the relevant calculations and generate the summary
    statistics
    
    Methods
    -------
    get:
        returns order analytics for a given day

    """

    def get(self, date):
        """
        Returns JSON data for GET request with 
        relevant error message
        
        The summary statitics are calculed from another 
        class called Calculate which returns the data as a
        dictionary.

        Parameters
        ----------
        date : str, required
            date formatted as YYYY-MM-DD

        Returns
        -------
        JSON data containing summary startics/analytics 
        of orders for a given day.

        Raises
        -------
            ValueError - If data has the incorrect format
            Empty DataFrame - No data in database for given day
        """
        #Convert date submitted by user to datetime python object
        try:
            date = datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError:
            abort(400, description='Date is not in the format required YYYY-MM-DD')

        #Find all order_ids for date specified by user
        order_ids = [
            order.id for order in 
            Order.query.filter(Order.created_at >= date)
                        .filter(Order.created_at < date + timedelta(days = 1))
        ]

        #Query to left join both the Order and VendorCommissions Model 
        #onto the OrderLine method for ID's in order_ids variable 
        #and date specified by user in request
        orders_query = (select(OrderLine, Order.created_at, Order.vendor_id, Order.customer_id,
                        VendorCommissions.rate)
                        .where(OrderLine.order_id.in_(order_ids))
                        .join(Order, Order.id==OrderLine.order_id, isouter=True)
                        .join(VendorCommissions, VendorCommissions.vendor_id==Order.vendor_id, isouter=True)
                        .where(VendorCommissions.date == date))
        
        #Return query from db as pandas DataFrame
        orders_df = pd.read_sql(
            sql=orders_query,
            con = db.session.bind
        )
        
        #Return message if no data found in database for given day
        if orders_df.empty:
            message = {'message': 'No orders took place on this day'}
            return make_response(jsonify(message), 200)


        #Query promotions table for day requested by user
        promotion_query = (
            select(ProductPromotion.product_id, ProductPromotion.promotion_id)
                    .where(ProductPromotion.date == date)
        )

        #Return query from db as Pandas DataFrame
        promotions_df = pd.read_sql(
            sql=promotion_query,
            con = db.session.bind
        )

        #Calculate summary statistics/analytics 
        # from .Calculate class
        data = Calculate(orders_df, promotions_df).main()
    
        return make_response(jsonify(data), 200)