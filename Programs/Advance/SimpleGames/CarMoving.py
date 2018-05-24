import time

print ("\n\n\n\n\n\n")

while True:
	for a in range(113):
		print ("   {:>{pad}}./\.......\\\.\r\n".format("",pad=a),end="")
		print ("   {:>{pad}}/\,--, ~|~  ,--,`-,\r\n".format("",pad=a),end="")
		print ("   {:>{pad}}`( o )-----( 0 )--`\r\n".format("",pad=a),end="")
		print ("   {:>{pad}}  `-'       `-'\r\033[F\033[F\033[F".format("",pad=a),end="")
		time.sleep(.05)
		
		
#{:>{pad} for padding "" before string
#{0:>4} will do 4 size and right justified
#{0:>{pad}} will do pad size right justified

#\003[F is for cursor up
#\003[K is for clear upto cursor
