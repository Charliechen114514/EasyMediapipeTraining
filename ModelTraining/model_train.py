from ParamsSettings import ModelParamsSetting, DICT_KEY
from google.colab import files
from mediapipe_model_maker import gesture_recognizer
from contextlib import suppress

import os
class ModelTraining:
    def __init__(self):
        self.__settings = None

    def inject_settings(self, settings: ModelParamsSetting):
        self.__settings = settings
        return self

    def check_params(self):
        if self.__settings is None:
            raise ValueError("settings or export dir is not set, check the settings")
        self.__settings.validate_settings()

    def do_train(self) -> list:
        self.check_params()

        result = self.__settings.fetch_savings()
        dataset_path = result[DICT_KEY.DATASET_PATH]
        per1 = result[DICT_KEY.PER1]
        per2 = result[DICT_KEY.PER2]
        export_dir = result[DICT_KEY.EXPORT_DIR]
        model_name = result[DICT_KEY.MODEL_NAME] + ".task"
        in_train_settings = self.__settings.gain_intrain_dict()
        epoch = in_train_settings[DICT_KEY.EPOCHS]
        batch_sz = in_train_settings[DICT_KEY.BATCH_SIZE]
        learn_rate = in_train_settings[DICT_KEY.LEARN_RATE]

        data = gesture_recognizer.Dataset.from_folder(
            dirname=dataset_path,
            hparams=gesture_recognizer.HandDataPreprocessingParams()
        )

        train_data, rest_data = data.split(per1)
        validation_data, test_data = rest_data.split(per2)
        hparams = gesture_recognizer.HParams(export_dir=export_dir)
        
        # Register intrain values
        hparams.batch_size = batch_sz
        hparams.epochs = epoch
        hparams.learning_rate = learn_rate

        options = gesture_recognizer.GestureRecognizerOptions(hparams=hparams)
        model = gesture_recognizer.GestureRecognizer.create(
            train_data=train_data,
            validation_data=validation_data,
            options=options
        )

        loss, acc = model.evaluate(test_data, batch_size=1)
        model.export_model()
        print(os.path.join(export_dir, model_name))
        # try:
        #     files.download(os.path.join(self.__export_dir, self.__model_name))
        # except Exception as e:
        #     print("I Fucking know i am not in IPython, \
        #           but I really need the task file:)")
        with suppress(Exception):
            files.download(os.path.join(export_dir, model_name))
            print("I Fucking know i am not in IPython, \
                   but I really need the task file:)")
        res = []
        res.append(loss)
        res.append(acc)
        return res