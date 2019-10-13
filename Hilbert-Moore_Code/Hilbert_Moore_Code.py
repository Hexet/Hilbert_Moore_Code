from cipher import Cipher
import os

f = open('alphabet.txt')
line = f.readline()
alphabet = line.split(',')
f.close()


print("1 Равномерное распределение")
print("2 P1(A)")
print("3 P2(A)")
print("4 Выход из программы")
n = True
while n:
    choice_p = input("Выберите распределение вероятностей: ")
    n = False
    if choice_p == "1":
        probabilities = []
        for i in range(len(alphabet)):
            probabilities += [1.0/len(alphabet)]
    elif choice_p == "2":
        f = open('probabilities_1.txt')
        line = f.readline()
        probabilities = line.split(',')
        f.close()
    elif choice_p == "3":
        f = open('probabilities_2.txt')
        line = f.readline()
        probabilities = line.split(',')
        f.close()
    elif choice_p == "4":
        quit()
    else: n = True

clear = lambda: os.system('cls')
clear()


s = Cipher(probabilities, alphabet)


print("1 Кодирование")
print("2 Декодирование")
print("3 Выход из программы")
flag = True
while flag:
    choice_w = input("Выберите режим работы: ")
    flag = False
    if choice_w == "1":
        clear = lambda: os.system('cls')
        clear()
        f = open('initial_sequence.txt')
        initial_s = f.readline()
        f.close()
        coded_s = s.coding(initial_s)
        f = open('coded_sequence.txt', 'w')
        f.write(coded_s)
        f.close()
        clear = lambda: os.system('cls')
        clear()
        print("закодированная последовательность:", coded_s)
        print("длина закодированной последовательности:", len(coded_s))

    elif choice_w == "2":
        clear = lambda: os.system('cls')
        clear()
        f = open('coded_sequence.txt')
        coded_s = f.readline()
        f.close()
        decoded_s = s.decoding(coded_s)
        f = open('decoded_sequence.txt', 'w')
        f.write(decoded_s)
        f.close()
        clear = lambda: os.system('cls')
        clear()
        print("декодированная последовательность:", decoded_s)

    elif choice_w == "3":
        quit()
    else: flag = True


print("средняя длина кодового слова:", s.average_codeword_length())
print("избыточность:", s.redundancy(s.average_codeword_length()))
print("неравенство Крафта:", s.craft_inequality())