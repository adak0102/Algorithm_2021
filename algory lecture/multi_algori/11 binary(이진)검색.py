#검색 위해선 정렬이 전제되어야한다.  #아니면 순차 검색해야함
#binary 이진검색


#함수
def binarySearch(ary,data):
    start=0
    end=len(ary)-1
    while start<=end:
        mid=(start+end)//2
        if data==ary[mid]: #운좋게 바로 찾을떄
            return mid
        elif data>ary[mid]:
            #midm는 어차피 아니니까 +1부터
            start=mid+1
        else:
            end=mid-1

    return -1 # 아무데서도 못찾았다 할떄 return -1 이라 많이 씀


#
dataAry=[1,2,3,5,9,11,55,77,88,128,444,9999] #9찾고 싶을때
print(binarySearch(dataAry,9)) #9를 찾아라
print(binarySearch(dataAry,1234))


#검색을 자주 해야하면 정렬 해놓는게 좋음
#이진 검색을 여러번 할거면
#한번할거면 순차검색 하는게 나음