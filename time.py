import time
timeout = time.time() + 60*(1/6)   # 5 minutes from now
while True:
    test = 0
    if test == 5 or time.time() > timeout:
        break
    test = test - 1