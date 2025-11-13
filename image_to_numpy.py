import cv2
import numpy as np

# Step 1: Read image
img_path = input("Enter image filename (e.g., image.jpg): ")
img = cv2.imread(img_path)

if img is None:
    print("❌ Error: Image not found!")
    exit()

# Step 2: Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Step 3: Resize while preserving aspect ratio
max_width = 600
h, w = gray.shape
scale = min(max_width / w, 1)
new_w, new_h = int(w * scale), int(h * scale)
resized = cv2.resize(gray, (new_w, new_h))

# Step 4: Save as NumPy array
np.save("grayscale_image.npy", resized)
print("✅ Grayscale image saved as 'grayscale_image.npy'")

# Optional: Display the resized grayscale image
cv2.imshow("Grayscale Image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
