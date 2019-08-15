
def detectCapitalUse(word: str) -> bool:
    if word.islower() or word.istitle() or word.isupper():
        return True
    else:
        return False