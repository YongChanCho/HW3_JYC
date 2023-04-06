def reverse(str):
    words=str.split()
    words.reverse()
    return " ".join(words)


str1="Two roads diverged in a yello wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth;"
str2="Then took the other, as just as fair, And having perhaps the better claim, Because it was grassy and wanted wear; Though as for that the passing there Had worm them really about the same,"

def main1():
    print(reverse(str1))

def main2():
    print(reverse(str2))

if __name__ == '__main__':
    main1()

if __name__ == '__main__':
    main2()