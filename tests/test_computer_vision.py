"""
计算机视觉模块测试
"""
import pytest
import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout


class TestModelArchitecture:
    """测试模型架构"""

    def test_simple_cnn_structure(self):
        """测试简单CNN结构"""
        model = Sequential([
            Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
            MaxPooling2D((2, 2)),
            Conv2D(64, (3, 3), activation='relu'),
            MaxPooling2D((2, 2)),
            Flatten(),
            Dense(64, activation='relu'),
            Dense(10, activation='softmax')
        ])

        assert len(model.layers) == 7
        assert model.input_shape == (None, 28, 28, 1)
        assert model.output_shape == (None, 10)

    def test_model_compilation(self):
        """测试模型编译"""
        model = Sequential([
            Flatten(input_shape=(28, 28, 1)),
            Dense(128, activation='relu'),
            Dense(10, activation='softmax')
        ])

        model.compile(
            optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy']
        )

        assert model.optimizer is not None
        assert model.loss is not None


class TestDataPreprocessing:
    """测试数据预处理"""

    def test_normalization(self):
        """测试数据归一化"""
        data = np.random.randint(0, 255, (100, 28, 28, 1)).astype('float32')
        normalized = data / 255.0

        assert normalized.min() >= 0.0
        assert normalized.max() <= 1.0

    def test_reshape(self):
        """测试数据reshape"""
        data = np.random.rand(100, 28, 28)
        reshaped = data.reshape(100, 28, 28, 1)

        assert reshaped.shape == (100, 28, 28, 1)

    def test_train_test_split(self):
        """测试数据集划分"""
        data = np.random.rand(1000, 28, 28, 1)
        labels = np.random.randint(0, 10, 1000)

        train_size = int(0.8 * len(data))
        x_train = data[:train_size]
        x_test = data[train_size:]

        assert len(x_train) == 800
        assert len(x_test) == 200


class TestModelTraining:
    """测试模型训练"""

    @pytest.mark.slow
    def test_quick_training(self):
        """快速训练测试（2个epoch）"""
        # 生成小数据集
        x_train = np.random.rand(100, 28, 28, 1).astype('float32')
        y_train = np.random.randint(0, 10, 100)

        # 构建简单模型
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

        # 训练
        history = model.fit(
            x_train, y_train,
            epochs=2,
            batch_size=32,
            verbose=0
        )

        assert 'loss' in history.history
        assert 'accuracy' in history.history
        assert len(history.history['loss']) == 2


class TestModelPrediction:
    """测试模型预测"""

    def test_prediction_shape(self):
        """测试预测输出形状"""
        model = Sequential([
            Flatten(input_shape=(28, 28, 1)),
            Dense(64, activation='relu'),
            Dense(10, activation='softmax')
        ])

        model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

        x_test = np.random.rand(10, 28, 28, 1).astype('float32')
        predictions = model.predict(x_test, verbose=0)

        assert predictions.shape == (10, 10)

    def test_softmax_output(self):
        """测试softmax输出和为1"""
        model = Sequential([
            Flatten(input_shape=(28, 28, 1)),
            Dense(10, activation='softmax')
        ])

        x_test = np.random.rand(5, 28, 28, 1).astype('float32')
        predictions = model.predict(x_test, verbose=0)

        # 每行和应该接近1
        assert np.allclose(predictions.sum(axis=1), 1.0, atol=1e-5)


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
