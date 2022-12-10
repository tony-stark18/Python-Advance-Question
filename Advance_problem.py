n=int(input())

# Question-1

# for i in range(1,n+1):
#     for j in range(i):
#         print(i,end=" ")
#     print("")

# Question-2

# for i in range(n,0,-1):
#     for j in range(i):
#         print(n+1-i,end=" ")
#     print("")

#Question-3

# for i in range(1,n+1):
#     for j in range(i):
#         print(j+1,end=" ")
#     print("")

#Question-4

# for i in range(n,0,-1):
#     for j in range(i):
#         print(i,end=" ")
#     print("")

# Question-5

# for i in range(n,0,-1):
#     for j in range(i):
#         print(n,end=" ")
#     print("")

# Question-6
# for i in range(1,n+1):
#     for j in range(i):
#         print(i-j,end=" ")
#     print("")

# Queston-7
# for i in range(n,0,-1):
#     for j in range(i):
#         print(j,end=" ")
#     print(" ")

# Question-#

# temp=0
# for i in range(1,n):
#     for j in range(i):
#         print(temp+j+1,end=" ")
#         if j==i-1:
#             temp=j+1+temp
#     print(" ")

#Question-8

# temp=0
# for i in range(n):
#     for j in range(2*i+1):
#         if temp+j+1<10:
#             print(temp+j+1,end=" ")
#         else:
#             break
#         if j==2*i:
#             temp=j+1+temp
#     print(" ")

#Question-9

# t=0
# for i in range(n):
#     for j in range(t+1,t-i,-1):
#         print(j,end=" ")
#     print()
#     t=t+i+2

#Question-10

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     for j in range(i-1,0,-1):
#         print(j,end=" ")
#     print()

#Question-11

# for i in range(1,n+1):
#     for j in range(n,i-1,-1):
#         print(j,end=" ")
#     for j in range(i,n+1):
#         print(j,end=" ")
#     print()

#Question-12

# for i in range(n,0,-1):
#     for j in range(2*n,2*i-1,-2):
#         print(j,end=" ")
#     print()

#Question-13

# for i in range(n):
#     for j in range(i+1):
#         print(j*i,end=" ")
#     print()

#Question-14

# for i in range(n):
#     for j in range(i+1):
#         print(i*2+1,end=" ")
#     print()

#Question-15

# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

#Question-16

# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(2*i+1):
#         print("*",end=" ")
#     print()

#Question-17

# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(i):
#         print("*",end=" ")
#     print()

#Question-18

for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()