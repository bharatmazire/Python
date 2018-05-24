import time

print ("\n\n\n\n\n\n\n")
while True:
	for i in range(100):
		print ("{0:>{pad}} /```````||``````\\\r\n".format("",pad=i),end="")
		print ("{0:>{pad}}======================\\\r\n".format("",pad=i),end="")
		print ("{0:>{pad}}|  ,--.  || ,--.       \\ \r\n".format("",pad=i),end="")
		print ("{0:>{pad}}==(    )===(    )========\r\n".format("",pad=i),end="")
		print ("{0:>{pad}}   `--'     `--'  \r".format("",pad=i),end="")
		print ("\r\033[F\033[F\033[F\033[F\033[F")
		time.sleep(0.1)
