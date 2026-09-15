def rot13(message):
    result=[]
    for ch in message:
        if ch.isupper():
            result.append(chr((ord(ch)- ord('A') + 13) % 26 + ord('A')))
        elif ch.islower():
            result.append(chr((ord(ch)- ord('a') + 13) % 26 + ord('a')))
        else:
            result.append(ch)
    return ''.join(result)
       
  

from solution import rot13

@test.describe("Fixed tests")
def tests():
        
    @test.it("Should obtain correct Rot13 encoding on fixed strings")
    def test_rot13_fixed_strings():
        test.assert_equals(rot13('test'), 'grfg', 'Returned solution incorrect for fixed string = test')
        test.assert_equals(rot13('Test'), 'Grfg', 'Returned solution incorrect for fixed string = Test')
        test.assert_equals(rot13('aA bB zZ 1234 *!?%'), 'nN oO mM 1234 *!?%', 'Returned solution incorrect for fixed string = aA bB zZ 1234 *!?%')