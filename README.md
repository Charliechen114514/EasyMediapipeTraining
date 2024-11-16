# Mediapipe Training Wrapper

## 介绍

​	这是一个封装了Mediapipe手部识别训练流程的简单Wrapper库

```
.
├── Env_Assertions  # 环境检测
├── ModelTraining   # 模型训练
├── ParamsSettings  # 参数设置
├── README.md		# 你在这里！
├── raw				# 原生的ipynb文件
├── example_usage.py #一个样例使用
└── test			# 测试，使用Pytest完成（但是偷懒了，只测试了frac分配）
```

## 如何构建环境

```
pip install mediapipe-model-maker
```

​	一句话即可！基本的环境都会安装

​	如果您是在WSL上进行构建的，您可以参考文章：[WSL2下使用miniconda + cuda + cudnn方案进行机器/深度学习环境配置方案_wsl2机器学习-CSDN博客](https://blog.csdn.net/charlie114514191/article/details/142834787?ops_request_misc=%7B%22request%5Fid%22%3A%22357FA295-1C50-4849-BE50-C49642FAA686%22%2C%22scm%22%3A%2220140713.130102334.pc%5Fblog.%22%7D&request_id=357FA295-1C50-4849-BE50-C49642FAA686&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-142834787-null-null.nonecase&utm_term=WSL&spm=1018.2226.3001.4450)

## 使用范例

### 如何使用

​	你需要按照mediapipe文档给出的数据集样例那样，提供相同文件层级的的三通道彩色图像，如下：

```
Base
|-Label1
	|-PicI
	|...
|-Label2
	|-PicI
	|...
```

​	其中BaseDir要求跟项目根目录同级。在样例中替换成您希望的数据集根目录即可。

### 架构说明

​	参考example_usage.py程序，作为一个完整的检测，您首先需要实例化一个Env_Assertions对象调用check_params方法进行检测，且需要接受异常处理防止程序的雪崩。

​	其次是使用接口类ModelParamsSetting，设置训练时参数和导出参数等，详情参考示例文件（值得一提的是您可以链式调用，让写代码稍稍轻松一些）

​	最后是使用包装类ModelTraining，向内注入我们的ModelParamsSetting的一个实例对象，模型将会解析ModelParamsSetting得到必备的参数。不必担心，大部分的参数都会受到检查。

## 一些注意

1. 笔者包装完毕后，发现mediapipe必须跑在ipynb文件下，才能导出**自定义名称**的mediapipe，如果您有这样的需求，请通过环境检查后直接在jupyter notebook中运行raw下方的model_train.ipynb文件
2. 没有了,enjoy!

