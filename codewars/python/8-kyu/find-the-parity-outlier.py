def find_outlier(integers):
    odd=[n for n in integers[:3] if n %2 !=0]
    even=[n for n in integers[:3] if n %2==0]
    
    if len(even)==1:
        return even[0]
    if len(odd)==1:
        return odd[0]
    if len(odd) > len(even):
        return next(n for n in integers if n %2==0)
    else:
        return next(n for n in integers if n %2!=0)
import codewars_test as test
from solution import find_outlier

@test.describe("Sample Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def _():
        test.assert_equals(find_outlier([2, 4, 6, 8, 10, 3]), 3, 'For input: [2, 4, 6, 8, 10, 3]')
        test.assert_equals(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11, 'For input: [2, 4, 0, 100, 4, 11, 2602, 36]')
        test.assert_equals(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160, 'For input: [160, 3, 1719, 19, 11, 13, -21]')
    
    @test.it("More complex tests")
    def _():
        test_cases = [
            ([2,6,8,10,3], 3), # odd at the back
            ([2,6,8,200,700,1,84,10,4], 1), # odd in the middle
            ([17,6,8,10,6,12,24,36], 17), # odd in the front