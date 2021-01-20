#퀵정렬은 기준을 선정 / 보통 중간거 : 작은거는 다 왼쪽 으로 큰거는 다 오른쪽으로 가져감
#왼쪽-기준-오른쪽 순
#또다시 왼쪽그룹에서 (4개중 ㅎ가운데 하나 기준 잡음)
#하나 남았을떄까지: 정렬할게 없음
#퀵정렬 재귀로 사용 : 나기준 작은거 왼쪽 큰거 오른쪽 (같은것) 한개 남을떄까지 --> 재귀 호출
#nlogn으로 데이터가 많아도 정렬가능 : 성능 무지 좋음
#------


import random
##함수 선언부
def quickSort(ary):
    n=len(ary)
    if n<=1:
        return ary
    pivot=ary[len(ary)//2] #기준값을 중간 #상관없지만 중간
    leftAry,rightAry=[],[] #왼,좌 두개 준비
    for num in ary:
        if num < pivot:
            leftAry.append(num)
        elif num>pivot:
            rightAry.append(num) #같은것 일단없다고 가정
    return quickSort(leftAry)+[pivot]+quickSort(rightAry)
#전역 변수부
ary=[random.randint(100,999) for _ in range(20) ]
#메인코드부
print('정렬전-->',ary)

ary=quickSort(ary)
print('정렬후-->',ary)