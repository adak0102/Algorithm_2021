# import numpy as np
#
# # array = np.arange(8)
# #
# # print(array.reshape((2,4)))
# # # print(array.resize((2,4)))
# # # print(array.reshape((4,2)))
# # # print(array.resize((4,2)))
# #
# # import numpy as np
#
# n = [1, 2, 3, 4]
# N = np.array(n)
# print(N+5)

N = list(map(int, input().split()))


# 지시사항 1번을 참고하여 코드를 작성하세요.
X = sorted(N)


# 지시사항 2번을 참고하여 코드를 작성하세요.
print(len(N))
M = X[len(N)//2]


# 아래 코드는 출력을 확인할 수 있는 코드입니다.
print(X)
print(M)