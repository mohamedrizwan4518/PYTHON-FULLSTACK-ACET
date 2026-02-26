from flask import Blueprint, render_template
from models.user import User

leaderboard_bp = Blueprint('leaderboard', __name__)

@leaderboard_bp.route('/')
def index():
    # Sort by XP descending
    top_users = User.query.order_by(User.xp.desc()).limit(50).all()
    return render_template('leaderboard.html', top_users=top_users)
