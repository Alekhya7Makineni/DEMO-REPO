import unittest
def upper(str):
    return str.upper()
def lower(str):
    return str.lower()
def uppercheck(str):
    if isupper(str):
        return True
def lowercheck(str):
    if islower(str):
        return True
class TestMethods(unittest.TestCase):
    def test_1(self):
        result=upper('abc')
        self.assertEqual(result,'ABC')
    def test_2(self):
        result=lower('ABC)
        self.assertEqual(result,'abc')
    def test_3(self):
        result=uppercheck('ABC')
        
                     
if __name__ == '__main__':
    unittest.main()                     
