import sys,socket,thread
socket.setdefaulttimeout(0.5)
def connect(ip,port):
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		result=s.connect_ex((ip,port))
		if result==0:
			list.append(port)
		s.close()
if __name__=='__main__':
	print('Scanning...Please wait...')
	list=[]
	ip=sys.argv[1]
	for port in range(0,65535):
		thread.start_new_thread(connect,(ip,port))
	print ('The following port is open.')
	print list