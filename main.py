from string import ascii_lowercase

class Enigma:
    def __init__(self, steckerbrett = {" ":" "}, alpha=None, beta=None, gamma=None):
        self.alphabet = list(ascii_lowercase)
        self.steckerbrett = steckerbrett
        if type(steckerbrett) is not dict:
            self.steckerbrett = {" " : " "}
        if alpha != None   and beta != None and gamma != None:
            rotors = [alpha, beta, gamma]
            for rotor in rotors:
                if type(rotor) is  int or type(rotor) is  float:
                    rotor = rotor % 26
                else:
                    rotor = 0
        else:

            rotors = [alpha, beta, gamma]
            for rotor in rotors:
                if rotor == None or type(rotor) is not int or type(rotor) is not float:
                    rotor = 0
                else:
                    rotor = rotor % 26       
        self.alpha = rotors[0]
        self.beta = rotors[1]
        self.gamma = rotors[2]
        
        for letter in list(self.steckerbrett.keys()):
            if letter in self.alphabet:
                self.steckerbrett.update({self.steckerbrett[letter]:letter})

        self.reflector = [letter for letter in reversed(self.alphabet)]
    def permutate(self, rotor):
        
        new_alphabet = self.alphabet.copy()
        for iter in range(rotor):
            new_alphabet.insert(0, new_alphabet[-1])
            new_alphabet.pop(-1)
        return new_alphabet
    def inverse_permutation(self, rotor):
        
        new_alphabet = self.alphabet.copy()
        for iter in range(rotor):
            new_alphabet.append(new_alphabet[0])
            new_alphabet.pop(0)
          
        return new_alphabet

    def encrypt_text(self, text):
        encrypted_text = []
        text = text.lower()
        for letter in text:
            if letter in self.steckerbrett:
                new_letter=self.steckerbrett[letter]
                temp_letter = self.permutate(self.alpha)[self.alphabet.index(new_letter)]
                temp_letter = self.permutate(self.beta)[self.alphabet.index(temp_letter)]
                temp_letter = self.permutate(self.gamma)[self.alphabet.index(temp_letter)]
                temp_letter = self.reflector[self.alphabet.index(temp_letter)]
                temp_letter = self.inverse_permutation(self.gamma)[self.alphabet.index(temp_letter)]
                temp_letter = self.inverse_permutation(self.beta)[self.alphabet.index(temp_letter)]
                temp_letter = self.inverse_permutation(self.alpha)[self.alphabet.index(temp_letter)]
                if temp_letter in self.steckerbrett:
                    temp_letter=self.steckerbrett[temp_letter]
                encrypted_text.append(temp_letter)
                self.alpha += 1
                if self.alpha % len(self.alphabet) == 0:
                    self.beta += 1
                    self.alpha = 0
                if self.beta % len(self.alphabet) == 0 and self.alpha % len(self.alphabet) != 0:
                    self.gamma += 1
                    self.beta = 0
            else:
                if letter!=" ":
                    temp_letter = self.permutate(self.alpha)[self.alphabet.index(letter)]
                    temp_letter = self.permutate(self.beta)[self.alphabet.index(temp_letter)]
                    temp_letter = self.permutate(self.gamma)[self.alphabet.index(temp_letter)]
                    temp_letter = self.reflector[self.alphabet.index(temp_letter)]
                    temp_letter = self.inverse_permutation(self.gamma)[self.alphabet.index(temp_letter)]
                    temp_letter = self.inverse_permutation(self.beta)[self.alphabet.index(temp_letter)]
                    temp_letter = self.inverse_permutation(self.alpha)[self.alphabet.index(temp_letter)]
                    if temp_letter in self.steckerbrett:
                        temp_letter=self.steckerbrett[temp_letter]
                    encrypted_text.append(temp_letter)
                    self.alpha += 1
                    if self.alpha % len(self.alphabet) == 0:
                        self.beta += 1
                        self.alpha = 0
                    if self.beta % len(self.alphabet) == 0 and self.alpha % len(self.alphabet) != 0:
                        self.gamma += 1
                        self.beta = 1
                else:
                    encrypted_text.append(" ")
        return ''.join(encrypted_text)


Enigma = Enigma({"b":'a', 'l':'z'}, alpha=5, beta=17, gamma=24)
print(Enigma.encrypt_text('Mynka world'))


