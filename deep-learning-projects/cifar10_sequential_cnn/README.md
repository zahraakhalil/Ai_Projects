🧠 CIFAR-10 Image Classification with CNN
This project demonstrates how to build, train, and evaluate a Convolutional Neural Network (CNN) using TensorFlow and Keras to classify images from the CIFAR-10 dataset. It’s a beginner-friendly walkthrough that covers data preprocessing, model architecture, training, and performance visualization.
📦 Dataset
- CIFAR-10: 60,000 32×32 color images in 10 classes
- 50,000 training images
- 10,000 test images
- Classes: airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck
🏗️ Model Architecture
The CNN is built using the Keras Sequential API:
Input: (32, 32, 3)
→ Conv2D(32, 3x3) + ReLU
→ MaxPooling2D(2x2)
→ Conv2D(64, 3x3) + ReLU
→ MaxPooling2D(2x2)
→ Conv2D(64, 3x3) + ReLU
→ Flatten
→ Dense(64) + ReLU
→ Dense(10) [Output]


⚙️ Setup
- Install dependencies:
pip install tensorflow matplotlib
- Run the script:
python cnn_cifar10.py
- Save environment:
pip freeze > requirements.txt


📊 Training & Evaluation
- Optimizer: Adam
- Loss: SparseCategoricalCrossentropy(from_logits=True)
- Epochs: 10
- Metrics: Accuracy
Training and validation accuracy/loss are plotted to visualize model performance.
📈 Results
- Achieved ~70% test accuracy after 10 epochs.
- Performance can be improved with data augmentation, dropout, or deeper architectures.
🖼️ Visualization
- First 25 training images are displayed with their class labels.
- Accuracy and loss curves are plotted for both training and validation sets.
🔗 References
- TensorFlow CNN Guide
- CIFAR-10 Dataset
- Keras Sequential API
