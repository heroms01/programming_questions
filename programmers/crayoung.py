import unittest

class TestCase(unittest.TestCase):
	def test1(self):
		self.assertEqual(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]), 4)
		self.assertEqual(solution([[0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 2, 1, 0, 0], [0, 2, 1, 0, 0], [0, 2, 1, 0, 0]], [1, 2, 3, 3, 2, 3, 1]), 4)

def solution(board, moves):
	answer = 0
	basket = []
	for col in moves:
		col = col - 1
		index = 0
		while board[len(board)-1][col] != 0 and board[index][col] == 0:
			index += 1

		if basket and basket[len(basket)-1] == board[index][col]:
			answer += 2
			basket.pop()
		elif board[index][col] != 0:
			basket.append(board[index][col])

		board[index][col] = 0

	return answer

unittest.main()
