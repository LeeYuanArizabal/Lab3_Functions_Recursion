# main.py

import grades

# Student Identity Configuration
LAST_NAME = "Arizabal"
STUDENT_ID = "TUPM-25-0167"

SEED_DIGIT = int(STUDENT_ID[-1])
ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())
NAME_LENGTH = len(LAST_NAME)

# Generate student-unique scores

scores = [
    SEED_DIGIT * 10,
    ID_SUM % 100,
    NAME_LENGTH * 7
]

average = grades.compute_average(scores)
grade = grades.assign_grade(average)
remark = grades.generate_remark(grade)

print("=" * 40)
print(f"Student: {LAST_NAME}")
print(f"Student ID: {STUDENT_ID}")
print(f"Generated Scores: {scores}")
print(f"Average: {round(average,2)}")
print(f"Grade: {grade}")
print(f"Remark: {remark}")
print("+" * 40)

SEED_NUM = 7
FAVORITE_ARTIST = "THE 1975"
CONTROL_NUM = max(1, SEED_NUM)

import access_control as ac
import media_engine as me

SEED_NUM = 7 
CONTROL_NUM = max(1, SEED_NUM)
FAVORITE_ARTIST = "DAFT PUNK"
ARTIST_LEN = len(FAVORITE_ARTIST)

print(f"--- EXERCISE 1: ACCESS CONTROL ---")
level = ac.compute_access_level(CONTROL_NUM, FAVORITE_ARTIST)
decision = ac.validate_access(level, CONTROL_NUM)
print(f"Level: {level} | Decision: {decision}\n")

print(f"--- EXERCISE 2: SIGNAL SHUTDOWN ---")
initial_power = CONTROL_NUM + ARTIST_LEN
total_calls = me.signal_shutdown(initial_power)
print(f"Total Recursive Calls: {total_calls}\n")

print(f"--- EXERCISE 3: MEDIA ANALYTICS ---")
stream_limit = CONTROL_NUM + ARTIST_LEN
@me.monitor
def run_analytics(limit):
    counts = list(me.play_count_stream(limit))
    return counts

generated_counts = run_analytics(stream_limit)
print(f"Generated Counts: {generated_counts}")
print(f"Total Plays: {sum(generated_counts)}")
print(f"Records Processed: {len(generated_counts)}")