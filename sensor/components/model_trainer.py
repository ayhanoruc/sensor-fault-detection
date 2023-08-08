
from sensor.utils.main_utils import load_numpy_array_data
from sensor.exceptions import SensorException
from sensor.logger import logging
from sensor.entity.artifact_entity import DataTransformationArtifact #to see where the Transformed data is
from sensor.entity.artifact_entity import ModelTrainerArtifact # for outputs
from sensor.entity.config_entity import ModelTrainerConfig
from sensor.ml.metric.classification_metric import get_classification_score
from xgboost import XGBClassifier
from sensor.ml.model.model_estimator import SensorModel
from sensor.utils.main_utils import save_object, load_object
import os,sys
import numpy as np
from sklearn.linear_model import LogisticRegression
class ModelTrainer:

    def __init__(self,model_trainer_config:ModelTrainerConfig,
                 data_transformation_artifact:DataTransformationArtifact):
        
        try:
            
            self.model_trainer_config = model_trainer_config
            self.data_transformation_artifact = data_transformation_artifact
        
        
        except Exception as e:
            raise SensorException(e,sys)


    def perform_hyper_tuning(self):

        try:
            pass 

        except Exception as e:
            raise SensorException(e,sys)


    def train_model(self,x_train,y_train)->LogisticRegression():
        try:


            l_r= LogisticRegression()
            l_r.fit(x_train,y_train)
            
            #xgb_clf = XGBClassifier()
            #xgb_clf.fit(x_train,y_train)
            return l_r
            
        except Exception as e:
            raise SensorException(e,sys)



        
        
    def initiate_model_trainer(self,)->ModelTrainerArtifact:
        try:

            #first, load the transformed data as numpy array
            train_file_path= self.data_transformation_artifact.transformed_train_file_path
            test_file_path = self.data_transformation_artifact.transformed_test_file_path
            train_arr= load_numpy_array_data(file_path=train_file_path)
            test_arr = load_numpy_array_data(file_path=test_file_path)


            #split the data as input and target features
            x_train, y_train, x_test, y_test = (
                train_arr[:, :-1],
                train_arr[:, -1],
                test_arr[:, :-1],
                test_arr[:, -1],
            )

            # then train the model:

            model= self.train_model(x_train=x_train,y_train=y_train)
            y_train_pred = model.predict(x_train)
            classificatation_train_metric = get_classification_score(y_true=y_train , y_pred= y_train_pred )
            if classificatation_train_metric.f1_score < self.model_trainer_config.expected_accuracy:
                logging.info("expected accuracy is not satisfied")
                raise Exception("expected accuracy is not satisfied, try to do more Experimentation")
            
            y_test_pred = model.predict(x_test)
            classificatation_test_metric = get_classification_score(y_true=y_test , y_pred= y_test_pred )


            #check OVERFITTING and UNDERFITTING
            diff = abs(classificatation_train_metric.f1_score-classificatation_test_metric.f1_score)

            if diff >self.model_trainer_config.over_under_threshold:
                logging.info("OVERFITTING OR UNDERFITTING may occur, try to do more Experimentation")
                raise Exception("OVERFITTING OR UNDERFITTING may occur, try to do more Experimentation")


            #save the model

            model_dir_path = os.path.dirname(self.model_trainer_config.trained_model_file_path)
            os.makedirs(model_dir_path,exist_ok=True)
            preprocessor = load_object(file_path=self.data_transformation_artifact.transformed_object_file_path)
            sensor_model = SensorModel(preprocessor=preprocessor,model=model) # save for model versioning
            save_object(file_path=self.model_trainer_config.trained_model_file_path,obj=sensor_model) 

            # model trainer artifact 
            model_trainer_artifact = ModelTrainerArtifact(trained_model_file_path=self.model_trainer_config.trained_model_file_path,
                                 train_metric_artifact= classificatation_train_metric,
                                 test_metric_artifact= classificatation_test_metric  )
            logging.info(f"model trainer artifact: {model_trainer_artifact}")
            return model_trainer_artifact

        except Exception as e:
            raise SensorException(e,sys)
        



