from sensor.utils.main_utils import  save_object,load_object, write_yaml_file
from sensor.exceptions import SensorException
from sensor.logger import logging
from sensor.entity.artifact_entity import DataValidationArtifact, ModelTrainerArtifact, ModelEvaluationArtifact
from sensor.entity.config_entity import ModelEvaluationConfig

import os,sys

from sensor.ml.metric.classification_metric import get_classification_score
from sensor.ml.model.model_estimator import SensorModel, ModelResolver

import pandas as pd 
import numpy as np

from sensor.constants.training_pipeline import TARGET_COLUMN



class ModelEvaluation:
    
    def __init__(self,model_eval_config:ModelEvaluationConfig,
                 data_validation_artifact:DataValidationArtifact,
                 model_trainer_artifact:ModelTrainerArtifact):
        
        try: 
            self.model_eval_config = model_eval_config
            self.data_validation_artifact = data_validation_artifact
            self.model_trainer_artifact = model_trainer_artifact

        except Exception as e:
            raise SensorException(e,sys)
        


    def initiate_model_evaluation(self)->ModelEvaluationArtifact:

        try: 
            valid_train_file_path = self.data_validation_artifact.valid_train_file_path
            valid_test_file_path =  self.data_validation_artifact.valid_test_file_path


            #load valid train and test dataframes
            train_df = pd.read_csv(valid_train_file_path)
            logging.info(f"train_df columns:{train_df.columns}")
            test_df = pd.read_csv(valid_test_file_path)
            logging.info(f"test_df columns:{test_df.columns}")

            #concatanate the df's for evaluation
            df= pd.concat(objs=[train_df,test_df],axis=0)
            y_true = pd.DataFrame(np.where(df[TARGET_COLUMN]<0,0,1))
            df.drop(TARGET_COLUMN,axis=1,inplace=True)
            logging.info(f"concat_df columns:{df.columns}")

            is_model_accepted=True 
            train_model_file_path = self.model_trainer_artifact.trained_model_file_path

            model_resolver = ModelResolver()
            if not model_resolver.is_model_exists(): # if no model exists currently
                model_evaluation_artifact = ModelEvaluationArtifact(
                    is_model_accepted=is_model_accepted,
                    improved_accuracy=None,
                    best_model_path = None,
                    trained_model_path=train_model_file_path,
                    trained_model_metric_artifact= self.model_trainer_artifact.test_metric_artifact,
                    best_model_metric_artifact=None
                 )
                logging.info(f"Model evaluation artifact : {model_evaluation_artifact}")
                return model_evaluation_artifact
            

            # load the current and best model for comparison
            
            latest_model_path = model_resolver.get_best_model_path()
            latest_model = load_object(file_path=latest_model_path)
            train_model = load_object(file_path=train_model_file_path)


            y_trained_pred= train_model.predict(df.values)
            y_latest_pred = latest_model.predict(df.values)

            trained_metric = get_classification_score(y_true,y_trained_pred)
            latest_metric = get_classification_score(y_true, y_latest_pred)

            improved_accuracy = trained_metric.f1_score - latest_metric.f1_score
            if improved_accuracy> self.model_eval_config.change_threshold:
                is_model_accepted=True 

            else:
                is_model_accepted = False 

            model_evaluation_artifact = ModelEvaluationArtifact(
                is_model_accepted=is_model_accepted,
                improved_accuracy=improved_accuracy,
                best_model_path = latest_model_path,
                trained_model_path=train_model_file_path,
                trained_model_metric_artifact= trained_metric,
                best_model_metric_artifact=latest_metric
                )
            logging.info(f"Model evaluation artifact : {model_evaluation_artifact}")
            
            #save the records
            model_eval_report = model_evaluation_artifact.__dict__
            write_yaml_file(file_path=self.model_eval_config.report_file_path,content=model_eval_report)

            return model_evaluation_artifact
        






        except Exception as e:
            raise SensorException(e,sys)
        



    