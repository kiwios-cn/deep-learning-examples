# Deep Learning Examples

深度学习学习示例集合，涵盖计算机视觉、自然语言处理、序列模型和时间序列预测。

## 项目简介

这是一个系统化的深度学习学习项目，包含从基础到进阶的各类实战示例。所有代码使用 Keras/TensorFlow 实现，配有详细的中文注释和说明文档。

## 目录结构

```
deep-learning-examples/
├── computer_vision/        # 计算机视觉
│   ├── minst_convent.py           # MNIST手写数字识别
│   ├── dogs_vs_cats.py            # 猫狗分类基础版
│   ├── dog_vs_cats_model.py       # 猫狗分类标准模型
│   ├── improved_dogs_vs_cats_model.py  # 猫狗分类改进版
│   ├── vgg16.py                   # VGG16迁移学习
│   ├── freezing_vgg16.py          # VGG16冻结层微调
│   └── README.md
├── nlp/                    # 自然语言处理
│   ├── one_hot.py                 # One-Hot编码
│   ├── word_embedding.py          # 词嵌入
│   ├── imdb.py                    # IMDB情感分析
│   └── README.md
├── sequence_models/        # 序列模型
│   ├── RNN.py                     # 循环神经网络
│   ├── LSTM.py                    # 长短期记忆网络
│   └── README.md
├── time_series/           # 时间序列预测
│   ├── weather.py                 # 天气数据探索
│   ├── weather_forecast.py        # 天气预测模型
│   └── README.md
├── notebooks/             # Jupyter笔记本版本
├── data/                  # 数据目录（不提交到Git）
│   ├── dogs-vs-cats/
│   ├── glove/
│   └── jena_climate/
├── tests/                 # 测试代码
├── requirements.txt       # 依赖包
├── .gitignore
├── LICENSE
└── README.md
```

## 学习路径

### 🎯 初学者路径（2-3周）

1. **第一周：深度学习基础**
   - `computer_vision/minst_convent.py` - CNN入门
   - `nlp/one_hot.py` - 文本向量化基础
   - `sequence_models/RNN.py` - 序列模型入门

2. **第二周：经典应用**
   - `computer_vision/dogs_vs_cats.py` - 图像分类实战
   - `nlp/word_embedding.py` - 词嵌入深入理解
   - `time_series/weather.py` - 时间序列数据探索

3. **第三周：高级技巧**
   - `computer_vision/vgg16.py` - 迁移学习
   - `nlp/imdb.py` - NLP完整流程
   - `sequence_models/LSTM.py` - 长期依赖处理

### 🚀 进阶路径（3-4周）

4. **第四周：模型优化**
   - `computer_vision/improved_dogs_vs_cats_model.py` - 模型调优
   - `computer_vision/freezing_vgg16.py` - 微调技巧
   - `time_series/weather_forecast.py` - 实际预测任务

5. **第五周：项目实战**
   - 选择一个领域深入，完成端到端项目
   - 尝试在自己的数据集上应用学到的技术

## 技术栈

- **深度学习框架**: TensorFlow 2.x / Keras
- **数据处理**: NumPy, Pandas
- **可视化**: Matplotlib, Seaborn
- **Python版本**: 3.8+

## 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/kiwios/deep-learning-examples.git
cd deep-learning-examples
```

### 2. 创建虚拟环境

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 准备数据

大部分示例使用Keras内置数据集，无需手动下载。对于需要外部数据的示例：

#### Dogs vs Cats 数据集
从 [Kaggle](https://www.kaggle.com/c/dogs-vs-cats) 下载，解压到 `data/dogs-vs-cats/`

#### GloVe 词向量
从 [Stanford NLP](https://nlp.stanford.edu/projects/glove/) 下载 `glove.6B.zip`，解压到 `data/glove/`

#### Jena 气候数据集
从 [Kaggle](https://www.kaggle.com/datasets/mnassrib/jena-climate) 下载，放入 `data/jena_climate/`

详细数据准备说明请查看各模块的README。

### 5. 运行示例

```bash
# 计算机视觉 - MNIST
python computer_vision/minst_convent.py

# 自然语言处理 - 情感分析
python nlp/imdb.py

# 序列模型 - LSTM
python sequence_models/LSTM.py

# 时间序列 - 天气预测
python time_series/weather_forecast.py
```

## 核心概念覆盖

### 深度学习基础
- ✅ 神经网络基本结构
- ✅ 反向传播与梯度下降
- ✅ 损失函数与优化器
- ✅ 过拟合与正则化

### 计算机视觉
- ✅ 卷积神经网络（CNN）
- ✅ 数据增强
- ✅ 迁移学习
- ✅ 预训练模型使用
- ✅ 微调（Fine-tuning）

### 自然语言处理
- ✅ 文本向量化（One-Hot、Embedding）
- ✅ 词嵌入（Word Embedding）
- ✅ 预训练词向量（GloVe）
- ✅ 情感分析

### 序列模型
- ✅ 循环神经网络（RNN）
- ✅ 长短期记忆网络（LSTM）
- ✅ 门控循环单元（GRU）
- ✅ 序列到序列学习

### 时间序列
- ✅ 时间序列数据处理
- ✅ 多步预测
- ✅ 多变量时间序列
- ✅ 模型评估指标

## 最佳实践

### 代码风格
- 遵循PEP 8规范
- 函数和变量使用英文命名
- 注释和文档使用中文

### 模型训练
- 始终设置随机种子保证可复现性
- 使用验证集进行模型选择
- 保存最佳模型检查点
- 记录训练日志

### 数据处理
- 训练/验证/测试集严格分离
- 标准化只使用训练集统计量
- 注意数据泄露问题

## 性能基准

在标准数据集上的参考性能：

| 数据集 | 任务 | 准确率/指标 | 模型 |
|--------|------|------------|------|
| MNIST | 手写数字识别 | ~99% | CNN |
| IMDB | 情感分析 | ~88% | LSTM |
| Dogs vs Cats | 二分类 | ~85% | 基础CNN |
| Dogs vs Cats | 二分类 | ~95% | VGG16微调 |

## 常见问题

### Q: 需要GPU吗？
A: 不是必须的。小模型在CPU上几分钟即可训练完成。对于大型模型（如VGG16微调），建议使用GPU。

### Q: 内存不足怎么办？
A: 减小batch_size，或使用数据生成器（generator）逐批加载数据。

### Q: 训练太慢怎么办？
A: 
- 减少训练轮数（epochs）
- 减小模型规模
- 使用预训练模型
- 使用GPU训练

### Q: 模型过拟合怎么办？
A: 
- 增加数据（数据增强）
- 添加Dropout层
- 使用正则化（L1/L2）
- 减小模型复杂度
- 早停（Early Stopping）

## 贡献指南

欢迎提交Issue和Pull Request！

- 报告Bug
- 提出新示例建议
- 改进文档
- 优化代码

## 学习资源

### 书籍
- 《Python深度学习》- François Chollet
- 《深度学习》- Ian Goodfellow
- 《动手学深度学习》- 李沐

### 在线课程
- [Deep Learning Specialization](https://www.coursera.org/specializations/deep-learning) - Andrew Ng
- [CS231n: CNN for Visual Recognition](http://cs231n.stanford.edu/)
- [CS224n: NLP with Deep Learning](http://web.stanford.edu/class/cs224n/)

### 官方文档
- [Keras Documentation](https://keras.io/)
- [TensorFlow Tutorials](https://www.tensorflow.org/tutorials)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)

## 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 作者

kiwios - [GitHub](https://github.com/kiwios)

## 致谢

感谢以下资源和社区：
- Keras团队提供的优秀深度学习框架
- François Chollet的《Python深度学习》
- Kaggle提供的数据集
- 深度学习开源社区

---

⭐ 如果这个项目对你有帮助，欢迎Star支持！

📧 问题和建议请提交Issue或通过邮件联系。
