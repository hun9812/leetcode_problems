class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) < 3:
            return False
        
        word = word.lower()
        con1 = False
        con2 = False

        for c in word:
            if c in 'aeiou':
                con1 = True
            elif c in 'bcdfghjklmnpqrstvwxyz':
                con2 = True
            elif c in '1234567890':
                pass
            else:
                return False
        
        if con1 is True and con2 is True:
            return True
        else:
            return False