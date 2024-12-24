# def one(n):
#     ones=1
#     zeros=0
#     while(n):
#         if(n&1==1):
#            ones+=1
#         else:
#             zeros+=1
#         n>>=1
#     print("Numbers of ones:",ones,"Numbers of zeros:",zeros)
# number=int(input("Enter your number:"))
# one(number)
# Acitvity 2
def setOrNot(number, n):
  # You need to define 'mask' before using it
  mask = 1  # Assuming you want to check if the bit is set or not 
  if (n & mask) == 1 or (n & mask) == 0:  # Corrected comparison and OR operator
    if number & (1 << (n - 1)):
      print("SET")
    else:
      print("NOT SET")
number = int(input("Enter the number: "))
n = int(input("Enter the bit position: "))
setOrNot(number, n)