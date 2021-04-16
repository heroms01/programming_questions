import unittest

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution([2,1,3,4,1]), [2,3,4,5,6,7])
        self.assertEqual(solution([5,0,2,7]), [2,5,7,9,12])


def solution(numbers):
    answer = set()
    
    for i, v in enumerate(numbers):
    	for i2, v2 in enumerate(numbers):
    		if i != i2:
	    		answer.add(v+v2)
    
    return list(sorted(answer))


unittest.main()
