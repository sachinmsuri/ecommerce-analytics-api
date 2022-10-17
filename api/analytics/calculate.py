import pandas as pd

class Calculate:
    """
    A class to calculate summary analytics for the 
    GET end-point '/daily/<string:date>' within the
    analytics_namespace.

    ...

    Attributes
    ----------
    orders : pd.DataFrame
        Dataframe querying the Order, OrderLine and 
        VendorCommissions Models
    promotions : pd.DataFrame
        Dataframe querying the ProductPromotion Model
    self.data : dictionary
        Dictionary that will be JSON serialised when 
        returning data to the user

    Methods
    -------
    total_customers:
        calculate total unique customers placing orders
    total_discount:
        calculate total discount applied to all order
    total_items:
        calculate total items purchases in all orders
    avg_discount:
        calculate average discount for all orders
    avg_order_total:
        calculate average price for each customer order 
    Total Commissions:
        calculate average price for each customer order 
    avg_comissions:
        calculate average commission for each order
    calculate_promotions:
        calculate the total commissions for each promotion
    main:
        run all functionns and return updated self.data
        attribute
    """

    def __init__(self, orders, promotions):
        self.orders = orders
        self.promotions = promotions

        self.data = {"commissions": {}}

    def total_customers(self):
        try:
            value = int(len(self.orders['customer_id'].unique()))
            self.data['customers'] = value
            
            return value
        except Exception as e:
            print(str(e))

    def total_discount(self):
        try:
            value = int(self.orders['discounted_amount'].sum())
            self.data['total_discount_amount'] = value

            return value
        except Exception as e:
            print(str(e))
    
    def total_items(self):
        try:
            value = int(self.orders['quantity'].sum())
            self.data['quantity'] = value

            return value
        except Exception as e:
            print(str(e))
    
    def avg_discount(self):
        try:
            value = float(self.orders['discount_rate'].mean())
            self.data['discount_rate'] = value

            return value
        except Exception as e:
            print(str(e))

    def avg_order_total(self):
        try:
            value = int(self.orders['quantity'].sum())/\
                        len(self.orders['order_id'].unique())
            self.data['order_total_avg'] = value
        except Exception as e:
            print(str(e))

    def total_commissions(self):
        try:
            self.orders['commissions'] = (
                self.orders['rate'] * self.orders['total_amount']
            )
            value = int(self.orders['commissions'].sum())
            self.data['commissions']['Total'] = value

            return value
        except Exception as e:
            print(str(e))
    
    def avg_comissions(self):
        try:
            value = int(
                self.orders['commissions'].sum() 
                / len(self.orders['order_id'].unique())
            )
            self.data['commissions']['order_average'] = value
            
            return value
        except Exception as e:
            print(str(e))
    
    def calculate_promotions(self):
        try:
            df = pd.merge(
                self.orders, self.promotions,
                on='product_id', how='left'
            )

            df = (df.groupby('promotion_id')['commissions']
                    .sum()
                    .reset_index())
            
            df.promotion_id = (df.promotion_id
                                .astype(int)
                                .astype(str))
            
            promotions_data = dict()
            
            for ind in df.index:
                promotions_data[df['promotion_id'][ind]] = int(df['commissions'][ind])
            
            self.data['commissions']['promotions'] = promotions_data       
        except Exception as e:
            print(str(e))

    def main(self):
        self.total_customers()
        self.total_discount()
        self.total_items()
        self.avg_discount()
        self.avg_order_total()
        self.total_commissions()
        self.avg_comissions()

        if not self.promotions.empty:
            self.calculate_promotions()
        
        return self.data















