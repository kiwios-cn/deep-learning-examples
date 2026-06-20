# 自然语言处理模块

本目录包含使用深度学习进行文本处理和情感分析的学习示例。

## 示例列表

### 1. One-Hot编码
**文件**: `one_hot.py`

学习文本的基础向量化方法 - One-Hot编码。

**技术点**:
- 字符级One-Hot编码
- 单词级One-Hot编码
- Keras内置One-Hot工具
- 稀疏表示与密集表示

**适用场景**: 理解文本数值化的基本原理

---

### 2. 词嵌入（Word Embedding）
**文件**: `word_embedding.py`

学习使用Embedding层将单词映射到密集向量空间。

**技术点**:
- Embedding层使用
- 从头训练词向量
- 使用预训练词向量（GloVe）
- 词向量可视化
- 相似度计算

**预训练模型**: GloVe

---

### 3. IMDB情感分析
**文件**: `imdb.py`

使用RNN/LSTM进行电影评论情感分类。

**技术点**:
- 文本序列处理
- Embedding + LSTM架构
- 二分类情感分析
- 序列填充（padding）
- Dropout防止过拟合

**数据集**: IMDB电影评论（Keras内置）

---

## 学习路径建议

1. **基础**: `one_hot.py` - 理解文本如何转换为数字
2. **进阶**: `word_embedding.py` - 学习词向量的强大表示能力
3. **应用**: `imdb.py` - 将词嵌入应用于实际NLP任务

## 数据准备

### IMDB数据集
无需下载，Keras会自动加载。

### GloVe预训练词向量
从 [Stanford NLP](https://nlp.stanford.edu/projects/glove/) 下载，例如 `glove.6B.zip`，解压到 `data/glove/` 目录：

```
data/glove/
└── glove.6B.100d.txt
```

## 运行示例

```bash
# One-Hot编码示例
python one_hot.py

# 词嵌入示例
python word_embedding.py

# IMDB情感分析
python imdb.py
```

## 核心概念

### One-Hot编码
- 优点：简单直观
- 缺点：维度高、稀疏、无法表示语义相似度

### 词嵌入
- 优点：密集表示、捕捉语义、维度可控
- 缺点：需要大量数据训练或使用预训练模型

### 预训练词向量
常用模型：
- **GloVe**: 基于全局词共现统计
- **Word2Vec**: 基于局部上下文窗口
- **FastText**: 支持子词信息

## 依赖环境

参见项目根目录的 `requirements.txt`。

## 参考资源

- [Deep Learning for NLP](https://www.manning.com/books/deep-learning-with-python) - François Chollet
- [CS224n: NLP with Deep Learning](http://web.stanford.edu/class/cs224n/)
- [GloVe: Global Vectors for Word Representation](https://nlp.stanford.edu/projects/glove/)
