class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
   
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        worddict = collections.defaultdict(list)
        for i in wordList:
            for j in range(len(i)):
                pattern = i[:j] + "#" + i[j+1:]
                worddict[pattern].append(i)
        
        visited = set(beginWord)
        q = deque([beginWord])
        count = 1
        while(q):
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return count
                for j in range(len(word)):
                    wordpattern = word[:j] + "#" + word[j+1:]
                    for nei in worddict[wordpattern]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            count+=1 
        return 0