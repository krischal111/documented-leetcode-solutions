def hash_mapify(word):
    hmap = {}
    for letter in word:
        if letter in hmap:
            hmap[letter] += 1
        else:
            hmap[letter] = 1
    return hmap

def word_formed_by_hmap(word, hmap):
    word_map = hash_mapify(word)
    for letter, count in word_map.items():
        if letter not in hmap or count > hmap[letter]:
            return False
    return True

class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        hmap = hash_mapify(chars)
        i = 0
        for word in words:
            if word_formed_by_hmap(word, hmap):
                i += len(word)
        return i
        