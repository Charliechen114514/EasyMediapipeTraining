from Env_Assertions.env_asserions import EnvAssertions, ModuleMissing, InvalidTensorVersion
from ParamsSettings import ModelParamsSetting, DICT_KEY
from ModelTraining.model_train import ModelTraining

# Check if the env is acceptable for running this issue
checking = EnvAssertions()
try:
    checking.check_params()
except ModuleMissing as e:
    print(str(e)) 
    exit(-1)
except InvalidTensorVersion as e:
    print(str(e))
    exit(-1)
except Exception as e:
    print(str(e))
    exit(-1)

# Initialize the settings
m = ModelParamsSetting()

# In train Settings
# you can modified things at here
train_params = m.gain_intrain_dict()
train_params[DICT_KEY.EPOCHS] = 20

# Out train settings
m.set_dataset_path("test_datas").set_split_param(8, 1, 1).\
    set_export_dirent("export_dir").set_model_name("hello")

# Do training
model_wrapper = ModelTraining()
res = model_wrapper.inject_settings(m).do_train()
