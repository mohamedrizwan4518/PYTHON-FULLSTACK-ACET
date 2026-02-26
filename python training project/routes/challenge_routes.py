from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from models.challenge import Challenge
from services.evaluation_service import evaluation_service

challenge_bp = Blueprint('challenge', __name__)

@challenge_bp.route('/<int:id>')
@login_required
def challenge_detail(id):
    challenge = Challenge.query.get_or_404(id)
    return render_template('challenges/detail.html', challenge=challenge)

@challenge_bp.route('/<int:id>/submit', methods=['POST'])
@login_required
def challenge_submit(id):
    challenge = Challenge.query.get_or_404(id)
    code = request.form.get('code')
    
    result = evaluation_service.process_submission(current_user, challenge, code)
    
    return jsonify(result)
