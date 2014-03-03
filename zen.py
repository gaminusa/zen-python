import urllib


print ("Ingrese comando:")
com = raw_input()

if com == 'zen_python':
	try:  
    		f = urllib.urlopen("https://api.github.com/zen")  
    		print f.read()  
    		f.close()  
	except HTTPError, e:  
    		print "Ocurrio un error"  
    		print e.code  
	except URLError, e:  
    		print "Ocurrio un error"  
    		print e.reason  
else:
	print ("Comando invalido")