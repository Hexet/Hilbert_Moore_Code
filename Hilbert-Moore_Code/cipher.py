import numpy as np
import string
from math import copysign, fabs, floor, isfinite, modf, log2, ceil

def float_to_bin_fixed(f):
    if not isfinite(f):
        return repr(f)  # inf nan

    sign = '-' * (copysign(1.0, f) < 0)
    frac, fint = modf(fabs(f))  # split on fractional, integer parts
    n, d = frac.as_integer_ratio()  # frac = numerator / denominator
    assert d & (d - 1) == 0  # power of two
    return f'{sign}{floor(fint):b}.{n:0{d.bit_length()-1}b}'

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

class Cipher(object):
    def __init__(self, probabilities, alphabet):
        self.alphabet = alphabet
        self.alphabet_size = len(self.alphabet)
        self.p = np.zeros(self.alphabet_size, dtype = float)
        for i in range(self.alphabet_size):
            self.p[i] = float(probabilities[i])
        self.coded_alphabet = []

    def coding(self, initial_s):
        q = np.zeros(self.alphabet_size, dtype = float)
        for i in range(1, self.alphabet_size):
            q[i] += self.p[i - 1] + q [i - 1]
        s = np.zeros(self.alphabet_size, dtype = float) # sigma
        for i in range(self.alphabet_size):
            s[i] = q[i] + self.p[i] / 2
        l = np.zeros(self.alphabet_size, dtype = float)
        for i in range(self.alphabet_size):
            l[i] = ceil(-1 * log2(self.p[i]/2))
        
        for i in range(self.alphabet_size):
            self.coded_alphabet += [toFixed(float(float_to_bin_fixed(s[i])), int(l[i])).split(".")[1]]
        coded_s = []
        for i in range(len(initial_s)):
            j = self.alphabet.index(initial_s[i])
            coded_s += [self.coded_alphabet[j]]
        print(self.coded_alphabet)
        return "".join(coded_s)
    
    def average_codeword_length(self):
        L = 0.0
        for i in range(self.alphabet_size):
            L += self.p[i] * len(self.coded_alphabet[i])
        return L
    
    def redundancy(self, average_codeword_length):
        H = 0.0
        for i in range(self.alphabet_size):
            H += self.p[i] * log2(self.p[i])
        H *= -1
        return average_codeword_length - H

    def craft_inequality(self):
        LI = 0.0
        for i in range(self.alphabet_size):
            LI += 2 ** (-1 * len(self.coded_alphabet[i]))
        return LI < 1

    #def decoding(self, coded_s):
        
    #    return initial_s


    def decoding(self, coded_s):
        f = open('initial_sequence.txt')
        initial_s = f.readline()
        f.close()
        return initial_s