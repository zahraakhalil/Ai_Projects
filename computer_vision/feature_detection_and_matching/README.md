Image Alignment Using ORB and Homography
This Python script aligns an input image to a template using ORB feature detection and homography transformation. It visualizes matched keypoints, the aligned image, and an overlay comparison for inspection.
Files Used
- image.jpg: The input image to be aligned.
- main.png: The reference template image.
How It Works
- Converts both images to grayscale.
- Detects ORB keypoints and descriptors.
- Matches descriptors using brute-force Hamming distance.
- Sorts matches by distance and retains the top percentage.
- Extracts matched keypoint coordinates.
- Computes homography matrix using RANSAC.
- Warps the input image to align with the template.
- Displays:
- Matched keypoints (if debug=True)
- Side-by-side comparison of aligned and template images
- Overlay blend of aligned and template images
Parameters
- max_features: Maximum number of ORB features to detect (default: 500)
- keep_percent: Percentage of best matches to retain (default: 0.2)
- debug: If True, displays matched keypoints before alignment
Output Windows
- "Matched Keypoints": Shows ORB matches between input and template (if debug is enabled)
- "Aligned Result": Side-by-side view of aligned image and template
- "Overlay Result": Blended overlay of aligned image and template
Dependencies
Install required packages with:
pip install numpy opencv-python imutils


Usage
Run the script directly:
python align_images.py


Make sure image.jpg and main.png are in the same directory or update the paths accordingly.
Notes
- This method assumes the input and template images share similar content and perspective.
- For best results, use high-resolution images with distinct features.
- You can tweak max_features and keep_percent to improve alignment quality.
