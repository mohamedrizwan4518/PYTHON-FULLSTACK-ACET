from extensions import db

from datetime import datetime

class UserProgress(db.Model):
    __tablename__ = 'user_progress'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    item_type = db.Column(db.String(20), nullable=False) # 'lesson' or 'challenge'
    item_id = db.Column(db.Integer, nullable=False)
    
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)
    score = db.Column(db.Integer) # AI score 1-10
    attempts = db.Column(db.Integer, default=1)
    feedback = db.Column(db.Text)
    
    def __repr__(self):
        return f'<UserProgress User:{self.user_id} Item:{self.item_type}:{self.item_id}>'
