# B={1:2, 2:4 , 4: 3, 5:-1}
#
# print(max(B.values()))
# print(len(B))


# import random
#
# #range 후 sample 개수 -> list가 됨
# numbers_b = random.sample(range(100), 12)
# print(numbers_b)
#
# #리스트 컴프리핸션으로 개수만큼 뽑음 -> list가 됨
# random_list=[random.randint(1,100) for i in range(12) ]
# print(random_list)   #random.randint(range(1000))은 틀림
#
# # Create randomer_number below: #하나 선택하기 -> int 숫자가 됨
# randomer_number=random.choice(random_list)
# print(randomer_number)




# def make_spoonerism (word1,word2):
#   word1[0],word2[0]=word2[0],word1[0]
#   return (word1+" "+word2)
#
# print(make_spoonerism("Hello", "world!"))

###TypeError: 'str' object does not support item assignment###

# def make_spoonerism(word1, word2):
#   return word2[0]+word1[1:]+" "+word1[0]+word2[1:]

# def add_exclamation(word):
#   s=''
#   if len(word)>=20:
#     return word
#   else:
#     for a in range(20):
#       if a+1 <= len(word):
#         s+word[a]
#       else:
#         s+'!'
#     return s
#
# print(add_exclamation("Codecademy"))


# def username_generator(first_name ,last_name):
#     #global username
#     username=''
#     if len(first_name) >3 and len(last_name) >4:
#         username+=first_name[:3]+last_name[:4]
#         #return username
#     else:
#         if len(last_name)<4:
#             username+=first_name[:3]+last_name
#             #return username
#
#         elif len(first_name)<3:
#             username+=first_name+last_name[:4]
#             #return username
#     return username
# def username_generator(first_name ,last_name):
#   if len(first_name) >3 and len(last_name) >4:
#     username=first_name[:3]+last_name[:4]
#
#   else:
#     if len(last_name)>4:
#       username=first_name[:3]+last_name
#
#     elif len(first_name)>3:
#       username=first_name+last_name[:4]
#   return username
# Expected the name Abe Simpson to produce the username AbeSimp,
# instead got AbeSimpson

# username_generator("Abe","Simpson")



#stack
# word = input('Input a word: ')
# world_list = list(word)
#
# result=[]
# for _ in range(len(world_list)):
#     result.append(world_list.pop())
# print(result)
# print(''.join(result))
# print(word[::-1])

#4949
# line=['.']
# print(len(line))
# print(line[0])
# print(line == ['.'])
# print(len(line) == 1)
# print(line[0] == '.')
# print(len(line) == 1 & line[0] == '.')
# print(True & True)
# print(len(line) == 1 and line[0] == '.')


# while
#
# sys.stdin
# N=sys.stdin.readlines()
# #for line in N[:-1]:
# for line in N:
#
# for line in sys.stdin.readlines():
#     line=list(line)
#
# N=input()


#1874
import sys
N=int(sys.stdin.readline().rstrip())
#list=[8,4,3,6,8,7,5,2,1]
push=[]
rows=[]
result=[]
#maxnum=[0]
maxnum=0
for a in range(8):
    num=int(sys.stdin.readline().rstrip())
    #print(num)
    #maxnum.append(num)

        # else: #없을때,
        # for b in range(max(maxnum),num)
    if num in push :
        #print(num,push,1)
        if push[-1]==num:
            rows.append(push.pop())
            result.append('-')
            #print(num,push,2)
        else:
            #print(num,push,3)
            #print('NO')
            result=['NO']
            break

        #print('wrong')
    #if not num in push:
    else:
        #print('else')
        #print(maxnum,num)
        for b in range(maxnum, num):
            #print(b,push)
            push.append(b + 1)
            result.append('+')
            #print(b,push)
        rows.append(push.pop())
        result.append('-')

    if num>maxnum:
        maxnum=num
for a in result:
    print(a)
#print(maxnum,push,rows)