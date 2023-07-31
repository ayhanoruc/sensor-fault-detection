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

DATA_INGESTION_COLLECTION_NAME:str = "sensor"
DATA_INGESTION_DIR_NAME:str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str = "feature_store"
DATA_INGESTION_INGESTED_DIR:str = "ingested"

DATA_INGESTION_TRAIN_TEST_SPLIT_RATION:float = 0.2

