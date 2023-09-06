import os
import sys
from src.e2emlprj.exception import CustomException
from src.e2emlprj.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()  #loads all env variables

host=os.getenv("host")
user=os.getenv("user")
pwd=os.getenv("password")
db=os.getenv("db")

def read_sql_data():
    logging.info("Reading SQL Databse started")
    try:
        mydb=pymysql.connect(
             host=host,
             user=user,
             password=pwd,
             db=db
        )
        logging.info("DB Connection estabilised ",mydb)

        df=pd.read_sql_query("Select * from studentsperformance",mydb)
        print(df)
        return df

    except Exception as e:
            raise CustomException(e,sys)


