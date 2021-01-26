import numpy as np

# def main():
#     print(matrix_tutorial())
#
# def matrix_tutorial():
#     # Create the matrix A here...
#     A= [
#         [1,4,5,8],
#         [2,1,7,3],
#         [5,4,5,9]
#         ]
#     A = np.array(A)
#     return A
#
# if __name__ == "__main__":
#     main()


#행렬의 산술 연산자
A를 normalize=>합을 1로 만드는 등등
import numpy as np


def main():
    print(matrix_tutorial())


def matrix_tutorial():
    A = np.array([[1, 4, 5, 8], [2, 1, 7, 3], [5, 4, 5, 9]])

    # 아래 코드를 작성하세요.
    A = A / np.sum(A)
    #     print(A)
    #     print(np.sum(A))
    # A.var()
    return np.var(A)
    return None


if __name__ == "__main__":
    main()