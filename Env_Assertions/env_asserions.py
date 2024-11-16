from Env_Assertions.env_assertions_impl \
    import NeccessaryPackageRequired, TensorFlowVersionChecker

class ModuleMissing(Exception):
    def __init__(self, err: str):
        self.msg = err
    
    def __str__(self):
        return self.msg

class InvalidTensorVersion(Exception):
    def __init__(self, err: str):
        self.msg = err
    
    def __str__(self):
        return self.msg

"""
    Env Assertions interface class
    Client programmers should call this and within a try-except format:
    
    env_assertion = EnvAssertions()
    try: 
        env_assertion.check_params()
    except ModuleMissing as e:
        ...
    except InvalidTensorVersion as e:
        ...
"""

class EnvAssertions:
    def __init__(self):
        self.__env_checker = NeccessaryPackageRequired()
        self.__tensorflow_checker = TensorFlowVersionChecker()
        
    def check_params(self) -> bool:
        if not self.__env_checker.checkParam():
            raise ModuleMissing(self.__env_checker.tell_invalid_how())
        if not self.__tensorflow_checker.checkParam():
            raise InvalidTensorVersion(self.__tensorflow_checker.tell_invalid_how())