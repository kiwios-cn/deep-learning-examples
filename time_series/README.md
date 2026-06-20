# 时间序列预测模块

本目录包含使用深度学习进行时间序列数据分析和预测的学习示例。

## 示例列表

### 1. 天气数据探索
**文件**: `weather.py`

学习时间序列数据的基本处理和可视化。

**技术点**:
- 时间序列数据加载
- 数据可视化
- 趋势分析
- 周期性模式识别
- 数据标准化

**数据集**: Jena气候数据集

---

### 2. 天气预测模型
**文件**: `weather_forecast.py`

使用RNN/LSTM进行多步时间序列预测。

**技术点**:
- 滑动窗口法构建训练数据
- 多变量时间序列处理
- LSTM时间序列预测
- 多步预测（Multi-step Forecasting）
- 模型评估指标（MAE、RMSE）
- Baseline对比

**数据集**: Jena气候数据集

**预测目标**: 预测未来温度

---

## 时间序列深度学习核心概念

### 数据准备

#### 滑动窗口
```python
# 使用过去24小时数据预测未来1小时
lookback = 24  # 回看窗口
delay = 1      # 预测步长
step = 1       # 采样间隔

# 示例：
# 输入: [t-24, t-23, ..., t-1, t]
# 输出: [t+1]
```

#### 数据标准化
时间序列数据通常需要标准化：
- **Z-score标准化**: (x - mean) / std
- **Min-Max标准化**: (x - min) / (max - min)
- **注意**: 只用训练集统计量标准化测试集

### 模型架构选择

| 模型类型 | 适用场景 | 优点 | 缺点 |
|---------|---------|------|------|
| **Dense** | 简单趋势 | 快速、简单 | 无时间记忆 |
| **1D CNN** | 局部模式 | 快速、并行 | 感受野有限 |
| **RNN** | 短期依赖 | 顺序处理 | 梯度消失 |
| **LSTM/GRU** | 长期依赖 | 记忆能力强 | 训练慢 |
| **Attention** | 复杂模式 | 可解释性好 | 计算复杂 |

### 评估指标

```python
# 平均绝对误差（MAE）
mae = mean(|y_true - y_pred|)

# 均方根误差（RMSE）
rmse = sqrt(mean((y_true - y_pred)^2))

# 平均绝对百分比误差（MAPE）
mape = mean(|y_true - y_pred| / |y_true|) * 100
```

### Baseline对比
建立简单基线模型很重要：
- **持久性模型**: 预测值 = 当前值
- **平均值模型**: 预测值 = 历史平均
- **线性趋势**: 简单线性回归

深度学习模型应该明显优于这些基线。

## 学习路径建议

1. **数据探索**: 从 `weather.py` 开始，理解时间序列数据特征
2. **建模预测**: 学习 `weather_forecast.py`，掌握深度学习预测方法
3. **对比实验**: 尝试不同模型架构（RNN vs LSTM vs GRU）
4. **调优**: 调整窗口大小、预测步长、模型参数

## 数据准备

### Jena气候数据集

从 [Max Planck Institute](https://www.bgc-jena.mpg.de/wetter/) 下载，或使用Kaggle版本。

```bash
# 下载并解压到data目录
mkdir -p /Users/fsr/worker/github/deep-learning-examples/data/jena_climate
# 将jena_climate_2009_2016.csv放入该目录
```

数据包含14个气象特征：
- 温度、气压、湿度、风速等
- 每10分钟采样一次
- 跨越2009-2016年

## 运行示例

```bash
# 数据探索
python weather.py

# 训练预测模型
python weather_forecast.py
```

## 常见时间序列任务

### 1. 单步预测
预测下一个时间点的值。
```
输入: [t-n, ..., t-1, t]
输出: [t+1]
```

### 2. 多步预测
预测未来多个时间点。
```
输入: [t-n, ..., t-1, t]
输出: [t+1, t+2, ..., t+m]
```

### 3. 序列到序列
输入输出都是序列。
```
输入: [t-n, ..., t-1, t]
输出: [t+1, t+2, ..., t+m]
```

## 实用技巧

### 1. 数据分割
```python
# 时间序列要按时间顺序分割，不能随机打乱
train = data[:int(0.7*len(data))]
val = data[int(0.7*len(data)):int(0.9*len(data))]
test = data[int(0.9*len(data)):]
```

### 2. 避免数据泄露
- 标准化参数只从训练集计算
- 验证集和测试集不参与任何训练决策

### 3. 处理缺失值
```python
# 前向填充
df.fillna(method='ffill')

# 线性插值
df.interpolate(method='linear')
```

### 4. 特征工程
- 时间特征：小时、星期、月份
- 滞后特征：前N个时间步的值
- 滚动统计：移动平均、移动标准差

## 扩展方向

- **Prophet**: Facebook开源的时间序列预测库
- **Transformer**: 用于时间序列的Attention机制
- **N-BEATS**: 专门的时间序列预测架构
- **AutoML**: 自动化时间序列建模

## 依赖环境

参见项目根目录的 `requirements.txt`。

## 参考资源

- [Time Series Forecasting with Deep Learning](https://machinelearningmastery.com/time-series-forecasting-with-deep-learning/)
- [Keras Time Series Examples](https://keras.io/examples/timeseries/)
- [Deep Learning for Time Series Forecasting](https://www.manning.com/books/deep-learning-for-time-series-forecasting)
- [Jena Climate Dataset](https://www.bgc-jena.mpg.de/wetter/)
