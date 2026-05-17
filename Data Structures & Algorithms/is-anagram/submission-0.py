class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)

        s_list.sort()
        t_list.sort()
        new_s = str(s_list)
        new_t = str(t_list)
        if new_s == new_t:
            return True
        else:
            return False
          