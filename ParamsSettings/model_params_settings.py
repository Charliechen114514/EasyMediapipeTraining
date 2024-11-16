# Import the tensorflow for checking the version
import tensorflow as tf
import os
from ParamsSettings.DICT_KEY import *
from .fraction_creator import FractionOfDataset

class ModelParamsSetting:
    DEF_MODEL_NAME = "gesture_recognizer.task"
    def __init__(self):
        self.__dataSplit = FractionOfDataset()
        self.__dataset_base_path = ""
        self.__export_dir = None
        self.__model_name = ModelParamsSetting.DEF_MODEL_NAME
        # this are in train dict current_exposed
        self.__train_dict = {
            BATCH_SIZE: 2,
            LEARN_RATE: 0.001,
            EPOCHS: 10,
        }

    def __str__(self):
        return \
            f"Datapath at:> {self.__dataset_base_path}\nTrain Validate " \
                "Test percentage:> {}".format(str(self.__dataSplit)) + \
            f"Export dirent_name: {self.__export_dir} \n" + \
            f"Export model_name: {self.__model_name}\n" + \
            str(self.__train_dict)

    def gain_intrain_dict(self) -> dict:
        return self.__train_dict

    """
        Following method is gpu related, if one only care if gpu is accessible
        call this
    """
    @staticmethod
    def is_gpu_accessible() -> bool:
        return tf.config.list_physical_devices('GPU')

    """ fuck some shit lib who don't expose the context/class meta info """

    """
        Following method is gpu related, if one care how and what gpu are availible 
        in this device, use this.
        interfaces are provided by tensorflow :)
    """
    @staticmethod
    def gpu_list():
        return tf.config.list_physical_devices('GPU')

    """
        Why list? it's a pity that py at 3.8 is not support list[str] as returned...
    """
    def try_gathering_labels(self) -> list:
        if not os.path.isdir(self.__dataset_base_path):
            raise FileNotFoundError("Using a dir path not exists!")
        labels:list[str] = []
        for i in os.listdir(self.__dataset_base_path):
            if os.path.isdir(os.path.join(self.__dataset_base_path, i)):
                labels.append(i)
        return labels

    def set_export_dirent(self, path: str):
        self.__export_dir = path
        return self

    def set_model_name(self, model_name: str):
        self.__model_name = model_name
        return self

    def set_dataset_path(self, path: str):
        test_dir = os.path.abspath(path)
        if not os.path.isdir(test_dir):
            raise FileNotFoundError("Using a dir path not exists!")

        self.__dataset_base_path = test_dir
        labels = self.try_gathering_labels()
        if labels.count("None") == 0:
            raise ValueError("The dataset must contain None as the fallback!")
        return self

    def set_split_param(self, train: int=FractionOfDataset.DEF_TRAIN_FRAC, \
                        validation: int=FractionOfDataset.DEF_VALID_FRAC, \
                        test: int=FractionOfDataset.DEF_TEST_FRAC):
        self.__dataSplit.set_split_param(train=train, validation=validation, test=test)
        self.__dataSplit.check_params()
        return self
    
    def fetch_savings(self) -> dict:
        per = self.__dataSplit.transform_to_mediapipe()
        return {
            DATASET_PATH: self.__dataset_base_path,
            PER1: per[0],
            PER2: per[1],
            EXPORT_DIR: self.__export_dir,
            MODEL_NAME: self.__model_name
        }

    def validate_settings(self):
        if not os.path.isdir(self.__dataset_base_path): 
            raise FileNotFoundError("Using a dir path not exists!")
        labels = self.try_gathering_labels()
        if labels.count("None") == 0:
            raise ValueError("The dataset must contain None as a fallback!")
        if self.__export_dir is None:
            raise ValueError("Forget to set a dirent name!")
        if self.__model_name == "":
            raise ValueError("Model name empty, can not make settings!")

