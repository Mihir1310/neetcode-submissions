class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash1 = defaultdict(list)

        for s in strs:
            arr = [0] * 26
            for i in s:
                arr[ord(i) - ord("a")] += 1

            hash1[tuple(arr)].append(s)

        return list(hash1.values())