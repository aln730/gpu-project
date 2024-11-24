from flask import Flask, request, jsonify, send_file
import os
from model import generate_caption
from meme import add_text_to_image

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/generate_meme', methods=['POST'])
def generate_meme():
    """Handles image upload and meme generation."""
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    # Save uploaded image
    image = request.files['image']
    input_path = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(input_path)

    try:
        caption = generate_caption(input_path)

        output_path = os.path.join(OUTPUT_FOLDER, f"meme_{image.filename}")
        add_text_to_image(input_path, caption, output_path)

        return send_file(output_path, mimetype='image/jpeg')

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        os.remove(input_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
