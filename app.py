from src.e2emlprj.logger import logging
from src.e2emlprj.exception import CustomException
import sys
from src.e2emlprj.components.data_ingestion import DataIngestion
#from src.e2emlprj.components.data_ingestion import DataIngestionConfig


if __name__=="__main__":
    logging.info("The execution has started")

    try:
        #a=1/0
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.info("Custom Exception ")
        raise CustomException(e,sys)    