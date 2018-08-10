import unittest
import account as AccountClass 

class Test(unittest.TestCase):
	accInfo = AccountClass.account()
	
	def test_check_password_length(self):
		print("Checking possible password\n")
		passwordList = ['dsasdsdfewe', 'dsdsdfwefwe', 'sdsfweadwefwe']

		for passwd in passwordList:
			print("checking password " + passwd + "\n")
			passinfo = self.accInfo.check_password_length(passwd)
			self.assertTrue(passinfo)


if __name__ == '__main__' :
	unittest.main()
