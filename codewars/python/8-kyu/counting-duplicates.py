def duplicate_count(text):
    text=text.lower()
    counts={}
    for ch in text:
        counts[ch]=counts.get(ch,0)+1
    return sum (1 for c in counts.values() if c > 1)
    
     
import codewars_test as test
from solution import duplicate_count

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(duplicate_count(""),        0, 'duplicate_count("")'       )
        test.assert_equals(duplicate_count("abcde"),   0, 'duplicate_count("abcde")'  )
        test.assert_equals(duplicate_count("abcdeaa"), 1, 'duplicate_count("abcdeaa")')
        test.assert_equals(duplicate_count("abcdeaB"), 2, 'duplicate_count("abcdeaB")')
        
        test.assert_equals(duplicate_count("Indivisibilities"), 2, 'duplicate_count("Indivisibilities")')
