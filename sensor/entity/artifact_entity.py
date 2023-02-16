from dataclasses import dataclass

<<<<<<< HEAD
@dataclass
class DataIngestionArtifact:
    pass

=======
class DataIngestitionArtifact :
    feature_store_file_path :str
    train_file_path :str
    test_file_path :str
    
>>>>>>> be249c909a356d8213942c1c19f72c3b9c719dd4

class DataValidationArtifact :...
class DataTransformationArtifact :...
class ModelTrainerArtifact:...
class ModelEvaluationArtifact:...
class ModelPusherArtifact :...
