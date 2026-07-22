class Solution:
    def compress(self, chars: List[str]) -> int:
        j = 0
        i = 0
        while i < (len(chars)):
            count = 1
            k = i + 1
            while k < len(chars) and chars[i] == chars[k]:
                count += 1
                k += 1
                print(i, chars[i], count)

            chars[j] = chars[i]
            j += 1

            if count > 1:
                c = str(count)
                print(count)
                for char in c:
                    chars[j] = (char)
                    j += 1

            i = k

        return j