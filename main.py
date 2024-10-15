'''
coucou
'''
import sys
sys.setrecursionlimit(2000)

def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne 
    de caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    if not s:
        return []

    result = []
    current_char = s[0]
    count = 1

    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = s[i]
            count = 1

    result.append((current_char, count))
    return result



def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne
     de caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    if not s:
        return []

    count = 1
    for i in range(1, len(s)):
        if s[i] != s[0]:
            break
        count += 1

    return [(s[0], count)] + artcode_r(s[count:])

def main():
    '''
    coucou
    '''
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
