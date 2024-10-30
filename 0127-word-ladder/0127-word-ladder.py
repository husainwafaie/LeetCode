class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        letters = "abcdefghijklmnopqrstuvwxyz"
        queue = deque()
        queue.append([beginWord, 1])
        found = set()
        found.add(beginWord)
        while queue:
            word, num = queue.popleft()
            if word == endWord:
                return num
            for i in range(len(word)):
                for letter in letters:
                    newword = word[:i] + letter + word[i+1:]
                    if newword in words and newword not in found:
                        queue.append([newword, num + 1])
                        found.add(newword)
        return 0