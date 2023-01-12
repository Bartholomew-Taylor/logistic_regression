import pandas as pd
from scipy import stats
from pydataset import data
import numpy as np
import env
import os

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

def clean_telco(df):
    '''
    this function cleans up the telco db
    '''
    
    to_drop = ['internet_service_type_id', 'internet_service_type_id.1', 
               'contract_type_id', 'payment_type_id', 'internet_service_type_id',
               'senior_citizen.1', 'payment_type_id.1', 'gender.1', 'contract_type_id.1',
               'paperless_billing.1','gender.1','senior_citizen.1', 'partner.1','dependents.1',
               'payment_type_id.1', 'monthly_charges.1', 'total_charges', 'total_charges.1','phone_service.1',
               'multiple_lines.1', 'online_security.1','online_backup.1','device_protection.1',
               'tech_support.1', 'streaming_tv.1','streaming_movies.1']
    df.drop(columns = to_drop, inplace = True)
    df.drop(df.columns[0], axis = 1, inplace = True)
    df['total_charges'] = (df.tenure * df.monthly_charges)
    df = df[df.total_charges != 0]
    df['charge_rank'] = pd.qcut(df['total_charges'], 4, labels = ['a','b','c','d'])
    return df

def dummies_telco(df):
    '''
    this function generates dummy columns for modeling
    '''
    outout = []
    outout = pd.get_dummies(df[['charge_rank', 'internet_service_type', 'gender', 'senior_citizen', 'partner', 
                                                'contract_type', 'dependents', 'phone_service','multiple_lines',
                                               'online_security', 'online_backup','device_protection','streaming_tv', 
                                                'paperless_billing','churn', 'contract_type','internet_service_type',
                                               'payment_type']],drop_first = [True, True])
    outout['customer_id'] = df.customer_id
    return outout


def train_val_test(df, target):
    '''
    this function splits up the data into sections for training,
    validating, and testing
    models
    '''
    seed = 99
    train, val_test = train_test_split(df, train_size = 0.7,
                                       random_state = seed, stratify = df[target])
    validate, test = train_test_split(val_test, train_size = 0.5, random_state = seed,
                                      stratify = val_test[target])
    return train, validate, test
