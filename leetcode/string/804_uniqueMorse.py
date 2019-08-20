def uniqueMorseRepresentations(words):
    morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
             "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
             "..-", "...-", ".--", "-..-", "-.--", "--.."]
    d = []
    for i in words:
        tmp = []
        for j in i:
            tmp.append(morse[ord(j) - ord('a')])
        d.append(''.join(tmp))
        print(tmp)
    return len(set(d))

words = ["gin", "zen", "gig", "msg"]
len_ = uniqueMorseRepresentations(words)
print(len_)
