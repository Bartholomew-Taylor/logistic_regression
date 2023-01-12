import os
import pandas as pd
from scipy import stats
from pydataset import data
import numpy as np
import env

def get_connection(db, username=env.username, host=env.host, password=env.password):
    return f'mysql+pymysql://{username}:{password}@{host}/{db}'
    '''
    this function acts as a part of the function below to establish a connection
    with the sql server
    '''




def get_telco_data():
    
    '''
    this function retrieves the telco_db info from the sql server
    or calls up the csv if it's saved in place
    
    '''
    
    filename = "telco_churn.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # read the SQL query into a dataframe
        df = pd.read_sql('SELECT * FROM customers LEFT JOIN contract_types USING(contract_type_id) LEFT JOIN internet_service_types USING(internet_service_type_id) LEFT JOIN payment_types USING(payment_type_id) LEFT JOIN customer_contracts USING(customer_id) LEFT JOIN customer_details USING(customer_id) LEFT JOIN customer_payments USING(customer_id) LEFT JOIN customer_signups USING(customer_id) LEFT JOIN customer_subscriptions USING(customer_id)', get_connection ('telco_churn'))

        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename)

        # Return the dataframe to the calling code
        return df  
    