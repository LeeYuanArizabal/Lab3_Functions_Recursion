def audit_log(func):
    def wrapper(*args, **kwargs):
        print("Authorization Started")
        result = func(*args, **kwargs)
        print("Authorization Completed")
        return result
    return wrapper

def compute_access_level(control, artist_name):
    return (control * 3) + len(artist_name)

@audit_log
def validate_access(level, control):
    threshold = control * 5
    if level >= threshold:
        return "ACCESS GRANTED"
    else:
        return "ACCESS DENIED"
    