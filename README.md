# Image-Translation

# Tamil Text Translation and Replacement Using OCR and Google Translate

This project extracts Tamil text from an input image using OCR (Optical Character Recognition), translates the text into English using Google Translate, and replaces the original text in the image with the translated English text. The output is a new image with the translated content in place of the original Tamil text.

---

## Features

- Extracts Tamil and English text from images using Tesseract OCR.
- Detects Tamil text using Unicode checks.
- Translates Tamil text to English using Google Translate.
- Replaces the Tamil text in the image with the translated English text.
- Saves the modified image as an output file.

---

## Requirements

### Libraries

- *Python* (3.x)
- Pillow
- OpenCV
- pytesseract
- googletrans

### Additional Setup

- Install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) and set the path to tesseract.exe in the script.
- Add a TrueType font (e.g., arial.ttf) in the project directory for rendering the translated text.

---

## Installation

1. Clone the repository:
   bash
   git clone <repository-link>
   cd <project-folder>
   

2. Install dependencies:
   bash
   pip install -r requirements.txt
   

3. Configure the Tesseract OCR path in the script:
   python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Path\to\Tesseract-OCR\tesseract.exe'
   

4. Ensure arial.ttf is present in the project directory.

## Usage

1. Place the input image in the designated directory.
2. Update the paths for input_image and output_image in the script.
3. Run the script:
   bash
   python tamil_text_translation.py
   

4. The output image with the translated text will be saved at the specified output path.

## Input and Output Examples

### Input Image

### Output Image

## How to Include Images in This README

1. Save the input and output images in the same directory as the README file.
2. Use the following syntax to add images:
   markdown
   ![Input Image](input_image.jpg)
   ![Output Image](output_image.jpg)
   

3. Ensure the file paths are correct relative to the README location.

## Notes

- Ensure Tesseract is configured to recognize Tamil (tam) language by downloading the necessary language pack.
- If translation fails due to internet connectivity issues, the original text will be retained.
