import unittest

from palindromos import is_palindrome


class TestPalindrome(unittest.TestCase):
    def test_a(self):
        resultado = is_palindrome('a')
        self.assertEqual(resultado, True)

    def test_b(self):
        resultado = is_palindrome('B')
        self.assertEqual(resultado, True)

    def test_aa(self):
        resultado = is_palindrome('aa')
        self.assertEqual(resultado, True)

    def test_ab(self):
        resultado = is_palindrome('ab')
        self.assertEqual(resultado, False)

    def test_aCa(self):
        resultado = is_palindrome('aCa')
        self.assertEqual(resultado, True)

    def test_aCs(self):
        resultado = is_palindrome('aCs')
        self.assertEqual(resultado, False)

    def test_ABBA(self):
        resultado = is_palindrome('ABBA')
        self.assertEqual(resultado, True)

    def test_ABCA(self):
        resultado = is_palindrome('BACB')
        self.assertEqual(resultado, False)

    def test_ABCBA(self):
        resultado = is_palindrome('ABCBA')
        self.assertEqual(resultado, True)

    def test_ABCCBA(self):
        resultado = is_palindrome('ABCCBA')
        self.assertEqual(resultado, True)

    def test_ZBCCBA(self):
        resultado = is_palindrome('ZBCCBA')
        self.assertEqual(resultado, False)

    def test_neuquen(self):
        resultado = is_palindrome('neuquen')
        self.assertEqual(resultado, True)

    def test_neuqueM(self):
        resultado = is_palindrome('neuqueM')
        self.assertEqual(resultado, False)

    def test_Anita(self):
        resultado = is_palindrome('Anita')
        self.assertEqual(resultado, False)
    

    def test_pizza_con_queso(self):
        resultado = is_palindrome('pizza con queso')
        self.assertEqual(resultado, False)
    

    def test_Pizza_con_queso(self):
        resultado = is_palindrome('Pizza con queso')
        self.assertEqual(resultado, False)
    

    def test_Estoy_en_casa(self):
        resultado = is_palindrome('Estoy en casa')
        self.assertEqual(resultado, False)


    def test_ESTOY_EN_CASA(self):
        resultado = is_palindrome('ESTOY EN CASA')
        self.assertEqual(resultado, False)


    def test_yo_soy(self):
        resultado = is_palindrome('yo soy')
        self.assertEqual(resultado, True)

    
unittest.main()