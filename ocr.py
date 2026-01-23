import cv2
import pytesseract


# Read image
easy_text_path = "assets/easy_text.png"
easy_img = cv2.imread(easy_text_path)

# Convert to text
text = pytesseract.image_to_string(easy_img)
print(text)

