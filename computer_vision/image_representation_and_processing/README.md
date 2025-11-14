🧠 Computer Vision Fundamentals with OpenCV
Overview
This project is a hands-on exploration of core computer vision techniques using OpenCV and NumPy. Across four structured notebooks, it demonstrates how to manipulate, analyze, and visualize images—building a strong foundation for more advanced CV and deep learning workflows.
Whether you're preprocessing data for a CNN or experimenting with edge detection, this project offers reproducible, well-documented examples that showcase technical depth and presentation skills.
📂 Notebooks Included
- 01_basic_operations.ipynb
- Focus: Image loading, color spaces, drawing
- Techniques: BGR ↔ RGB, grayscale conversion, channel splitting, pixel access, drawing primitives
- 02_transformations_histograms.ipynb
- Focus: Geometric and arithmetic operations
- Techniques: Translation, rotation, resizing, flipping, masking, histograms, blurring
- 03_morphological_filters.ipynb
- Focus: Morphological processing
- Techniques: Erosion, dilation, opening, closing, gradient, synthetic noise removal
- 04_edge_detection.ipynb
- Focus: Edge detection and filtering
- Techniques: Prewitt, Sobel, Canny, Gaussian blur, manual kernel application
🛠️ Setup Instructions
Install dependencies:
pip install opencv-python numpy matplotlib imutils


Ensure your working directory contains the required images:
- image1.png
- colors.jpg
- rgb_image.jpg
- grayscale_image.jpg
🚀 How to Run
Each notebook is standalone and can be run in Jupyter or Google Colab. GUI-based cv.imshow() calls require a local environment with display capabilities. For Colab, consider replacing cv.imshow() with matplotlib visualizations.
📸 Sample Outputs
- ✅ Color channel extraction and saving
- 🔄 Translated, rotated, and flipped images
- 📊 RGB and grayscale histograms
- 🧼 Morphological filtering on noisy text
- 🧠 Edge maps using Prewitt, Sobel, and Canny
💡 Learning Outcomes
- Understand pixel-level manipulation and image representation
- Apply geometric transformations and filtering techniques
- Visualize image statistics and histograms
- Implement morphological operations for noise reduction
- Compare edge detection algorithms and their visual impact
👩‍💻 Author
Zahraa
Aspiring Data Scientist & Machine Learning Engineer
Focused on reproducible ML pipelines, impactful documentation, and professional self-presentation.