class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            char_frequency = [0]*26
            for char in string:
                c = ord(char)-97
                char_frequency[c]+=1
            freq = tuple(char_frequency)
            if freq not in anagrams:
                anagrams[freq] = []
            anagrams[freq].append(string) 
        print(anagrams)
        return list(anagrams.values())