class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        need = [0] * 26
        window = [0] * 26
        a = ord('a')

        for i in range(n1):
            need[ord(s1[i]) - a] += 1
            window[ord(s2[i]) - a] += 1

        matches = sum(1 for i in range(26) if need[i] == window[i])

        if matches == 26:
            return True

        for i in range(n1, n2):
            add_idx = ord(s2[i]) - a
            rem_idx = ord(s2[i - n1]) - a

            # add new char
            window[add_idx] += 1
            if window[add_idx] == need[add_idx]:
                matches += 1
            elif window[add_idx] == need[add_idx] + 1:
                matches -= 1

            # remove old char
            window[rem_idx] -= 1
            if window[rem_idx] == need[rem_idx]:
                matches += 1
            elif window[rem_idx] == need[rem_idx] - 1:
                matches -= 1

            if matches == 26:
                return True

        return False
        