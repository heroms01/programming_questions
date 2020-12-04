import unittest

class TestCase(unittest.TestCase):
	def test_1(self):
		p = [1, 2, 3, 2, 3]	
		r = [4, 3, 1, 1, 0]
		self.assertEqual(solution(p), r)

		
def solution(prices):
	answer = []
	cnt = len(prices)
	for pi, pv in enumerate(prices):
		if pi >= len(answer):
			answer.append(0)
		for i in range(pi+1, cnt):
			answer[pi] += 1		
			if prices[i] < pv:
				break
					
	return answer
	
unittest.main()
