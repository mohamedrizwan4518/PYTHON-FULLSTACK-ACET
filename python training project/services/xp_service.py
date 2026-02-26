class XPService:
    @staticmethod
    def calculate_xp(base_xp, no_syntax_errors=False, first_attempt=False, streak_days=0):
        total_xp = base_xp
        
        if no_syntax_errors:
            total_xp += 10
            
        if first_attempt:
            total_xp += 20
            
        # +5 per streak day
        total_xp += (streak_days * 5)
        
        return total_xp

xp_service = XPService()
