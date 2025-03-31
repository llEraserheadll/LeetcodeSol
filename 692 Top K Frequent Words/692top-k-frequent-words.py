class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_count = Counter(words)

        max_heap = [(-count,words) for words,count in words_count.items()]
        heapify(max_heap)

        result = []
        for _ in range(k):
            i,word = heappop(max_heap)
            result.append(word)
        
        return result