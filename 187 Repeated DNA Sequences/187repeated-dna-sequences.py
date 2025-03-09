class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        string_length = len(s)
        k = 10
        if string_length < k:
            return list(set())


        mapping = {'A' : 1, 'C' : 2,'G' : 3 , 'T' : 4}
        base_value = 4
        numbers = []

        for m in range(string_length):
            numbers.append(mapping.get(s[m]))

        hash_value = 0
        hash_set = set()
        output = set()

        for i in range(string_length - k + 1):
            if i == 0:
                for j in range(k):
                    hash_value += numbers[j]*(base_value**(k-j-1))
            
            else:
                previous = hash_value
                hash_value = (previous - numbers[i-1]*(base_value**(k - 1)))*base_value + numbers[i+k- 1]

            
            if hash_value in hash_set:
                output.add(s[i : i+k])
            
            hash_set.add(hash_value)

        return list(output)

        