import urllib


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