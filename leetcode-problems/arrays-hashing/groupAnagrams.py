# Key py trick to remember is that a hashmap(dict) can store list as values

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            # can easily check if something is a KEY in a hashmap
            if sorted_word not in words:
                words[sorted_word] = []

            words[sorted_word].append(word)
    
        final_list = []
        for key in words:
            final_list.append(words[key])

        # Could also just do return list(words.values())

        return final_list



             



