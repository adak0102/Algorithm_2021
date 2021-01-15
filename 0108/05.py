# import sys
# N=int(input())
#
# num=list(0 for _ in range (N))
#
# for k,i in enumerate(sys.stdin):
#     num[k] = i
#
# print(min(num),max(num))

#10818
#(1)
# import sys
# N=int(input())
#
# num=list(0 for _ in range (N))
#
# for k,i in enumerate(map(int,input().split())):
#     num[k] = i
#
# print(min(num),max(num))

#(2) (error)
# N=int(input())
#
# num=list(0 for _ in range (N))
#
# for k in range(N):
#     num[k] = map(int,input().split())[k]  #오류!! map객체 자체는 list가 아니라서!!!
#
# print(min(num),max(num))

#(3)
# N=int(input())
# num=list(map(int,input().split()))
# print(min(num),max(num))
#
# #short
# import sys
# n, *m = map(int, sys.stdin.read().split())  # *m-> 몇개인지 모를떄!!!!!!!!!!
# print(min(m), max(m))

#2562  #????????????#
# import sys
# n=list(map(int,sys.stdin.read().split()))
# print(max(n))
# print(min(n))

# number=list(0 for i in range(9))
# maxnum=0
# maxcount=0
# for i in range(9):
#     number[i]=int(input())
#     if number[i]>maxnum:
#         maxnum=number[i]
#         maxcount=i+1
#
# print(max(number))
# print(maxcount)
#
# ##short
# l=[int(input())for i in range(9)]
# print(max(l),l.index(max(l))+1)
#
# ###short #???
# l=[0];exec("l.append(int(input()));"*9);m=max(l);print(m,l.index(m))
#
# #####short
# m=0;k=0
# for i in range(9):
#     n=int(input())
#     if m<n:m=n;k=i+1
# print(m);print(k)
# ######short
# p=[]
# [p.append(int(input()))for i in range(9)]
# print(max(p))
# print(p.index(max(p))+1)
#
# p=[]
# [p.append(int(input()))for i in range(9)]
# print(max(p))
# print(p.index(max(p))+1)

#2577
num=int(input())
num*=int(input())
num*=int(input())

for

##3052

#1546 평균
# N=int(input())
# score=list(map(int,input().split()))
# maxscore=max(score)
# print(sum((score[i]/maxscore) for i in range(N))*100/N)
# #
# # for i in range(N):
# #     score[i]=score[]
#
# #short
# import sys
# num_record = int(sys.stdin.readline().rstrip())
# list_record = list(map(int, sys.stdin.readline().rstrip().split()))
# print(sum(list_record)/max(list_record)*100/num_record)

#8958 OX
# N=int(input())
#
#
# for i in range(N):
#     total = 0
#     sum = 0
#     count = 0
#     score=list(input())
#     for i in score:
#        if i == 'O':
#            count+=1
#            sum+=count
#            #print(count)
#            #print(sum)
#        else:
#            #sum = 0
#            count = 0
#        #total+=sum
#        #print(total)
#     print(sum)

####Short 안봄####


#4344평균은  #########틀림!!###########
# N=int(input())
# for i in range(N):
#     score=list(map(int,input().split()))
#     total=sum(score)
#     average=((total-score[0])/score[0])
#     count=0
#     for k in score:
#         if k > average:
#             count+=1
#     print('%.3f%%'%round(((count/score[0])*100),3))
#
# #short
# n = int(input())
#
# for _ in range(n):
#     nums = list(map(int, input().split()))
#     avg = sum(nums[1:])/nums[0]  # 평균을 구함 (nums[0]: 학생수, nums[1:] 점수)
#     cnt = 0
#     for score in nums[1:]:
#         if score > avg:
#             cnt += 1  # 평균 이상인 학생 수
#     rate = cnt/nums[0] *100
#     print(f'{rate:.3f}%')

