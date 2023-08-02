# pylint: disable=import-error
# pylint: disable=no-name-in-module
import os 
from sensor.constants.s3_bucket import PREDICTION_BUCKET_NAME


#defining common constant variable for training pipeline
TARGET_COLUMN = "class"
PIPELINE_NAME:str = "sensor"
ARTIFACT_DIR: str = "artifact"
FILE_NAME:str = "sensor.csv"

TRAIN_FILE_NAME:str = "train.csv"
TEST_FILE_NAME:str = "test.csv"

PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"
MODEL_FILE_NAME = "model.pkl"
SCHEMA_FILE_PATH = os.path.join("config","schema.yaml")

SCHEMA_DROP_COLS = "drop_columns"



#-----------------------------------
# Data Ingestion related constants
#-----------------------------------

DATA_INGESTION_COLLECTION_NAME:str = "kafka-sensor-data"
DATA_INGESTION_DIR_NAME:str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str = "feature_store"
DATA_INGESTION_INGESTED_DIR:str = "ingested"

DATA_INGESTION_TRAIN_TEST_SPLIT_RATION:float = 0.2


"""
Data Validation related constants

"""

DATA_VALIDATION_DIR_NAME: str = "data_validation" # root folder
DATA_VALIDATION_VALID_DIR:str = "validated"
DATA_VALIDATION_INVALID_DIR:str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR:str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str = "report.yaml" #yaml is more readible type



"""
Data Transformation Related constants 
"""
DATA_TRANSFORMATION_DIR_NAME :str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR :str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR:str = "transformed_object" # preprocessing.pkl object


