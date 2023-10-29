from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
from housing.config.configuration import Configuartion
from housing.util.util import load_data
import sys


import os
def main():
    try:
        #config_path = os.path.join("config","config.yaml")
        #pipeline = Pipeline(Configuartion(config_file_path=config_path))
        #data_ingestion_config = Configuartion().get_data_ingestion_config()
        #print(data_ingestion_config)
        
        
        #schema_file_path=r"D:\ML_project\Machine_Learning_Project_1\config\schema.yaml"
        #file_path=r"D:\ML_project\Machine_Learning_Project_1\housing\artifact\data_ingestion\2023-10-28-18-58-22\ingested_data\train\housing.csv"
        
        #df = load_data(file_path=file_path, schema_file_path=schema_file_path)
        #print(df.columns)
        #print(df.dtypes)
        

        #data_transformation_config = Configuartion().get_data_transformation_config()
        #print(data_transformation_config)
        
        pipeline = Pipeline()
        pipeline.run_pipeline()
        #p.ipeline.start()
        #logging.info("main function execution completed.")
        
        #data_validation_config = Configuartion().get_data_validation_config()
        #print(data_validation_config)
        # schema_file_path=r"D:\Project\machine_learning_project\config\schema.yaml"
        # file_path=r"D:\Project\machine_learning_project\housing\artifact\data_ingestion\2022-06-27-19-13-17\ingested_data\train\housing.csv"

        # df= DataTransformation.load_data(file_path=file_path,schema_file_path=schema_file_path)
        # print(df.columns)
        # print(df.dtypes)

    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__=="__main__":
    main()
