# Import ABC for common methods
from abc import ABC, abstractmethod
# Import the tensorflow for checking the version
import tensorflow as tf

"""
    This block is used for block assertions
    including tensorflow version check and 
    some neccess lib check
"""
"""
    Base for all the params checkings
"""
class ParamCheckerBase(ABC):
    """
        Virtual Params Checker, each check must tell if params 
        is valid, else we dont!
    """
    @abstractmethod
    def checkParam(self) -> bool:
        pass

    """
        Virtual Error Broadcaster, tell the error and fetch the string!
    """
    @abstractmethod
    def tell_invalid_how(self) -> str:
        pass

class NeccessaryPackageRequired(ParamCheckerBase):
    def __init__(self):
        super().__init__()
        self.__error_str_import = ""

    def checkParam(self) ->bool:
        """ try google colab """
        test_flag = True
        try:
            from google.colab import files
        except ImportError as e:
            self.__error_str_import += str(e) + "\n"
            test_flag = False
        
        """ try tensorflow """
        try:
            import tensorflow
        except ImportError as e:
            self.__error_str_import += str(e) + "\n"
            test_flag = False

        """ try mediapipe """
        try:
            from mediapipe_model_maker import gesture_recognizer
        except ImportError as e:
            self.__error_str_import += str(e) + "\n"
            test_flag = False
        
        if self.__error_str_import != "":
            self.__error_str_import += "This modules are missing, try pip install them!\n"
        return test_flag

    def tell_invalid_how(self) -> str:
        return self.__error_str_import

"""
    In current mediapipe, it only requires the Tensorflow
"""
class TensorFlowVersionChecker(ParamCheckerBase):
    def __init__(self):
        super().__init__()

    def checkParam(self) ->bool:
        return tf.__version__.startswith('2')

    def tell_invalid_how(self) -> str:
        return "Tensorflow version is invalid, it should be at Major verison 2 at least"


