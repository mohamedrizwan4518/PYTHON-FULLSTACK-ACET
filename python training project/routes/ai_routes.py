from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from services.ai_service import ai_service

ai_bp = Blueprint('ai', __name__)

@ai_bp.route('/mentor/chat', methods=['POST'])
@login_required
def mentor_chat():
    message = request.json.get('message')
    if not message:
        return jsonify({"error": "No message provided"}), 400
        
    response = ai_service.get_mentor_response(message, current_user.level)
    return jsonify({"response": response})
