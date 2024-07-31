import os
from heart_stroke.constant.training_pipeline import *
from heart_stroke.constant.s3_bucket import TRAINING_BUCKET_NAME
from pymongo import MongoClient # type: ignore
from dataclasses import dataclass
from datetime import datetime

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")


@dataclass
class TrainingPipelineConfig:
    pipeline_name: str = PIPELINE_NAME
    artifact_dir: str = os.path.join(ARTIFACT_DIR, TIMESTAMP)
    timestamp: str = TIMESTAMP


training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()


@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_INGESTION_DIR_NAME) # type: ignore
    feature_store_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR, FILE_NAME) # type: ignore
    training_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TRAIN_FILE_NAME) # type: ignore
    testing_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TEST_FILE_NAME) # type: ignore
    train_test_split_ratio: float = DATA_INGESTION_TRAIN_TEST_SPLIT_RATION # type: ignore
    collection_name: str = DATA_INGESTION_COLLECTION_NAME # type: ignore


@dataclass
class DataValidationConfig:
    data_validation_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_VALIDATION_DIR_NAME) # type: ignore
    drift_report_file_path: str = os.path.join(data_validation_dir, DATA_VALIDATION_DRIFT_REPORT_DIR, # type: ignore
                                               DATA_VALIDATION_DRIFT_REPORT_FILE_NAME) # type: ignore


@dataclass
class DataTransformationConfig:
    data_transformation_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_TRANSFORMATION_DIR_NAME) # type: ignore
    transformed_train_file_path: str = os.path.join(data_transformation_dir, DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR, # type: ignore
                                                    TRAIN_FILE_NAME.replace("csv", "npy"))
    transformed_test_file_path: str = os.path.join(data_transformation_dir, DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR, # type: ignore
                                                   TEST_FILE_NAME.replace("csv", "npy"))
    transformed_object_file_path: str = os.path.join(data_transformation_dir,
                                                     DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR, # type: ignore
                                                     PREPROCSSING_OBJECT_FILE_NAME)


@dataclass
class ModelTrainerConfig:
    model_trainer_dir: str = os.path.join(training_pipeline_config.artifact_dir, MODEL_TRAINER_DIR_NAME) # type: ignore
    trained_model_file_path: str = os.path.join(model_trainer_dir, MODEL_TRAINER_TRAINED_MODEL_DIR, MODEL_FILE_NAME) # type: ignore
    expected_accuracy: float = MODEL_TRAINER_EXPECTED_SCORE # type: ignore
    model_config_file_path: str = MODEL_TRAINER_MODEL_CONFIG_FILE_PATH # type: ignore


@dataclass
class ModelEvaluationConfig:
    changed_threshold_score: float = MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE # type: ignore
    bucket_name: str = MODEL_PUSHER_BUCKET_NAME # type: ignore
    s3_model_key_path: str = "heart-stroke-model.pkl"


@dataclass
class ModelPusherConfig:
    bucket_name: str = MODEL_PUSHER_BUCKET_NAME # type: ignore
    s3_model_key_path: str = "heart-stroke-model.pkl"


@dataclass
class StrokePredictorConfig:
    model_file_path: str = "heart-stroke-model.pkl"
    model_bucket_name: str = TRAINING_BUCKET_NAME