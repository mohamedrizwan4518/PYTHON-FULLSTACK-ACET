import math

class LevelingService:
    @staticmethod
    def get_required_xp(level):
        """required_xp = 100 * (level ^ 1.5)"""
        if level < 1:
            return 0
        return int(100 * math.pow(level, 1.5))

    @staticmethod
    def check_level_up(current_xp, current_level):
        required = LevelingService.get_required_xp(current_level)
        if current_xp >= required:
            return True, current_level + 1
        return False, current_level

leveling_service = LevelingService()
