import unittest

class User:
	def __init__(self):
		pass


class TestUser(unittest.TestCase):
	def setUp(self):
		self.user = User()

	def testranking(self):
		self.assertEqual(self.user.rank, -8)
		self.assertEqual(self.user.progress, 0)
		user.inc_progress(-7)
		self.assertEqual(self.user.progress, 10)
		user.inc_progress(-5)
		self.assertEqual(self.user.progress, 0)
		self.assertEqual(self.user.rank, -7)


if __name__ == '__main__':
	unittest.main()