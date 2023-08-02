# pylint: disable=all

from sensor.exceptions import SensorException
import os, sys
from sensor.logger import logging
from sensor.entity import config_entity
from sensor.pipeline.training_pipeline import TrainPipeline

import pandas as pd 

from sensor.data_access.sensor_data import SensorData

from sensor.exceptions import SensorException
from sensor.logger import logging
from sensor.entity.config_entity import DataIngestionConfig
from sensor.entity.artifact_entity import DataIngestionArtifact
import os,sys
from pandas import DataFrame
from sensor.data_access.sensor_data import SensorData

from typing import Optional
import numpy as np

from sensor.constants.database import DATABASE_NAME
import pymongo
import certifi

            

if __name__ == '__main__':
    try:

        training_pipeline= TrainPipeline()
        training_pipeline.run_pipeline()
    except Exception as e:
        raise SensorException(e,sys)
    """ 

    training_pipeline_config = config_entity.TrainingPipelineConfig()
    data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
    data_ingestion= DataIngestion(data_ingestion_config=data_ingestion_config)
    df= data_ingestion.export_data_into_feature_store() """