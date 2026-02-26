from extensions import db

from datetime import datetime

class Badge(db.Model):
    __tablename__ = 'badges'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    description = db.Column(db.String(256))
    icon = db.Column(db.String(64)) # Icon class or filename
    criteria_type = db.Column(db.String(64)) # e.g., 'challenges_completed', 'streak', 'level'
    criteria_value = db.Column(db.Integer)

    def __repr__(self):
        return f'<Badge {self.name}>'

class UserBadge(db.Model):
    __tablename__ = 'user_badges'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    badge_id = db.Column(db.Integer, db.ForeignKey('badges.id'), nullable=False)
    awarded_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref=db.backref('badges', lazy='dynamic'))
    badge = db.relationship('Badge', backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return f'<UserBadge User:{self.user_id} Badge:{self.badge_id}>'
