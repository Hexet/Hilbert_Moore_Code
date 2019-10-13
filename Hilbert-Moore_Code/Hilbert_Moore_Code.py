from cipher import Cipher
import os

f = open('initial_sequence.txt')
initial_s = f.readline()
f.close()
f = open('alphabet.txt')
line = f.readline()
alphabet = line.split(',')
f.close()

print("1 Равномерное распределение")
print("2 P1(A)")
print("3 P2(A)")
print("4 Выход из прошраммы")
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
coded_s = s.coding(initial_s)
decoded_s = s.decoding(coded_s)
f = open('coded_sequence.txt', 'w')
f.write(coded_s)
f.close()
f = open('decoded_sequence.txt', 'w')
f.write(decoded_s)
f.close()
print("средняя длина кодового слова:", s.average_codeword_length())
print("избыточность:", s.redundancy(s.average_codeword_length()))
print("неравенство Крафта:", s.craft_inequality())
print("закодированная последовательность:", coded_s)
print("длина закодированной последовательности:", len(coded_s))