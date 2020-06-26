import sys
for line in sys.stdin:

    line = line.strip()
    words = line.split()
    print(line)
    print(words)
    for word in words:
        print(word)
