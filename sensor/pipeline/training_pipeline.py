# pylint: disable=all
from sensor.entity import config_entity
from sensor.exceptions import SensorException
import os , sys
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor import logger
from sensor.components.data_ingestion import DataIngestion



class TrainPipeline:

    def __init__(self):
        self.training_pipeline_config = config_entity.TrainingPipelineConfig()
        

    
    def start_data_ingestion(self)->DataIngestionArtifact:
        try: 
            self.data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            logger.logging.info("Starting Data Ingestion")
            data_ingestion= DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact= data_ingestion.initiate_data_ingestion()
            
            logger.logging.info(f"Data Ingestion Completed and artifact:{data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e:
            raise SensorException(e,sys)
        
    def start_data_validation(self):
        try: 
            pass
        
        except Exception as e:
            raise SensorException(e,sys)
        
    def start_data_transformation(self):
        try: 
            pass
        
        except Exception as e:
            raise SensorException(e,sys)
        

    def start_model_trainer(self):
        try: 
            pass
        
        except Exception as e:
            raise SensorException(e,sys)
        

    def start_model_evaluation(self):
        try: 
            pass
        
        except Exception as e:
            raise SensorException(e,sys)
        

    def start_model_pusher(self):
        try: 
            pass
        
        except Exception as e:
            raise SensorException(e,sys)
        

    def run_pipeline(self):
        try: 
            data_ingestion_artifact:DataIngestionArtifact = self.start_data_ingestion()
        
        except Exception as e:
            raise SensorException(e,sys)
        

