import time

zaman = time.time()  # Epoch, from 1 Jan 1970
print(zaman)

zaman = time.ctime()
print(zaman)

zaman = time.localtime()
zaman_two = time.asctime(zaman)
print(zaman_two)

zaman = time.strftime("%d:%m:%Y %H:%M:%S")
print(zaman)

for i in range(3, 0, -1):
    print(i)
    time.sleep(1)

s = time.strftime("%a, %d %b %Y %H:%M:%S")
print("Example:", s)
