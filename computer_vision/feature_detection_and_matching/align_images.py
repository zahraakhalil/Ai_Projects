import numpy as np
import cv2 as cv
import imutils

def align_images(image, template, max_features=500, keep_percent=0.2, debug=False):
    image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    template_gray = cv.cvtColor(template, cv.COLOR_BGR2GRAY)

    orb = cv.ORB_create(max_features)
    (kpsA, descA) = orb.detectAndCompute(image_gray, None)
    (kpsB, descB)= orb.detectAndCompute(template_gray, None)

    method = cv.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING
    matcher = cv.DescriptorMatcher_create(method)
    matches = matcher.match(descA, descB)

    matches = sorted(matches, key = lambda x:x.distance)
     
    keep = int(len(matches)*keep_percent)
    matches = matches[:keep]

    ptsA = np.zeros((len(matches), 2), dtype="float")
    ptsB = np.zeros((len(matches), 2), dtype="float")

    if  debug:
        matchedVis = cv.drawMatches(image, kpsA, template, kpsB, matches, None)
        matchedVis = imutils.resize(matchedVis, width=1000)
        cv.imshow("Matched Keypoints", matchedVis)
        if cv.waitKey(0):
            cv.destroyAllWindows()

    for (i,m) in enumerate(matches):
        ptsA[i] = kpsA[m.queryIdx].pt
        ptsB[i] = kpsB[m.trainIdx].pt
    
    (H, mask) = cv.findHomography(ptsA, ptsB, cv.RANSAC)
    (h,w)= template.shape[:2]
    aligned = cv.warpPerspective(image, H, (w,h))
    return aligned

image = cv.imread("image.jpg")
template = cv.imread("main.png")

print("Aligning Image")

aligned = align_images(image, template, debug=True)

aligned = imutils.resize(aligned, width=700)
template = imutils.resize(template, width=700)
stacked = np.hstack([aligned, template])

overlay = template.copy()
output = aligned.copy()
cv.addWeighted(overlay, 0.5, output, 0.5, 0, output)
cv.imshow("Aligned Result", stacked)
cv.imshow("Overlay Result", output)
if cv.waitKey(0):
            cv.destroyAllWindows()