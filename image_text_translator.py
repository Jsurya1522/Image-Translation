### Image text translation 

from PIL import Image, ImageDraw, ImageFont
import pytesseract
from googletrans import Translator
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def is_tamil(text):
    """Check if the text contains Tamil characters."""
    for char in text:
        if '\u0b80' <= char <= '\u0bff':  # Unicode range for Tamil characters
            return True
    return False


def translate_image(input_image_path, output_image_path):
    # Load the image
    image = cv2.imread(input_image_path)
    pil_image = Image.open(input_image_path).convert("RGB")
    draw = ImageDraw.Draw(pil_image)

    # Extract text using OCR
    print("Extracting Tamil texts...")
    data = pytesseract.image_to_data(image, lang='tam+eng', output_type=pytesseract.Output.DICT)
    translator = Translator()

    for i in range(len(data["text"])):
        text = data["text"][i].strip()
        if text and is_tamil(text):  # Process only Tamil text
            x, y, w, h = data["left"][i], data["top"][i], data["width"][i], data["height"][i]
            print(text)

            # Translate Tamil text to English
            try:
                translated_text = translator.translate(text, src="ta", dest="en").text
                print("translated text",translated_text)
            except Exception as e:
                print(f"Translation failed for '{text}': {e}")
                translated_text = text  # Fallback to original text if translation fails

            # Fill the Tamil text area with background color
            region = image[y:y + h, x:x + w]
            avg_color_bgr = cv2.mean(region)[:3]
            avg_color_rgb = (int(avg_color_bgr[2]), int(avg_color_bgr[1]), int(avg_color_bgr[0]))
            draw.rectangle([x, y, x + w, y + h], fill=avg_color_rgb)

            # Write the translated English text in the same position
            font_size = int(h * 0.8)  # Adjust font size based on bounding box height
            font_path = "arial.ttf"  
            font = ImageFont.truetype(font_path, size=font_size)

            draw.text((x, y), translated_text, fill="black", font=font)

    # Save the output image
    pil_image.save(output_image_path)
    print(f"\nTranslated image saved to {output_image_path}")


# Example usage
input_image = "D:\\Sem 10\\Novintix\\input_image\\inp2.jpg"
output_image = "D:\\Sem 10\\Novintix\\output_image\\oup2.jpeg"
translate_image(input_image, output_image)
