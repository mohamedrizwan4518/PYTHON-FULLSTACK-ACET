from extensions import db


class Challenge(db.Model):
    __tablename__ = 'challenges'
    
    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lessons.id'))
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    starter_code = db.Column(db.Text)
    solution_code = db.Column(db.Text)
    xp_reward = db.Column(db.Integer, default=100)
    difficulty = db.Column(db.String(20), default='Beginner')
    
    def __repr__(self):
        return f'<Challenge {self.title}>'
