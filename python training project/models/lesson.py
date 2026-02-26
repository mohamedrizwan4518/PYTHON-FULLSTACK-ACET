from extensions import db

from datetime import datetime

class Lesson(db.Model):
    __tablename__ = 'lessons'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    content = db.Column(db.Text, nullable=False)
    difficulty = db.Column(db.String(20), default='Beginner') # Beginner, Intermediate, Advanced
    order = db.Column(db.Integer) # For sequence
    xp_reward = db.Column(db.Integer, default=50)
    
    challenges = db.relationship('Challenge', backref='lesson', lazy='dynamic')
    
    def __repr__(self):
        return f'<Lesson {self.title}>'
