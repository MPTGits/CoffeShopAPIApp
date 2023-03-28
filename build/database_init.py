import asyncio

from sqlalchemy import MetaData, Table, Column, Integer, ForeignKey, String, Date, CHAR, Float, create_engine
import pandas as pd

from app.configuration.configuration import Configuration
from app.environment import Environment

# TODO: Rework this build file into a better looking interface

metadata = MetaData()

Table('Sales_Outlet', metadata,
    Column('sales_outlet_id', Integer, primary_key=True, autoincrement=True),
    Column('sales_outlet_type', String(256), nullable=False),
    Column('store_address', String(256), nullable=False),
    Column('store_city', String(256), nullable=False),
    Column('store_telephone', String(12),  nullable=False)
)

Table('Customer', metadata,
    Column('customer_id', Integer, primary_key=True, autoincrement=True),
    Column('home_store', Integer, ForeignKey('Sales_Outlet.sales_outlet_id'), nullable=False),
    Column('customer_first_name', String(256), nullable=False),
    Column('customer_email', String(256), nullable=True),
    Column('customer_since', Date, nullable=False),
    Column('loyalty_card_number', String(12), nullable=True),
    Column('birthdate', Date, nullable=False),
    Column('gender', CHAR, nullable=False),
)


Table('Product', metadata,
    Column('product_id', Integer, primary_key=True, autoincrement=True),
    Column('product_group', String(256), nullable=False),
    Column('product_category', String(256), nullable=False),
    Column('product_type', String(256), nullable=False),
    Column('product', String(256), nullable=False),
    Column('product_description', String(256), nullable=True),
)


Table('Pastry_Inventory', metadata,
    Column('sales_outlet_id', Integer, ForeignKey('Sales_Outlet.sales_outlet_id'), nullable=False),
    Column('product_id', Integer, ForeignKey('Product.product_id'), nullable=False),
    Column('transaction_date', Date, nullable=False),
    Column('start_of_day', Integer, nullable=False),
    Column('quantity_sold', Integer, nullable=False),
)

Table('Sales_Reciept', metadata,
    Column('reciept_id', Integer, primary_key=True, autoincrement=True),
    Column('transaction_id', Integer),
    Column('transaction_date', Date, nullable=False),
    Column('transaction_time', String(10), nullable=False),
    Column('sales_outlet_id', Integer, ForeignKey('Sales_Outlet.sales_outlet_id'), nullable=False),
    Column('customer_id', Integer, ForeignKey('Customer.customer_id'), nullable=False),
    Column('quantity', Integer,  nullable=False),
    Column('unit_price', Float, nullable=False),
)



if __name__ == '__main__':
    Configuration.init()
    db_name, host, user, password = Configuration.get_db_connection_info()
    engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}/{db_name}')

    metadata.create_all(engine)

    df = pd.read_csv('dataset/sales_outlet.csv')

    data = df[['sales_outlet_id', 'sales_outlet_type', 'store_address', 'store_city', 'store_telephone']]

    data.to_sql('Sales_Outlet', engine, if_exists='append', index=False)

    df = pd.read_csv('dataset/customer.csv')

    customer_data = df[['customer_id', 'home_store', 'customer_first_name', 'customer_email', 'customer_since', 'loyalty_card_number', 'birthdate', 'gender']]

    customer_data.to_sql('Customer', engine, if_exists='append', index=False)

    df = pd.read_csv('dataset/product.csv')

    data = df[['product_id', 'product_group', 'product_category', 'product_type', 'product', 'product_description']]

    data.to_sql('Product', engine, if_exists='append', index=False)

    df = pd.read_csv('dataset/pastry inventory.csv')

    data = df[['sales_outlet_id', 'product_id', 'transaction_date', 'start_of_day', 'quantity_sold']]

    data.to_sql('Pastry_Inventory', engine, if_exists='append', index=False)

    df = pd.read_csv('dataset/sales_reciepts.csv')

    data = df[['transaction_id', 'transaction_date', 'transaction_time', 'sales_outlet_id', 'customer_id', 'quantity', 'unit_price']][df['customer_id'].isin(customer_data['customer_id'])]

    data.to_sql('Sales_Reciept', engine, if_exists='append', index=False)