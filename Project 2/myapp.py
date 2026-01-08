import time

from datetime import datetime
 
FILE_PATH = "/tmp/log.txt"
 
while True:

    with open(FILE_PATH, "a") as f:

        f.write(f"Hi this Barani Gopal use python  {datetime.now()}\n")

    print("All the best")

    time.sleep(5)
 
