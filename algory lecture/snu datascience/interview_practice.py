#leetcode
# Given an array of integers, return indices of the two numbers such that they
#add up to a specific target
#assumption: each input have one solution, you may not use the same element twice

#중간고사 문제도 추가하기

def twosum(nums:list,target:int)->list[int]:
    map={}
    for i in range(len(nums)):
        map[nums[i]]=i
    for i in range(len(nums)):
        complement=target-nums[i]
        if complement in map:  # in 연산자 : 딕셔너리에서 키 기준으로 찾아짐
            return (map[complement],i)
                               # ( in이 원래 dict에 키를 유무를 확인 )


# new dict={}
# for k, v in old_dict.items():
#     newdict[v]=k