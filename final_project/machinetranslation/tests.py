import unittest

from translator import englishToFrench, frenchToEnglish

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench(None), None) # test when None is given as input the output is None.
        self.assertEqual(englishToFrench('Hello'), 'Bonjour') # test when 'Hello' is given as input the output is 'Bonjour'.
        

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish(None), None) # test when None is given as input the output is None.
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') # test when 'Bonjour' is given as input the output is 'Hello'.

unittest.main()