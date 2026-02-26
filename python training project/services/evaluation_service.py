from services.ai_service import ai_service
from services.xp_service import xp_service
from services.leveling_service import leveling_service
from services.badge_service import badge_service
from models.user import User
from models.progress import UserProgress
from extensions import db


class EvaluationService:
    @staticmethod
    def process_submission(user, challenge, code):
        # 1. Evaluate via AI
        feedback_raw = ai_service.evaluate_code(code, challenge.description, user.level)
        
        # Extract score from feedback (simple heuristic)
        score = 0
        try:
            if "Score:" in feedback_raw:
                score_str = feedback_raw.split("Score:")[1].split("/10")[0].strip()
                score = int(score_str)
        except:
            score = 5 # Default if parsing fails
            
        # 2. Calculate XP
        # Check if first attempt
        existing_progress = UserProgress.query.filter_by(user_id=user.id, item_type='challenge', item_id=challenge.id).first()
        first_attempt = existing_progress is None
        
        # Check syntax (naive check for now)
        no_syntax_errors = True
        try:
            compile(code, '<string>', 'exec')
        except SyntaxError:
            no_syntax_errors = False
            
        earned_xp = xp_service.calculate_xp(challenge.xp_reward, no_syntax_errors, first_attempt, user.streak_days)
        
        # 3. Update User
        user.xp += earned_xp
        leveled_up, new_level = leveling_service.check_level_up(user.xp, user.level)
        if leveled_up:
            user.level = new_level
            
        # 4. Save Progress
        if first_attempt:
            progress = UserProgress(user_id=user.id, item_type='challenge', item_id=challenge.id, score=score, feedback=feedback_raw)
            db.session.add(progress)
        else:
            existing_progress.attempts += 1
            existing_progress.score = score
            existing_progress.feedback = feedback_raw
            
        # 5. Check Badges
        new_badges = badge_service.check_and_award_badges(user)
        
        db.session.commit()
        
        return {
            "score": score,
            "feedback": feedback_raw,
            "xp_earned": earned_xp,
            "leveled_up": leveled_up,
            "new_level": user.level,
            "new_badges": [b.name for b in new_badges]
        }

evaluation_service = EvaluationService()
