import cv2
import pytesseract


def image_to_text(input_path):
   """
   A function to read text from images.
   """
   img = cv2.imread(input_path)
   text = pytesseract.image_to_string(img)

   return text.strip()


# Define image path
medium_text_path = "assets/medium_text.png"

# Extract text
extracted_text = image_to_text(medium_text_path)
print(extracted_text)
