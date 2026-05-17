def validate_email(email):
    if "@" in email:
        raise ValueError ('valid email')
    if len(email) >= 8:
        return True
        
    return False
