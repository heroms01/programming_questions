import unittest

class TestCase(unittest.TestCase):
	def test_1(self):
		a1 = [1, 5, 2, 6, 3, 7, 4]
		a2 = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
		expect = [5, 6, 3]
		self.assertEqual(solution(a1, a2), expect)

		
def solution(array, cmds):
	answer = []
	for cmd in cmds:
		temp = array[cmd[0]-1:cmd[1]]
		temp.sort()
		answer.append(temp[cmd[2]-1])
		
	return answer
	
unittest.main()