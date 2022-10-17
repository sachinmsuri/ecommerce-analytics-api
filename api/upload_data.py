import pandas as pd
from sqlalchemy import create_engine
import os
import pandas as pd

BASE_DIR=os.path.dirname(os.path.realpath(__file__))
URI = f"sqlite:///{os.path.join(BASE_DIR,'config/db.sqlite3')}"

def upload_data(uri):
    '''
    Function to allow users to add data to the database
    to easily test-end points. Function looks at the
    data directory and adds the relevant CSV to the 
    correct Model using SQLAlchemy and Pandas

        Parameters:
                uri (str): database path name
                   
    '''
    engine = create_engine(uri)

    file_mappings = {
        'data/products.csv': 'Product',
        'data/promotions.csv': 'Promotion',
        'data/product_promotions.csv': 'ProductPromotion',
        'data/commissions.csv': 'VendorCommissions',
        'data/orders.csv': 'Order',
        'data/order_lines.csv': 'OrderLine'
    }

    for file, table in file_mappings.items():
        print(f'Upload data to table - {table}')
        (pd.read_csv(file)
        .to_sql(table, con=engine, if_exists='append', index=False))

if __name__== '__main__':
    upload_data(URI)