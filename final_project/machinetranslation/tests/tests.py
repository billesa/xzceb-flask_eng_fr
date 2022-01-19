import unittest

from translator import english_to_french, french_to_english

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(english_to_french('None'), '') # test when None is given as input the output is ''.
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # test when 'Hello' is given as input the output is 'Bonjour'.
        

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(french_to_english('None'), '') # test when None is given as input the output is ''.
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test when 'Bonjour' is given as input the output is 'Hello'.

unittest.main()