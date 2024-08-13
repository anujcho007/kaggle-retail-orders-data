import sqlalchemy
import pandas as pd


df = pd.read_csv('orders.csv', na_values=['Not Available', 'unknown'])
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ', '_')
df['discount_price'] = df['list_price']*df['discount_percent']*.01
df['sale_price'] = df['list_price']-df['discount_price']
df['profit'] = df['sale_price']-df['cost_price']
df['order_date'] = pd.to_datetime(df['order_date'], format="%Y-%m-%d")
df.drop(columns=['list_price', 'cost_price',
                 'discount_percent'], inplace=True)


hostname = 'localhost'
username = 'root'
password = 'root'
port = 3306
database = 'orders'

# dbapi_connection = mysql.connector.connect(
# user=username, password=password, host=hostname, database=database)

cnx = sqlalchemy.create_engine(
    'mysql+pymysql://' + username+':'+password+'@'+hostname+':'+str(port)+'/'+database)

df.to_sql('df_orders', con=cnx, index=False, if_exists='append')
