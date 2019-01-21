import unittest
import pontos

class TestStringMethods(unittest.TestCase):

    def test_pontos(self):
        self.assertEqual(pontos.pontos(1,4,1,5), 5)

if __name__ == '__main__':
    unittest.main()
