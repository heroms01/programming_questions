import unittest
import heapq

class TestCase(unittest.TestCase):
	def test_1(self):
		s = [1, 2, 3, 9, 10, 12]
		k = 7
		r = 2
		self.assertEqual(solution(s, k), r)

def solution(s, k):
	max_loop_count = len(s)
	heapq.heapify(s)
	count = 1

	while count < max_loop_count:
		heapq.heappush(s, (heapq.heappop(s) + (heapq.heappop(s) * 2)))
		last = s[0]

		if last >= k:
			break
		count += 1

	if count == max_loop_count:
		count = -1

	return count

unittest.main()