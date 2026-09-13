def solution(s):
    if len(s) % 2 !=0:
      s += '_'
    return [s[i:i+2] for i in range(0, len(s),2)]
import codewars_test as test
from solution import *

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        tests = (
            ("asdfadsf", ['as', 'df', 'ad', 'sf']),
            ("asdfads", ['as', 'df', 'ad', 's_']),
            ("", []),
            ("x", ["x_"]),
        )

        for inp, exp in tests:
            test.assert_equals(solution(inp), exp)