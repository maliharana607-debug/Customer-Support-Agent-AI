import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

if api_key:
    print("✅ API key loaded successfully!")
    print(f"Key starts with: {api_key[:20]}...")
else:
    print("❌ API key not found")