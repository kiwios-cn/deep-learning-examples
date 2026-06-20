"""
pytest配置和共享fixtures
"""
import pytest
import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Flatten


@pytest.fixture(scope="session", autouse=True)
def set_random_seeds():
    """设置随机种子以保证测试可重复性"""
    np.random.seed(42)
    tf.random.set_seed(42)


@pytest.fixture
def sample_image_data():
    """生成示例图像数据（MNIST格式）"""
    x = np.random.rand(100, 28, 28, 1).astype('float32')
    y = np.random.randint(0, 10, 100)
    return x, y


@pytest.fixture
def sample_text_data():
    """生成示例文本序列数据"""
    # 模拟文本序列（词ID）
    sequences = np.random.randint(1, 1000, (100, 50))
    labels = np.random.randint(0, 2, 100)
    return sequences, labels


@pytest.fixture
def sample_time_series_data():
    """生成示例时间序列数据"""
    # 时间步长=24, 特征数=5
    x = np.random.randn(100, 24, 5).astype('float32')
    y = np.random.randn(100, 1).astype('float32')
    return x, y


@pytest.fixture
def simple_classifier_model():
    """创建简单的分类模型"""
    model = Sequential([
        Flatten(input_shape=(28, 28, 1)),
        Dense(64, activation='relu'),
        Dense(10, activation='softmax')
    ])
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    return model


@pytest.fixture
def binary_classifier_model():
    """创建二分类模型"""
    model = Sequential([
        Flatten(input_shape=(28, 28, 1)),
        Dense(64, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    return model


def pytest_configure(config):
    """pytest配置"""
    config.addinivalue_line(
        "markers", "slow: 标记为慢速测试（需要较长时间）"
    )
    config.addinivalue_line(
        "markers", "gpu: 标记为需要GPU的测试"
    )
    config.addinivalue_line(
        "markers", "integration: 标记为集成测试"
    )


def pytest_collection_modifyitems(config, items):
    """修改测试收集行为"""
    # 如果没有GPU，跳过GPU测试
    if not tf.config.list_physical_devices('GPU'):
        skip_gpu = pytest.mark.skip(reason="需要GPU环境")
        for item in items:
            if "gpu" in item.keywords:
                item.add_marker(skip_gpu)
