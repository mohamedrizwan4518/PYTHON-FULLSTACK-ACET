class RecommendationService:
    @staticmethod
    def get_recommendation(user):
        from models.lesson import Lesson
        from models.progress import UserProgress
        
        # Get last activity
        last_progress = UserProgress.query.filter_by(user_id=user.id).order_by(UserProgress.completed_at.desc()).first()
        
        if not last_progress:
            return Lesson.query.order_by(Lesson.order).first()
            
        if last_progress.score is not None and last_progress.score < 5:
            # Recommend easier or same lesson
            return Lesson.query.get(last_progress.item_id)
        elif last_progress.score is not None and last_progress.score > 8:
            # Recommend next lesson
            current_lesson = Lesson.query.get(last_progress.item_id)
            if not current_lesson: return Lesson.query.order_by(Lesson.order).first()
            next_lesson = Lesson.query.filter(Lesson.order > current_lesson.order).order_by(Lesson.order).first()
            return next_lesson or current_lesson
        else:
            # Same level or next
            if not last_progress: return Lesson.query.order_by(Lesson.order).first()
            current_lesson = Lesson.query.get(last_progress.item_id)
            if not current_lesson: return Lesson.query.order_by(Lesson.order).first()
            return Lesson.query.filter(Lesson.order > current_lesson.order).order_by(Lesson.order).first() or current_lesson

recommendation_service = RecommendationService()
