import os

def main():
    ceva = os.popen("gdrive upload capture_19Jul19-22:34.jpg --share", 'r', 1)
    print(ceva)

if __name__ == "__main__":
    main()
