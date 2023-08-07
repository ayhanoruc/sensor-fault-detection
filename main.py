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
from sensor.utils.main_utils import read_yaml_file
from sensor.constants.database import DATABASE_NAME
from sensor.constants.training_pipeline import SAVED_MODEL_DIR
from sensor.ml.model.model_estimator import ModelResolver, TargetValueMapping
from sensor.utils.main_utils import load_object
import pymongo
import certifi
from fastapi import FastAPI
from fastapi.responses import Response
from sensor.constants.application import APP_HOST, APP_PORT   
from starlette.responses import RedirectResponse
from uvicorn import run as app_run       
from fastapi.middleware.cors import CORSMiddleware


env_file_path=os.path.join(os.getcwd(),"env.yaml")

def set_env_variable(env_file_path):

    if os.getenv('MONGO_DB_URL',None) is None:
        env_config = read_yaml_file(env_file_path)
        os.environ['MONGO_DB_URL']=env_config['MONGO_DB_URL']


app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def train_route():
    try:

        train_pipeline = TrainPipeline()
        if train_pipeline.is_pipeline_running:
            return Response("Training pipeline is already running.")
        train_pipeline.run_pipeline()
        return Response("Training successful !!")
    except Exception as e:
        return Response(f"Error Occurred! {e}")

@app.get("/predict")
async def predict_route():
    try:
        #get data from user csv file
        #conver csv file to dataframe

        df=None
        model_resolver = ModelResolver(model_dir=SAVED_MODEL_DIR)
        if not model_resolver.is_model_exists():
            return Response("Model is not available")
        
        best_model_path = model_resolver.get_best_model_path()
        model = load_object(file_path=best_model_path)
        y_pred = model.predict(df)
        df['predicted_column'] = y_pred
        df['predicted_column'].replace(TargetValueMapping().reverse_mapping(),inplace=True)
        
        #decide how to return file to user.
        
    except Exception as e:
        raise Response(f"Error Occured! {e}")

def main():
    try:
        set_env_variable(env_file_path)
        training_pipeline = TrainPipeline()
        training_pipeline.run_pipeline()
    except Exception as e:
        print(e)
        logging.exception(e)


if __name__=="__main__":
    #main()
    set_env_variable(env_file_path)
    app_run(app, host=APP_HOST, port=APP_PORT)