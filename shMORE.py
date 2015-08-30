# $language = "python"
# $interface = "1.0"

# Changes the pagination and does a 'more system:running'

def Main():
	crt.Screen.Synchronous = True
	crt.Screen.Send("terminal pager 0" + chr(13))
	crt.Screen.WaitForString(chr(13) + "#")
	crt.Screen.Send("more system:running-config" + chr(13))
	crt.Screen.WaitForString(chr(13) + "#")	
	crt.Screen.Send("terminal pager 24" + chr(13))

Main()
