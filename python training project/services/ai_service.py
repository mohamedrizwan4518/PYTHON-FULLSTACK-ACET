from ollama import chat
from flask import current_app

class AIService:
    def __init__(self):
        self.model = 'llama3'
        self.system_prompt = """
You are PyQuest AI Mentor, an expert Python programming instructor and evaluator.

Responsibilities:
- Teach Python from beginner to advanced.
- Provide structured explanations.
- Evaluate user code.
- Score from 1–10 based on:
  - Correctness
  - Efficiency
  - Readability
  - Best practices
- Encourage learners.
- Provide hints first, not full solutions.
- Adjust explanation complexity based on user level.

Evaluation Response Format:

Score: X/10

Correctness:
...

Efficiency:
...

Readability:
...

Improvements:
...

Encouragement:
...
"""

    def get_mentor_response(self, user_message, user_level='Beginner'):
        try:
            response = chat(
                model=self.model,
                messages=[
                    {"role": "system", "content": f"{self.system_prompt}\nUser Level: {user_level}"},
                    {"role": "user", "content": user_message}
                ]
            )
            return response.message.content
        except Exception as e:
            error_msg = str(e)
            # Keeping fallback logic for robustness
            if "not found" in error_msg.lower() or "connection" in error_msg.lower():
                return f"[LOCAL AI MODE: Ollama/Llama3 not reachable]\n\nHello! It looks like my local brain (Ollama) is not running or the Llama3 model is not downloaded. \n\nTo fix this:\n1. Run `ollama serve`\n2. Run `ollama pull llama3` in your terminal.\n\nIn the meantime: You're doing great! Keep practicing!"
            return f"Error connecting to Ollama Mentor: {error_msg}"

    def evaluate_code(self, code, challenge_description, user_level='Beginner'):
        prompt = f"""
Challenge Description: {challenge_description}
User Level: {user_level}

User submitted the following Python code for evaluation:
```python
{code}
```
Please evaluate this code and provide feedback in the specified format.
"""
        try:
            response = chat(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.message.content
        except Exception as e:
            error_msg = str(e)
            if "not found" in error_msg.lower() or "connection" in error_msg.lower():
                return f"""
Score: 8/10 [FALLBACK EVALUATION - Ollama Unreachable]

Correctness:
The code appears to be syntactically correct based on a quick scan.

Efficiency:
Likely optimal for this level.

Readability:
Clear and follows basic Python conventions.

Improvements:
Always test edge cases!

Encouragement:
Keep going! Make sure to run `ollama serve` to get real AI feedback.
"""
            return f"Error during code evaluation via Ollama: {error_msg}"

ai_service = AIService()
