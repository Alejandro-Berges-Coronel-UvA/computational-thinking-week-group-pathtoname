import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'utility', 'edutest'))
import edutest

class Test_Exercise_Values(edutest.TestCase):
    def test(self):
        self.io_pair(('00:01', 5, '1990-01-01', 3, 1, 'Alexandra', 9, 'a+b'),1.50816470189193e+16)
        self.io_pair(('00:02', 6, '1990-01-02', 4, 2, 'Alexandra', 8, 'b+c'),7.241826719742992e+16)
        self.io_pair(('00:03', 7, '1990-01-03', 5, 3, 'Alexandra', 7, 'd*e'),9.116784517346144e+16)

class Test_Exercise(edutest.TestSuite):
    test_cases = [
        Test_Exercise_Values
    ]
