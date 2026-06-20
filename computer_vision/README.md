# 计算机视觉模块

本目录包含使用深度学习进行图像分类和识别的学习示例。

## 示例列表

### 1. MNIST手写数字识别
**文件**: `minst_convent.py`

使用卷积神经网络（CNN）识别手写数字，这是深度学习入门的经典案例。

**技术点**:
- Conv2D 卷积层
- MaxPooling2D 池化层
- Dropout 防止过拟合
- 多类别分类

**数据集**: MNIST (Keras内置)

---

### 2. 猫狗分类 - 基础版
**文件**: `dogs_vs_cats.py`

从零开始训练简单的CNN模型进行二分类。

**技术点**:
- 数据增强（ImageDataGenerator）
- 二分类问题
- 基础CNN架构

**数据集**: Kaggle Dogs vs Cats

---

### 3. 猫狗分类 - 标准模型
**文件**: `dog_vs_cats_model.py`

更深层的CNN架构，包含数据增强和正则化。

**技术点**:
- 更深的网络结构
- BatchNormalization
- 数据增强策略
- 模型保存与加载

---

### 4. 猫狗分类 - 改进版
**文件**: `improved_dogs_vs_cats_model.py`

在标准模型基础上进行优化改进。

**技术点**:
- 学习率调整
- 早停机制
- 更强的正则化

---

### 5. VGG16迁移学习
**文件**: `vgg16.py`

使用预训练的VGG16模型进行特征提取。

**技术点**:
- 迁移学习基础
- 预训练模型使用
- 特征提取
- 在小数据集上的应用

**预训练模型**: VGG16 (ImageNet)

---

### 6. VGG16冻结层微调
**文件**: `freezing_vgg16.py`

冻结VGG16的部分层，只训练顶层分类器。

**技术点**:
- 层冻结（Freezing）
- 微调（Fine-tuning）
- 迁移学习高级技巧
- 防止过拟合

**预训练模型**: VGG16 (ImageNet)

---

## 学习路径建议

1. **入门**: 从 `minst_convent.py` 开始，理解CNN基本结构
2. **进阶**: 学习 `dogs_vs_cats.py` → `dog_vs_cats_model.py` → `improved_dogs_vs_cats_model.py`，了解模型优化过程
3. **高级**: 学习 `vgg16.py` → `freezing_vgg16.py`，掌握迁移学习

## 数据准备

### MNIST
无需下载，Keras会自动加载。

### Dogs vs Cats
从 [Kaggle](https://www.kaggle.com/c/dogs-vs-cats) 下载数据集，解压到 `data/dogs-vs-cats/` 目录：

```
data/dogs-vs-cats/
├── train/
│   ├── cat/
│   └── dog/
└── validation/
    ├── cat/
    └── dog/
```

## 运行示例

```bash
# MNIST示例
python minst_convent.py

# 猫狗分类（需要先准备数据）
python dogs_vs_cats.py

# VGG16迁移学习
python vgg16.py
```

## 依赖环境

参见项目根目录的 `requirements.txt`。

## 参考资源

- [Deep Learning with Python](https://www.manning.com/books/deep-learning-with-python) - François Chollet
- [CS231n: CNN for Visual Recognition](http://cs231n.stanford.edu/)
- [Keras Computer Vision Examples](https://keras.io/examples/vision/)
