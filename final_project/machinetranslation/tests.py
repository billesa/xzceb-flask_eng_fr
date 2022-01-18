import unittest

from translator import english_to_french, french_to_english

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        #self.assertRaises(ValueError('text must be provided'), english_to_french(None)) # test when None is given as input the output is None.
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # test when 'Hello' is given as input the output is 'Bonjour'.
        

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        #self.assertRaises(ValueError('text must be provided'), french_to_english(None)) # test when None is given as input the output is None.
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test when 'Bonjour' is given as input the output is 'Hello'.

unittest.main()