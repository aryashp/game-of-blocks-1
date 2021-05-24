import hashlib
import time

start = time.time()

data = input("what is the concatenation of previous block's hash and transactions to be included in next block\n")

padding=1
while True:
    x = data + str(padding)
    #print(x)
    res = hashlib.sha256(x.encode())
    res1 = res.hexdigest();
    #print(res1)
    padding+=1
    if res1.startswith('00000'):
        print(f'congratulations possible padding is {padding} , lets become rich')
        break

end = time.time()
print(f' execution time : {end-start} seconds')