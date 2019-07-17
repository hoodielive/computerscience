def anagram(s1, s2):
    s1.replace(' ', '').lower()
    s2.replace(' ', '').lower()

    # compensate for Edge case
    if len(s1) != len(s2):
        return False

    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1


    for k in count:
        if count[k] != 0:
            return False


    return True


assert anagram('clint eastwood', 'old west action') == False