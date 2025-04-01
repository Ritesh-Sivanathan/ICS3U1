import time

text = "abc"

for char in text:
    print(char, end="", flush=True)
    time.sleep(0.2)