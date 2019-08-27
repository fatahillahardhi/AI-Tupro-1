import random
import math

#rumus
def objektif(x1,x2):
  return -abs(math.sin(X1)*math.cos(X2)*math.exp(abs(1-(math.sqrt(((X1)*(X1))+((X2)*(X2)))/math.pi))))

#rumus random dengan range -10,10
def generate():
  return random.uniform(-10,10)

X1 = generate()
X2 = generate()

#deklarasi variable X1B dan X2B
X1B = X1
X2B = X2

#EB dan E dimasukan rumus 
EB = objektif(X1B,X2B)
E  = objektif(X1,X2)

#temperature
T = 500

#looping temperature sampai kurang dari 0
while T > 0:
  #deklarasi X1N dan X2N
  X1N = X1 + generate()
  X2N = X2 + generate()
  
  #looping pengecekan bahwa X1N dan X2N harus kurang dari range (-10,10)
  while ((X1N >= 10) or (X1N <= -10)) or ((X2N >= 10) or (X2N <= -10)):
    #deklarasi X1N dan X2N yang telah melalui proses pengecekan
    X1N = X1 + generate()
    X2N = X2 + generate()
  
  #En dimasukan rumus
  En  = objektif(X1N,X2N)
  
  #deltaE dihasilkan dari En - E
  dE  = En - E
  
  #kondisi jika dE kurang dari 0
  if dE<0:
    X1 = X1N
    X2 = X2N
    E  = En
    if En<EB:
      X1B = X1N
      X2B = X2N
      EB  = En
  #kondisi jika dE tidak kurang dari 0
  else:
    P = math.exp(-dE/T)
    R = random.random()
    if R<P:
      X1 = X1N
      X2 = X2N
  T = T - 0.1
print("X1 Best = ",X1B,"\nX2 Best = ",X2B,"\nE Best  = ",EB)