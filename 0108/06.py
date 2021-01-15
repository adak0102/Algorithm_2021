#15596

# def solve(a:list)->int:
#     return(sum(a))


#4673 #오류!!
# def d(n):
#     for a in range(n):
#         p=a+1
#         check=0
#         for b in range(p):
#             m=b+1
#             num=list(str(m))
#             if p==m+sum(map(int,num)):
#                 check=1
#         if check==0:
#             print(p)
#     return ''
# #
# d(70)



# for a in range(10000):
#     n=a+1 #34
#     check=0
#     for b in range(n):
#         m=b+1
#         num=list(str(m))
#         if n==m+sum(map(int,num)):
#             check=1
#     if check==0:
#         print(n)


#1065  #???????????#

# num=int(input())
# def hansu(a):
#     count=0
#     for a in range(1,a+1):
#         if a <=99:
#            count+=1
#         else:
#             lista=list(str(a))
#             if int(lista[0])-int(lista[1])==int(lista[1])-int(lista[2]):
#                 count+=1
#     print(count)

#hansu(num)

##short
# num = int(input())
# hansu = 0
#
# for n in range(1, num + 1):
#     if n <= 99:  # 1부터 99까지는 모두 한수
#         hansu += 1
#
#     else:
#         nums = list(map(int, str(n)))  # 숫자를 자릿수대로 분리 #****#
#         if nums[0] - nums[1] == nums[1] - nums[2]:  # 등차수열 확인
#             hansu += 1

# n=1234
# print(str(n))
#
# nums = list(map(int, str(n)))  #map 두번째 객체는 iterable이라서 iterable하게 적용됨
# print(nums)

#숫자 단위 100만일때 도전#

#num=int(input())
# def hansu(a):
#     count=0
#     for a in range(1,a+1):
#         if a <= 99:
#            count+=1
#
#         else:
#             lista=list(str(a)) #[1,2,3,4,6]
#             for i in range(1,len(lista)): #12346
#                 if int(lista[i])-int(lista[i-1])==int(lista[1])-int(lista[0]):
#                     han=1
#                 else:
#                     han=0
#                     break
#             if han==1:
#                 count+=1
#     print(count)
#
# hansu(1000)

#재귀, 브루트 포스스