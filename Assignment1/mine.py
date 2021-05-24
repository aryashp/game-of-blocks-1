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
    if res1.startswith('0000'):
        print(f'congratulations possible padding is {padding} , lets become rich')
        break
    padding+=1

end = time.time()
print(f' execution time : {end-start} seconds')