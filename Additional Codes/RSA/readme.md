## RSA (Rivest–Shamir–Adleman) 

RSA (Rivest–Shamir–Adleman) is one of the first public-key cryptosystems and is widely used for secure data transmission. In such a cryptosystem, the encryption key is public and it is different from the decryption key which is kept secret (private). In RSA, this asymmetry is based on the practical difficulty of the factorization of the product of two large prime numbers, the "factoring problem". The acronym RSA is made of the initial letters of the surnames of Ron Rivest, Adi Shamir, and Leonard Adleman, who first publicly described the algorithm in 1978. Clifford Cocks, an English mathematician working for the British intelligence agency Government Communications Headquarters (GCHQ), had developed an equivalent system in 1973, but this was not declassified until 1997.

A user of RSA creates and then publishes a public key based on two large prime numbers, along with an auxiliary value. The prime numbers must be kept secret. Anyone can use the public key to encrypt a message, but with currently published methods, and if the public key is large enough, only someone with knowledge of the prime numbers can decode the message feasibly. Breaking RSA encryption is known as the RSA problem. Whether it is as difficult as the factoring problem remains an open question.

> For further reading click [here](https://en.wikipedia.org/wiki/RSA_(cryptosystem))


___

### Requirenments : 
##### 1. Python3
you can get it from [here](https://www.python.org/downloads/)

___

### Sequence of execution : 
##### `1. $ python3 RsaPublicKeyDist.py`
##### `2. $ python3 RsaSender.py`
##### `3. $ python3 RsaReceiver.py`
