import os
from dotenv import load_dotenv
from app import create_app
from services.ai_service import ai_service

load_dotenv()

def test_ai():
    app = create_app('development')
    # No longer need OpenAI key for local Ollama
    with app.app_context():
        print("Testing Ollama AI Mentor response (Llama 3)...")
        try:
            response = ai_service.get_mentor_response("Hello! Introduce yourself briefly.")
            print(f"Response:\n{response}")
        except Exception as e:
            print(f"Exception during AI test: {e}")

if __name__ == "__main__":
    test_ai()
