import time

count = 10
while count > 0:
    print(count)
    count -= 1
    time.sleep(1)  # Pauses for 1 second between counts

print("Time's up!")
