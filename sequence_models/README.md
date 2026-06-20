# 序列模型模块

本目录包含循环神经网络（RNN）和长短期记忆网络（LSTM）的学习示例。

## 示例列表

### 1. 循环神经网络（RNN）
**文件**: `RNN.py`

学习RNN的基本原理和实现。

**技术点**:
- SimpleRNN层使用
- 序列数据处理
- 时间步概念
- 梯度消失问题演示
- return_sequences参数理解

**应用场景**: 
- 文本生成
- 序列预测
- 时间序列分析

---

### 2. 长短期记忆网络（LSTM）
**文件**: `LSTM.py`

学习LSTM如何解决RNN的长期依赖问题。

**技术点**:
- LSTM层使用
- 遗忘门、输入门、输出门机制
- 细胞状态（Cell State）
- 处理长序列
- 双向LSTM（Bidirectional）

**应用场景**:
- 机器翻译
- 语音识别
- 长文本分析
- 时间序列预测

---

## RNN vs LSTM 对比

| 特性 | RNN | LSTM |
|------|-----|------|
| **结构复杂度** | 简单 | 复杂（包含3个门） |
| **长期依赖** | 难以处理 | 可以处理 |
| **梯度消失** | 严重 | 有效缓解 |
| **训练速度** | 快 | 较慢 |
| **参数数量** | 少 | 多（约4倍RNN） |
| **适用场景** | 短序列 | 长序列 |

## 核心概念

### RNN工作原理
```
x_t → [RNN Cell] → h_t
        ↑     ↓
      h_(t-1)
```
- 每个时间步共享权重
- 前一时刻的隐藏状态影响当前输出

### LSTM门控机制
1. **遗忘门**: 决定丢弃哪些信息
2. **输入门**: 决定更新哪些信息
3. **输出门**: 决定输出什么

### 常见问题

**Q: 什么时候用RNN？**
A: 序列较短（<50步）、计算资源有限、问题简单时。

**Q: 什么时候用LSTM？**
A: 需要记忆长期依赖、序列较长、复杂任务时。

**Q: return_sequences参数作用？**
A: 
- `False`: 只返回最后时间步输出（用于分类）
- `True`: 返回所有时间步输出（用于序列到序列）

## 学习路径建议

1. **基础**: 先学习 `RNN.py`，理解循环结构和时间步概念
2. **进阶**: 学习 `LSTM.py`，理解如何解决长期依赖问题
3. **对比**: 在相同任务上对比RNN和LSTM的表现差异
4. **应用**: 到 `time_series/` 查看实际应用案例

## 运行示例

```bash
# RNN基础示例
python RNN.py

# LSTM示例
python LSTM.py
```

## 扩展学习

### 其他序列模型
- **GRU** (Gated Recurrent Unit): LSTM的简化版本，参数更少
- **Bidirectional LSTM**: 双向处理序列，同时考虑过去和未来
- **Attention机制**: 让模型关注序列中的重要部分

### 实际应用示例
查看其他模块：
- `nlp/imdb.py`: 使用LSTM进行情感分析
- `time_series/`: 使用RNN/LSTM进行时间序列预测

## 依赖环境

参见项目根目录的 `requirements.txt`。

## 参考资源

- [Understanding LSTM Networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/) - Chris Olah
- [The Unreasonable Effectiveness of RNN](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) - Andrej Karpathy
- [Keras RNN Guide](https://keras.io/guides/working_with_rnns/)
- [Deep Learning Book - Sequence Modeling](https://www.deeplearningbook.org/contents/rnn.html)
