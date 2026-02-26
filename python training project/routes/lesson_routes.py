from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from models.lesson import Lesson
from models.progress import UserProgress

lesson_bp = Blueprint('lesson', __name__)

@lesson_bp.route('/')
@login_required
def list_lessons():
    lessons = Lesson.query.order_by(Lesson.order).all()
    # Mark completed lessons
    completed_ids = [p.item_id for p in UserProgress.query.filter_by(user_id=current_user.id, item_type='lesson').all()]
    return render_template('lessons/list.html', lessons=lessons, completed_ids=completed_ids)

@lesson_bp.route('/<int:id>')
@login_required
def lesson_detail(id):
    lesson = Lesson.query.get_or_404(id)
    # Mark as viewed/completed (simple logic)
    existing = UserProgress.query.filter_by(user_id=current_user.id, item_type='lesson', item_id=id).first()
    if not existing:
        from extensions import db
        progress = UserProgress(user_id=current_user.id, item_type='lesson', item_id=id)

        current_user.xp += lesson.xp_reward
        db.session.add(progress)
        db.session.commit()
        flash(f'Lesson completed! +{lesson.xp_reward} XP')
        
    return render_template('lessons/detail.html', lesson=lesson)
