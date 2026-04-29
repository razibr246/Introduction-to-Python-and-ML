def create_character(name, strength, intelligence, charisma):
    # ---- Name validation ----
    if not isinstance(name, str):
        return "The character name should be a string."
    
    if name == "":
        return "The character should have a name."
    
    if len(name) > 10:
        return "The character name is too long."
    
    if " " in name:
        return "The character name should not contain spaces."
    
    # ---- Stats validation ----
    stats = [strength, intelligence, charisma]
    
    # Check integers
    if not all(isinstance(stat, int) for stat in stats):
        return "All stats should be integers."
    
    # Check minimum
    if not all(stat >= 1 for stat in stats):
        return "All stats should be no less than 1."
    
    # Check maximum
    if not all(stat <= 4 for stat in stats):
        return "All stats should be no more than 4."
    
    # Check total points
    if sum(stats) != 7:
        return "The character should start with 7 points."
    
    # ---- Build character output ----
    def build_stat_line(label, value):
        full = "●" * value
        empty = "○" * (10 - value)
        return f"{label} {full}{empty}"
    
    result = (
        f"{name}\n"
        f"{build_stat_line('STR', strength)}\n"
        f"{build_stat_line('INT', intelligence)}\n"
        f"{build_stat_line('CHA', charisma)}"
    )
    
    return result
