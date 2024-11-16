# Mediapipe Training Wrapper

## Introduction

​ This is a simple wrapper library that encapsulates the Mediapipe hand recognition training process

```
.
├── Env_Assertions # Environment detection
├── ModelTraining # Model training
├── ParamsSettings # Parameter settings
├── README.md # You are here!
├── raw # Native ipynb file
├── example_usage.py # A sample usage
└── test # Test, completed with Pytest (but lazy, only tested frac allocation)
```

## How to build the environment

```
pip install mediapipe-model-maker
```

​ Just one sentence! The basic environment will be installed

​ If you are building on WSL, you can refer to the article: [Using miniconda + cuda + cudnn scheme for machine/deep learning environment configuration scheme_wsl2 machine learning-CSDN blog](https://blog.csdn.net/charlie114514191/article/details/142834787?ops_request_misc=%7B%22request%5Fid%22%3A%22357FA295-1C50-4849-BE50-C49642FAA686%22%2C%22scm%22%3A%2220140713.130102334.pc%5Fbl og.%22%7D&request_id=357FA295-1C50-4849-BE50-C49642FAA686&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-142834787-null-null. nonecase&utm_term=WSL&spm=1018.2226.3001.4450) ## Example of use

### How to use

​ You need to provide three-channel color images of the same file level as the dataset sample given in the mediapipe document, as follows:

```
Base
|-Label1
|-PicI
|...
|-Label2
|-PicI
|...
```

​ BaseDir is required to be at the same level as the project root directory. Replace it with the dataset root directory you want in the sample.

### Architecture description

​ Refer to the example_usage.py program. As a complete test, you first need to instantiate an Env_Assertions object and call the check_params method for testing, and you need to accept exception handling to prevent program avalanche.

​ Secondly, use the interface class ModelParamsSetting to set parameters during training and export parameters, etc. For details, refer to the sample file (it is worth mentioning that you can call it in a chain, which makes writing code a little easier)

​ Finally, use the wrapper class ModelTraining to inject an instance object of our ModelParamsSetting into it. The model will parse ModelParamsSetting to get the necessary parameters. Don't worry, most parameters will be checked.

## Some notes

1. After the author finished packaging, I found that mediapipe must be run under the ipynb file to export the mediapipe with a **custom name**. If you have such a requirement, please run the model_train.ipynb file under raw directly in the jupyter notebook after passing the environment check

2. No more, enjoy!