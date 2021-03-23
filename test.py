import os 
f = open("potato.txt", 'w+')
f.write(f"running test 12 in {os.listdir()}")
f.close()
print(str(os.listdir())+"test number 12 I think")