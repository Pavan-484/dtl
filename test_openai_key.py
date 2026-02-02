#!/usr/bin/env python3
"""
Quick test script to verify OpenAI API key is working
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# Load .env file
env_path = Path(__file__).resolve().parent / '.env'
load_dotenv(dotenv_path=env_path)

# Get API key
api_key = os.environ.get("OPENAI_API_KEY")

print("=" * 60)
print("OpenAI API Key Test")
print("=" * 60)

if not api_key:
    print("❌ ERROR: OPENAI_API_KEY not found in .env file")
    print("\nPlease add your API key to .env file:")
    print("OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxx")
    exit(1)

if api_key == "your-openai-api-key-here":
    print("❌ ERROR: API key is still the placeholder value")
    print("\nPlease replace 'your-openai-api-key-here' with your actual OpenAI API key")
    exit(1)

print(f"✅ API Key found: {api_key[:15]}...{api_key[-4:]}")
print("\nTesting connection to OpenAI...")

try:
    client = OpenAI(api_key=api_key)
    
    # Test with a simple chat completion
    print("\n1️⃣ Testing Chat Completion (GPT-4o)...")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": "Say 'Hello, API is working!' if you can hear me."}
        ],
        max_tokens=20
    )
    result = response.choices[0].message.content
    print(f"   Response: {result}")
    print("   ✅ Chat API working!")
    
    print("\n2️⃣ Testing Model List...")
    models = client.models.list()
    print(f"   ✅ Found {len(models.data)} models available")
    
    print("\n" + "=" * 60)
    print("🎉 SUCCESS! Your OpenAI API key is working perfectly!")
    print("=" * 60)
    print("\n✅ You can now:")
    print("   - Use voice transcription (Whisper)")
    print("   - Use sign reading (GPT-4o Vision)")
    print("   - All features of your Voice Assistant app")
    print("\nNext steps:")
    print("   1. Make sure Flask backend is running (python3 app.py)")
    print("   2. Open http://localhost:5173 in your browser")
    print("   3. Test the voice features!")
    
except Exception as e:
    print(f"\n❌ ERROR: {str(e)}")
    print("\nPossible issues:")
    print("   - Invalid API key")
    print("   - No credits/quota on your OpenAI account")
    print("   - Network connection issue")
    print("\nPlease check:")
    print("   - Your API key at: https://platform.openai.com/api-keys")
    print("   - Your usage/billing at: https://platform.openai.com/usage")
    exit(1)
