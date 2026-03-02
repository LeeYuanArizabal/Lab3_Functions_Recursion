def monitor(func):
    def wrapper(*args, **kwargs):
    
        if func.__name__ == "signal_shutdown":
            print("Authorization Started") 
            res = func(*args, **kwargs)
            print("Authorization Completed")
        else:
            print("Processing Started")    
            res = func(*args, **kwargs)
            print("Processing Completed")
        return res
    return wrapper

@monitor
def signal_shutdown(power):
    print(f"Current signal strength: {power}")
    if power <= 0:
        return 0
    return 1 + signal_shutdown(power - 1)

def play_count_stream(limit):
    for i in range(limit + 1):
        if i % 2 == 0:
            yield i ** 2