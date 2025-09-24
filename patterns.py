

# #centered Pyramid Pattern
# n = 5
# for i in range (1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(1,2*i):
#         print("*" ,end = "" )
#     print()


#Half pyramid pattern
# n = 5
# for i in range (n):
#     for j in range(i,n-1):
#         print("",end="")
#     for j in range(i+1):
#         print("* " ,end = "" )
#     print()

# #inverted pyramid pattern
# n = 5
# for i in range (n,0,-1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(2*i-1):
#         print("*" ,end = "" )
#     print("")


#numerical half pyramid
# n = 9
# for i in range(n+1):
#     for j in range(i):
#         print(i,end='')
#     print('')

# m=[]
# n = 3
# for _ in range(n):
#         l=list(map(int,input().split()))
#         m.append(l)
# for i in range(n):
#     for j in range(n-1,-1,-1):
#         print(m[j][i],end="")
#     print()
 
#hallow
# n = 5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==n or j==1 or j==n:
#             print("*",end=" ")
#         elif 3==[i] or 3==[j]:
#             print(" ",end=" ")
#         else:
#             print("*",end=" ")
#     print()

# #right hallow pattern
# n = 5
# for i in range(n):
#     for j in range (i+1):
#         if i==j or j==0 or i==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# #
# n = 5
# for i in range (1,n+1):
#     if i==1 or i==n:
#         print("*"*i)
#     else:
#         print("*" + " "*(i-2)+"*")

# #
# n = 5
# for i in range(n):
#         for i in range(n):
#             print("$",end=" ")
#         print()

# rows = 5
# for i in range(rows):
#     print(' ' * (rows - i - 1) + '*' * (2 * i + 1))


# n = 5
# for i in range(n):
#     for j in range(n):
#         print('*' ,end=' ')
#     print()

print(ord(input()))
