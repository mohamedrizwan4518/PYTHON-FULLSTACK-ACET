from extensions import db

from models.badge import Badge, UserBadge
from datetime import datetime

class BadgeService:
    @staticmethod
    def check_and_award_badges(user):
        from models.progress import UserProgress
        from models.challenge import Challenge
        
        new_badges = []
        
        # 1. Python Explorer: 10 challenges completed
        challenge_count = UserProgress.query.filter_by(user_id=user.id, item_type='challenge').count()
        if challenge_count >= 10:
            new_badges.append(BadgeService._award_badge(user, "Python Explorer"))
            
        # 2. Consistency Master: 7-day streak
        if user.streak_days >= 7:
            new_badges.append(BadgeService._award_badge(user, "Consistency Master"))
            
        # 3. Rising Developer: Level 5
        if user.level >= 5:
            new_badges.append(BadgeService._award_badge(user, "Rising Developer"))
            
        # 4. Python Warrior: Level 10
        if user.level >= 10:
            new_badges.append(BadgeService._award_badge(user, "Python Warrior"))
            
        db.session.commit()
        return [b for b in new_badges if b is not None]

    @staticmethod
    def _award_badge(user, badge_name):
        badge = Badge.query.filter_by(name=badge_name).first()
        if not badge:
            return None
            
        existing = UserBadge.query.filter_by(user_id=user.id, badge_id=badge.id).first()
        if not existing:
            award = UserBadge(user_id=user.id, badge_id=badge.id)
            db.session.add(award)
            return badge
        return None

badge_service = BadgeService()
