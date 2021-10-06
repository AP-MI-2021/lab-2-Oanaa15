def get_base_16_from_2(n):
    '''
    transforma un numar din baza 2 in baza 16
    :param n: nr. in baza 2
    :return: numarul n in baza 16
    '''
    zece = 0 # nr in baza 10
    p10 = 1
    while n!=0:   # transformam din baza 2 in baza 10
        zece = zece + (n%10) * p10   # la 10 se aduna pe rand ultima cifra *p10
        p10 = p10 * 2
        n = n // 10     # scapam de ultima cifra

    put10 = 1  # put10=1,10, 100, 1000, ...
    in16 = 0     # nr in baza 16
    while zece!= 0 :    # transformam nr din baza 10 in baza 16
        in16 = in16 + (zece%16) *put10 # la in16 se adauga restul n%16 * put10
        zece = zece // 16
        put10 = put10 * 10   # put10 se mareste de 10 ori
    return in16

def test_get_base_16_from_2():
    assert get_base_16_from_2(111) == 7
    assert get_base_16_from_2(1000) == 8
    assert get_base_16_from_2(1001) == 9


def get_n_chose_k(n, k):
    '''
    calculeaza combinari de n luate cate k
    :param n: nr. intreg
    :param k: nr intreg
    :return: combinari de n luate cate k
    '''
    if k > n:
        return False
    if k == 0 or k == n:
        return 1
    if k == n:
        return n
    c = 1
    for i in range (1, k+1):
        c = c*(n-i+1)//i   # aplicam formula combinarilor de n luate cate k
    return c

def test_get_n_choose_k():
    assert get_n_chose_k(3, 6) is False
    assert get_n_chose_k(3, 2) == 3
    assert get_n_chose_k(3, 0) == 1

def is_palindrome(n):
    '''
    verifica daca un numar e palindrom
    :param n: nr. intreg
    :return: True daca nr. e palindrom sau False in caz contrar
    '''
    copie=n
    og=0
    while copie != 0:
        og = og *10 + copie%10
        copie = copie//10
    if n == og:
        return True
    return False

def test_is_palindrome():
    assert is_palindrome(121) == True
    assert is_palindrome(77) == True
    assert is_palindrome(26) == False

def main():
    shouldRun = True
    while shouldRun:
        print("1. transformare din baza 2 in baza 16")
        print("2. Combinari de n luate cate k")
        print("3. Verifica daca un numar este palindrom")

        optiune = input("Dati optiunea: ")
        if optiune == "1":
            test_get_base_16_from_2()
            a = int(input("Dati numar: "))

            print(get_base_16_from_2(a))
        elif optiune == "2":
            test_get_n_choose_k()
            n = int(input("Dati un nr."))
            k = int(input("Dati un nr."))

            print(get_n_chose_k(n, k))
        elif optiune == "3":
            test_is_palindrome()
            nr = int(input("Dati numar: "))
            print(is_palindrome(nr))

        elif optiune == "x":
            shouldRun = False
        else:
            print("Optiune gresita! Reincercati!")
if __name__ == '__main__':
  main()





