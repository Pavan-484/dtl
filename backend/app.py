from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import subprocess
import traceback


# Configure Gemini
import google.generativeai as genai
import os
import tempfile
from pathlib import Path

# Try to load .env file if present
try:
    from dotenv import load_dotenv
    # Load .env from project root
    env_path = Path(__file__).resolve().parent.parent / '.env'
    load_dotenv(dotenv_path=env_path)
except ImportError:
    pass

# Use the user's provided key from env
GENAI_API_KEY = os.environ.get("GENAI_API_KEY")

if not GENAI_API_KEY:
    print("WARNING: GENAI_API_KEY not found in environment variables.")

if GENAI_API_KEY:
    genai.configure(api_key=GENAI_API_KEY)

app = Flask(__name__)
# Enable CORS for all domains
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/api/ocr', methods=['POST'])
def ocr_endpoint():
    return jsonify({'error': 'Offline OCR (Tesseract) is not supported in this cloud deployment. Please use the Sign Reader (Gemini) feature.'}), 501

@app.route('/api/transcribe', methods=['POST'])
def transcribe_endpoint():
    try:
        if 'audio' not in request.files:
            return jsonify({'error': 'No audio file provided'}), 400
        
        audio_file = request.files['audio']
        if audio_file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        # Save to temp file because GenerativeAI prefers file paths or direct upload
        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp:
            audio_file.save(tmp.name)
            tmp_path = tmp.name

        print("Transcribing audio...")
        
        # Upload the file to Gemini
        gemini_file = genai.upload_file(tmp_path, mime_type="audio/wav")
        
        # Prompt for transcription
        model = genai.GenerativeModel("gemini-1.5-flash")
        result = model.generate_content([
            "Listen to this audio commands and transcribe exactly what is said. Output ONLY the text.", 
            gemini_file
        ])
        
        # Cleanup
        os.remove(tmp_path)
        
        text = result.text.strip()
        print(f"Transcription: {text}")
        
        return jsonify({'text': text})

    except Exception as e:
        print("Error transcribing:")
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

@app.route('/api/analyze_sign', methods=['POST'])
def analyze_sign_endpoint():
    try:
        data = request.json
        image_data = data.get('image') # Base64 string
        
        if not image_data:
            return jsonify({'error': 'No image data provided'}), 400

        if ',' in image_data:
            header, encoded = image_data.split(',', 1)
        else:
            encoded = image_data
            
        # Create a dictionary representing the image for Gemini
        # We can pass the base64 data directly with 'mime_type'
        image_part = {
            "mime_type": "image/jpeg",
            "data": encoded
        }

        print("Analyzing sign with Gemini...")
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        # Prompt from original frontend code
        prompt = "EXTRACT TEXT ONLY. Look closely at the image. Read the big illuminated text on the signboard. Ignore background items. If it says 'RADIOLOGY', output 'Radiology'. Just the text."
        
        result = model.generate_content([prompt, image_part])
        text = result.text.strip()
        print(f"Sign Analysis: {text}")
        
        return jsonify({'text': text})

    except Exception as e:
        print("Error analyzing sign:")
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Starting Flask Server on Port 5000...")
    app.run(debug=True, port=5000)
