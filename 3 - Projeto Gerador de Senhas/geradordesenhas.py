import random, string

tamanho = 16

chars = string.ascii_letters + string.digits + string.digits + '!@#&*%$-=+()' #composição da senha

rnd = random.SystemRandom() #os.urandom
print(''.join(rnd.choice(chars) for i in range (tamanho)))

