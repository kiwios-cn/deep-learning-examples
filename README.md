# Deep Learning Examples

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)](https://www.tensorflow.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)](https://pytorch.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange.svg)](notebooks/)

[中文](README_CN.md) | **English**

A comprehensive collection of deep learning examples covering Computer Vision, Natural Language Processing, Sequence Models, and Time Series Prediction. Perfect for learning, teaching, and rapid prototyping.

<p align="center">
  <img src="docs/images/banner.png" alt="Deep Learning Examples" width="800">
</p>

---

## ✨ Features

- 📚 **70+ Ready-to-use Examples** - From basics to advanced topics
- 🎯 **Multiple Frameworks** - TensorFlow, PyTorch, and Keras
- 📊 **Well-documented** - Detailed explanations and comments
- 🚀 **Quick Start** - Run examples in minutes
- 📓 **Interactive Notebooks** - Jupyter notebooks for experimentation
- 🏆 **Best Practices** - Industry-standard code patterns
- 🔄 **Regular Updates** - New examples added monthly

---

## 📑 Table of Contents

- [Examples Overview](#examples-overview)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Examples by Category](#examples-by-category)
  - [Computer Vision](#computer-vision)
  - [Natural Language Processing](#nlp)
  - [Sequence Models](#sequence-models)
  - [Time Series](#time-series)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Examples Overview

| Category | Examples | Difficulty | Frameworks |
|----------|----------|------------|------------|
| 🖼️ Computer Vision | 25+ | ⭐⭐⭐ | TensorFlow, PyTorch |
| 📝 NLP | 20+ | ⭐⭐⭐⭐ | PyTorch, Transformers |
| 🔄 Sequence Models | 15+ | ⭐⭐⭐⭐ | TensorFlow, PyTorch |
| 📈 Time Series | 10+ | ⭐⭐⭐ | TensorFlow, PyTorch |

---

## 🚀 Installation

### Prerequisites

- Python 3.8+
- CUDA 11.0+ (optional, for GPU support)
- 8GB+ RAM recommended

### Quick Install

```bash
# Clone repository
git clone https://github.com/kiwios-cn/deep-learning-examples.git
cd deep-learning-examples

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install Jupyter (optional)
pip install jupyter
```

### Using Docker

```bash
# Build image
docker build -t dl-examples .

# Run container with GPU support
docker run --gpus all -it -p 8888:8888 -v $(pwd):/workspace dl-examples

# Start Jupyter
jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root
```

### Using Conda

```bash
# Create environment
conda env create -f environment.yml
conda activate dl-examples
```

---

## ⚡ Quick Start

### Run Your First Example

```bash
# Computer Vision - Image Classification
cd computer_vision/image_classification
python mnist_cnn.py

# NLP - Sentiment Analysis
cd nlp/sentiment_analysis
python imdb_lstm.py

# Launch Jupyter Notebook
jupyter notebook notebooks/getting_started.ipynb
```

### Example Output

```
Training CNN on MNIST...
Epoch 1/10 - loss: 0.2546 - accuracy: 0.9241
Epoch 2/10 - loss: 0.0842 - accuracy: 0.9756
...
Test accuracy: 99.12%
```

---

## 🖼️ Computer Vision

### Image Classification

| Example | Description | Accuracy | Dataset |
|---------|-------------|----------|---------|
| [MNIST CNN](computer_vision/image_classification/mnist_cnn.py) | Basic CNN for digit recognition | 99.1% | MNIST |
| [CIFAR-10 ResNet](computer_vision/image_classification/cifar10_resnet.py) | ResNet architecture | 94.5% | CIFAR-10 |
| [ImageNet Transfer](computer_vision/image_classification/imagenet_transfer.py) | Transfer learning | 92.3% | ImageNet |

#### Example: MNIST CNN

```python
import tensorflow as tf
from tensorflow.keras import layers, models

# Load data
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# Build model
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Train
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_train, y_train, epochs=10, validation_split=0.1)

# Evaluate
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'Test accuracy: {test_acc:.4f}')
```

### Object Detection

| Example | Description | mAP | Framework |
|---------|-------------|-----|-----------|
| [YOLO v5](computer_vision/object_detection/yolov5_detection.py) | Real-time detection | 0.65 | PyTorch |
| [Faster R-CNN](computer_vision/object_detection/faster_rcnn.py) | Two-stage detector | 0.72 | TensorFlow |
| [RetinaNet](computer_vision/object_detection/retinanet.py) | Single-stage detector | 0.68 | PyTorch |

### Image Segmentation

| Example | Description | IoU | Framework |
|---------|-------------|-----|-----------|
| [U-Net Medical](computer_vision/segmentation/unet_medical.py) | Medical image segmentation | 0.89 | TensorFlow |
| [DeepLab v3](computer_vision/segmentation/deeplab_v3.py) | Semantic segmentation | 0.82 | PyTorch |
| [Mask R-CNN](computer_vision/segmentation/mask_rcnn.py) | Instance segmentation | 0.75 | TensorFlow |

### Generative Models

| Example | Description | Framework |
|---------|-------------|-----------|
| [GAN MNIST](computer_vision/gan/gan_mnist.py) | Generate handwritten digits | TensorFlow |
| [StyleGAN](computer_vision/gan/stylegan.py) | High-quality face generation | PyTorch |
| [VAE](computer_vision/gan/vae.py) | Variational autoencoder | TensorFlow |

---

## 📝 Natural Language Processing

### Text Classification

| Example | Description | Accuracy | Framework |
|---------|-------------|----------|-----------|
| [IMDB Sentiment](nlp/text_classification/imdb_sentiment.py) | Movie review sentiment | 89.5% | TensorFlow |
| [News Classification](nlp/text_classification/news_classification.py) | Multi-class news categorization | 92.1% | PyTorch |
| [BERT Fine-tuning](nlp/text_classification/bert_finetune.py) | BERT for classification | 94.8% | Transformers |

#### Example: BERT Fine-tuning

```python
from transformers import BertTokenizer, BertForSequenceClassification
from transformers import Trainer, TrainingArguments
import torch

# Load pre-trained model
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Tokenize data
def tokenize_function(examples):
    return tokenizer(examples['text'], padding='max_length', truncation=True)

tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Training arguments
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=64,
    warmup_steps=500,
    weight_decay=0.01,
)

# Train
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets['train'],
    eval_dataset=tokenized_datasets['test']
)
trainer.train()
```

### Named Entity Recognition

| Example | Description | F1 Score | Framework |
|---------|-------------|----------|-----------|
| [BiLSTM-CRF](nlp/ner/bilstm_crf.py) | NER with CRF layer | 0.87 | PyTorch |
| [BERT NER](nlp/ner/bert_ner.py) | BERT for NER | 0.92 | Transformers |

### Machine Translation

| Example | Description | BLEU | Framework |
|---------|-------------|------|-----------|
| [Seq2Seq](nlp/translation/seq2seq.py) | Basic seq2seq | 24.3 | TensorFlow |
| [Transformer](nlp/translation/transformer.py) | Attention is all you need | 32.1 | PyTorch |

### Question Answering

| Example | Description | EM/F1 | Framework |
|---------|-------------|-------|-----------|
| [SQuAD BERT](nlp/qa/squad_bert.py) | BERT for QA | 82.3/89.5 | Transformers |

---

## 🔄 Sequence Models

### Time Series Forecasting

| Example | Description | MAE | Framework |
|---------|-------------|-----|-----------|
| [LSTM Forecasting](sequence_models/time_series/lstm_forecast.py) | Stock price prediction | 0.032 | TensorFlow |
| [GRU Forecasting](sequence_models/time_series/gru_forecast.py) | Weather forecasting | 0.028 | PyTorch |
| [Transformer Time Series](sequence_models/time_series/transformer_ts.py) | Transformer for TS | 0.025 | PyTorch |

### Speech Recognition

| Example | Description | WER | Framework |
|---------|-------------|-----|-----------|
| [DeepSpeech](sequence_models/speech/deepspeech.py) | Speech to text | 12.3% | TensorFlow |

---

## 📈 Time Series

### Anomaly Detection

| Example | Description | Framework |
|---------|-------------|-----------|
| [Autoencoder Anomaly](time_series/anomaly_detection/autoencoder.py) | Detect anomalies | TensorFlow |
| [LSTM Anomaly](time_series/anomaly_detection/lstm_anomaly.py) | LSTM-based detection | PyTorch |

---

## 📓 Jupyter Notebooks

Interactive notebooks for learning and experimentation:

| Notebook | Topic | Level |
|----------|-------|-------|
| [Getting Started](notebooks/01_getting_started.ipynb) | Introduction to DL | Beginner |
| [CNN Visualization](notebooks/02_cnn_visualization.ipynb) | Visualize CNN layers | Intermediate |
| [Transfer Learning](notebooks/03_transfer_learning.ipynb) | Use pre-trained models | Intermediate |
| [Attention Mechanism](notebooks/04_attention.ipynb) | Understanding attention | Advanced |
| [GAN Tutorial](notebooks/05_gan_tutorial.ipynb) | Build your own GAN | Advanced |

---

## 🏗️ Project Structure

```
deep-learning-examples/
├── computer_vision/
│   ├── image_classification/
│   │   ├── mnist_cnn.py
│   │   ├── cifar10_resnet.py
│   │   └── imagenet_transfer.py
│   ├── object_detection/
│   │   ├── yolov5_detection.py
│   │   └── faster_rcnn.py
│   ├── segmentation/
│   │   ├── unet_medical.py
│   │   └── deeplab_v3.py
│   └── gan/
│       ├── gan_mnist.py
│       └── stylegan.py
├── nlp/
│   ├── text_classification/
│   │   ├── imdb_sentiment.py
│   │   └── bert_finetune.py
│   ├── ner/
│   │   ├── bilstm_crf.py
│   │   └── bert_ner.py
│   ├── translation/
│   │   ├── seq2seq.py
│   │   └── transformer.py
│   └── qa/
│       └── squad_bert.py
├── sequence_models/
│   ├── time_series/
│   │   ├── lstm_forecast.py
│   │   └── transformer_ts.py
│   └── speech/
│       └── deepspeech.py
├── time_series/
│   └── anomaly_detection/
│       ├── autoencoder.py
│       └── lstm_anomaly.py
├── notebooks/
│   ├── 01_getting_started.ipynb
│   ├── 02_cnn_visualization.ipynb
│   └── ...
├── utils/
│   ├── data_loader.py
│   ├── metrics.py
│   └── visualization.py
├── tests/
├── docs/
├── requirements.txt
├── setup.py
└── README.md
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Ways to Contribute

1. **Add new examples** - Share your implementations
2. **Improve documentation** - Make it clearer
3. **Fix bugs** - Help us improve quality
4. **Suggest features** - Tell us what you need

### Contribution Guidelines

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

Quick start:

```bash
# Fork and clone
git clone https://github.com/YOUR_USERNAME/deep-learning-examples.git
cd deep-learning-examples

# Create branch
git checkout -b feature/new-example

# Make changes and test
pytest tests/

# Commit and push
git commit -m "Add: New CNN example for CIFAR-100"
git push origin feature/new-example

# Open pull request
```

---

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

- [TensorFlow](https://www.tensorflow.org/) - Deep learning framework
- [PyTorch](https://pytorch.org/) - Deep learning framework
- [Hugging Face](https://huggingface.co/) - Transformers library
- [Keras](https://keras.io/) - High-level API

---

## 📧 Contact

- **Author**: kiwios
- **Email**: kiwios.cn@gmail.com
- **GitHub**: [@kiwios-cn](https://github.com/kiwios-cn)

---

## 📊 Statistics

- **70+ Examples** across 4 categories
- **2 Frameworks** (TensorFlow & PyTorch)
- **10+ Datasets** covered
- **Active Development** - Updated monthly

---

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=kiwios-cn/deep-learning-examples&type=Date)](https://star-history.com/#kiwios-cn/deep-learning-examples&Date)

---

**If you find this useful, please give it a ⭐!**

Happy Learning! 🚀
