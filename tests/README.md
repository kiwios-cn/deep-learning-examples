# Tests

本目录包含项目的单元测试和集成测试。

## 测试结构

```
tests/
├── test_computer_vision.py    # 计算机视觉模块测试
├── test_nlp.py                 # NLP模块测试
├── test_sequence_models.py     # 序列模型测试
├── test_time_series.py         # 时间序列测试
├── conftest.py                 # pytest配置和fixtures
└── README.md
```

## 运行测试

### 运行所有测试
```bash
pytest tests/
```

### 运行特定模块测试
```bash
pytest tests/test_computer_vision.py
pytest tests/test_nlp.py
```

### 运行特定测试函数
```bash
pytest tests/test_computer_vision.py::test_model_architecture
```

### 生成覆盖率报告
```bash
pytest tests/ --cov=./ --cov-report=html
# 查看报告：open htmlcov/index.html
```

### 详细输出
```bash
pytest tests/ -v
pytest tests/ -vv  # 更详细
```

## 测试类型

### 1. 单元测试
测试单个函数和类的功能。

```python
def test_data_preprocessing():
    """测试数据预处理函数"""
    data = np.array([1, 2, 3, 4, 5])
    normalized = normalize(data)
    assert normalized.mean() == pytest.approx(0, abs=1e-5)
    assert normalized.std() == pytest.approx(1, abs=1e-5)
```

### 2. 模型架构测试
验证模型结构正确性。

```python
def test_cnn_architecture():
    """测试CNN模型架构"""
    model = build_cnn_model(input_shape=(28, 28, 1), num_classes=10)
    assert len(model.layers) == 8
    assert model.input_shape == (None, 28, 28, 1)
    assert model.output_shape == (None, 10)
```

### 3. 训练测试
快速训练测试（小数据、少轮次）。

```python
def test_model_training():
    """测试模型能否正常训练"""
    x_train = np.random.rand(100, 28, 28, 1)
    y_train = np.random.randint(0, 10, 100)
    
    model = build_model()
    history = model.fit(x_train, y_train, epochs=2, verbose=0)
    
    assert 'loss' in history.history
    assert len(history.history['loss']) == 2
```

### 4. 推理测试
测试模型预测功能。

```python
def test_model_prediction():
    """测试模型预测"""
    model = load_model('test_model.h5')
    x_test = np.random.rand(10, 28, 28, 1)
    predictions = model.predict(x_test)
    
    assert predictions.shape == (10, 10)
    assert np.allclose(predictions.sum(axis=1), 1.0)  # softmax输出
```

## 测试配置

### conftest.py
定义共享的fixtures和配置。

```python
import pytest
import numpy as np
from keras.models import Sequential

@pytest.fixture
def sample_data():
    """生成示例数据"""
    x = np.random.rand(100, 28, 28, 1)
    y = np.random.randint(0, 10, 100)
    return x, y

@pytest.fixture
def simple_model():
    """创建简单测试模型"""
    model = Sequential([
        Dense(64, activation='relu', input_shape=(784,)),
        Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')
    return model
```

## 最佳实践

### 1. 测试命名
```python
# Good
def test_model_compiles_successfully():
    pass

def test_preprocessing_normalizes_data():
    pass

# Bad
def test1():
    pass

def test_stuff():
    pass
```

### 2. 使用fixtures
```python
@pytest.fixture
def mnist_data():
    """加载MNIST数据（只加载一次）"""
    from keras.datasets import mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    return (x_train[:1000], y_train[:1000]), (x_test[:100], y_test[:100])

def test_with_mnist(mnist_data):
    (x_train, y_train), (x_test, y_test) = mnist_data
    # 使用数据进行测试
```

### 3. 参数化测试
```python
@pytest.mark.parametrize("input_shape,num_classes", [
    ((28, 28, 1), 10),
    ((32, 32, 3), 5),
    ((64, 64, 3), 2),
])
def test_model_with_different_shapes(input_shape, num_classes):
    model = build_model(input_shape, num_classes)
    assert model.output_shape[-1] == num_classes
```

### 4. 跳过耗时测试
```python
@pytest.mark.slow
def test_full_training():
    """完整训练测试（耗时）"""
    pass

# 运行时跳过：pytest -m "not slow"
```

### 5. 临时文件处理
```python
def test_model_save_load(tmp_path):
    """测试模型保存和加载"""
    model = build_model()
    model_path = tmp_path / "test_model.h5"
    
    model.save(model_path)
    loaded_model = load_model(model_path)
    
    assert loaded_model is not None
```

## CI/CD集成

测试会在GitHub Actions中自动运行，配置见 `.github/workflows/ci.yml`。

### 触发条件
- Push到main/develop分支
- 创建Pull Request

### 测试环境
- Python 3.8, 3.9, 3.10
- Ubuntu Latest
- CPU环境

## 常见问题

### Q: 测试太慢怎么办？
A:
- 使用更小的数据集
- 减少训练轮次
- 使用 `@pytest.mark.slow` 标记耗时测试
- 并行运行：`pytest -n auto`

### Q: 如何测试GPU代码？
A:
```python
import tensorflow as tf

@pytest.mark.skipif(not tf.config.list_physical_devices('GPU'),
                    reason="需要GPU")
def test_gpu_training():
    pass
```

### Q: 随机性导致测试不稳定？
A:
```python
def test_with_fixed_seed():
    np.random.seed(42)
    tf.random.set_seed(42)
    # 测试代码
```

### Q: 如何模拟数据加载？
A:
```python
from unittest.mock import patch, MagicMock

@patch('keras.datasets.mnist.load_data')
def test_with_mock_data(mock_load):
    mock_load.return_value = (
        (np.zeros((100, 28, 28)), np.zeros(100)),
        (np.zeros((10, 28, 28)), np.zeros(10))
    )
    # 测试代码
```

## 测试覆盖率目标

| 模块 | 目标覆盖率 |
|------|-----------|
| 核心功能 | >80% |
| 模型构建 | >70% |
| 数据处理 | >80% |
| 工具函数 | >90% |

## 贡献测试

提交新功能时，请：
1. 为新功能编写测试
2. 确保所有测试通过
3. 保持或提高代码覆盖率
4. 更新测试文档

---

💡 **提示**: 良好的测试是代码质量的保证！
