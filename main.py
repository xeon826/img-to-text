import subprocess
from PIL import Image
import pytesseract

def get_window_id(window_name):
    output = subprocess.check_output(["xwininfo", "-name", window_name]).decode()
    return output.split()[3]

def capture_window(window_id, output_filename):
    subprocess.call(["xwd", "-id", window_id, "-out", output_filename])
    convert_xwd_to_png(output_filename, output_filename.replace(".xwd", ".png"))

def convert_xwd_to_png(xwd_filename, png_filename):
    subprocess.call(["convert", xwd_filename, png_filename])

def extract_text_from_image(image_path):
    try:
        return pytesseract.image_to_string(Image.open(image_path))
    except Exception as e:
        print(f"Error during OCR processing: {e}")
        return ""

# Parameters
window_name = "Dansieg"
output_filename = "window_capture.xwd"
# Process
window_id = get_window_id(window_name)
if window_id:
    capture_window(window_id, output_filename)
    text = extract_text_from_image(output_filename.replace(".xwd", ".png"))
    print("Extracted Text:\n", text)
else:
    print("Window not found!")

