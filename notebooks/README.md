# Jupyter Notebooks

本目录包含所有学习示例的Jupyter Notebook交互式版本。

## 为什么使用Notebook？

Jupyter Notebook提供：
- 📊 **可视化**: 实时查看训练曲线、图像、结果
- 🔍 **交互式探索**: 逐步运行代码，检查中间结果
- 📝 **学习笔记**: 在代码旁边添加Markdown注释
- 🎯 **快速实验**: 修改参数立即看到效果

## 目录结构

```
notebooks/
├── 01_computer_vision/
│   ├── mnist_cnn.ipynb
│   ├── dogs_vs_cats.ipynb
│   ├── vgg16_transfer_learning.ipynb
│   └── vgg16_fine_tuning.ipynb
│
├── 02_nlp/
│   ├── text_vectorization.ipynb
│   ├── word_embedding.ipynb
│   └── imdb_sentiment.ipynb
│
├── 03_sequence_models/
│   ├── rnn_basics.ipynb
│   └── lstm_deep_dive.ipynb
│
├── 04_time_series/
│   ├── weather_exploration.ipynb
│   └── weather_forecasting.ipynb
│
└── 05_projects/
    ├── image_classification_project.ipynb
    └── text_classification_project.ipynb
```

## 快速开始

### 1. 安装Jupyter

```bash
pip install jupyter notebook
# 或使用JupyterLab
pip install jupyterlab
```

### 2. 启动Notebook服务器

```bash
# 在项目根目录
jupyter notebook

# 或使用JupyterLab
jupyter lab
```

浏览器会自动打开 `http://localhost:8888`

### 3. 打开Notebook

导航到 `notebooks/` 目录，选择想要学习的notebook。

## Notebook使用技巧

### 快捷键

| 快捷键 | 功能 |
|--------|------|
| `Shift + Enter` | 运行当前单元格并移到下一个 |
| `Ctrl + Enter` | 运行当前单元格 |
| `A` | 在上方插入单元格 |
| `B` | 在下方插入单元格 |
| `D + D` | 删除当前单元格 |
| `M` | 转换为Markdown单元格 |
| `Y` | 转换为代码单元格 |
| `Esc` | 命令模式 |
| `Enter` | 编辑模式 |

### 魔法命令

```python
# 显示执行时间
%time code_line
%%time
# code block

# 查看变量
%whos

# 加载外部脚本
%load ../computer_vision/mnist_cnn.py

# 运行外部脚本
%run ../computer_vision/mnist_cnn.py

# 绘图内联显示
%matplotlib inline

# 自动重载模块（开发时很有用）
%load_ext autoreload
%autoreload 2
```

### 可视化设置

```python
import matplotlib.pyplot as plt
import seaborn as sns

# 设置样式
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# 高分辨率图像
%config InlineBackend.figure_format = 'retina'

# 图像大小
plt.rcParams['figure.figsize'] = (12, 8)
```

## Notebook vs Python脚本

### 何时使用Notebook？
- ✅ 学习和探索
- ✅ 数据分析和可视化
- ✅ 原型开发
- ✅ 教学演示

### 何时使用Python脚本？
- ✅ 生产环境
- ✅ 批量训练
- ✅ 版本控制
- ✅ 自动化流程

## 从Python脚本创建Notebook

可以使用以下命令将Python脚本转换为Notebook：

```bash
# 安装转换工具
pip install jupytext

# 转换
jupytext --to notebook script.py
```

或者手动创建：
1. 创建新的Notebook
2. 复制Python代码到代码单元格
3. 添加Markdown说明
4. 运行并验证

## 学习建议

### 对于初学者
1. **按顺序学习**: 从01开始，逐步深入
2. **运行所有单元格**: 理解每一步的输出
3. **做笔记**: 在Markdown单元格记录理解和问题
4. **修改参数**: 尝试改变超参数，观察效果

### 对于进阶者
1. **对比实验**: 同时打开多个notebook对比方法
2. **混合使用**: 结合多个技术解决问题
3. **创建项目**: 使用05_projects/模板开始自己的项目

## GPU支持

### Google Colab（推荐）

免费GPU，无需配置：

1. 上传notebook到Google Drive
2. 右键 → 打开方式 → Google Colaboratory
3. 运行时 → 更改运行时类型 → GPU

连接GitHub仓库：
```
File → Open notebook → GitHub → 输入仓库URL
```

### 本地GPU配置

```bash
# 检查GPU
python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"

# 如果检测到GPU，TensorFlow会自动使用
```

## 常见问题

### Q: Kernel死掉怎么办？
A: 
- Kernel → Restart
- 检查内存使用（可能数据太大）
- 减小batch_size

### Q: 训练太慢怎么办？
A:
- 使用GPU（Colab或本地）
- 减少数据量
- 使用更小的模型

### Q: 无法导入模块？
A:
```python
import sys
sys.path.append('..')  # 添加项目根目录到路径
```

### Q: 如何保存训练好的模型？
A:
```python
# 在notebook中
model.save('../saved_models/my_model.h5')

# 下次加载
from keras.models import load_model
model = load_model('../saved_models/my_model.h5')
```

## 分享Notebook

### 导出为HTML
```bash
jupyter nbconvert --to html notebook.ipynb
```

### 导出为PDF
```bash
jupyter nbconvert --to pdf notebook.ipynb
```

### 分享到GitHub
- 确保清除输出（Kernel → Restart & Clear Output）
- 提交到仓库
- GitHub会自动渲染notebook

### 使用nbviewer
```
https://nbviewer.jupyter.org/github/kiwios/deep-learning-examples/blob/main/notebooks/path/to/notebook.ipynb
```

## 最佳实践

1. **保持简洁**: 每个notebook专注一个主题
2. **添加说明**: 用Markdown解释每个步骤
3. **清理输出**: 提交前清除大量输出
4. **设置随机种子**: 保证可复现性
5. **保存检查点**: 长时间训练要定期保存

## 模板结构

标准notebook结构：

```markdown
# 标题

## 1. 导入库和设置
- 导入必要的库
- 设置随机种子
- 配置可视化

## 2. 加载和探索数据
- 加载数据
- 数据可视化
- 统计信息

## 3. 数据预处理
- 标准化/归一化
- 划分数据集
- 数据增强

## 4. 构建模型
- 定义模型架构
- 编译模型
- 模型摘要

## 5. 训练模型
- 训练
- 可视化训练过程

## 6. 评估模型
- 测试集评估
- 可视化结果
- 错误分析

## 7. 结论和下一步
- 总结发现
- 改进方向
```

## 贡献

欢迎贡献新的notebook示例！请确保：
- 代码可运行
- 包含详细注释
- 清除不必要的输出
- 遵循模板结构

---

💡 **提示**: 从简单的notebook开始，逐步构建对深度学习的理解！
