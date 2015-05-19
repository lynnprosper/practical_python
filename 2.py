database = [
	['albert', '1234']
]

username = raw_input('user  name: ')
pin = raw_input('pin code: ')
if [username, pin] in database:
	print 'access granted'