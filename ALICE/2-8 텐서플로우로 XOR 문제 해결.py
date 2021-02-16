'''
텐서플로우로 XOR 문제 해결하기
이전 단원 ‘퍼셉트론’에선 And_gate, OR_gate, NAND_gate를 활용해서 비선형 회귀 문제였던 XOR_gate를 구현해보았습니다.

이번 시간에는 앞선 실습에서 배운 텐서플로우와 케라스를 활용해서 다층 퍼셉트론 모델을 자유롭게 만들어보고, 이를 활용해 XOR 문제를 100% 해결해보겠습니다.

XOR gate 입출력 표

Input (x1)	Input (x2)	XOR Output(y)
0	0	0
0	1	1
1	0	1
1	1	0
'''


import numpy as np
import tensorflow as tf
from tensorflow.keras import layers
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def main():
    # XOR 문제를 위한 데이터 생성

    training_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], "float32")
    target_data = np.array([[0], [1], [1], [0]], "float32")

    '''
    1. 다층 퍼셉트론 모델을 생성합니다.
    '''

    #     model = None
    #     model.add(None)

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(32, input_dim=2, activation='relu'))
    model.add(tf.keras.layers.Dense(32, activation='relu'))
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

    '''
    2. 모델의 손실 함수, 최적화 방법, 평가 방법을 설정합니다.
    '''

    # model.compile(None)
    model.compile(loss='mse', optimizer='adam', metrics=['binary_accuracy'])

    '''
    3. 모델을 학습시킵니다. epochs를 자유롭게 설정해보세요.
    '''

    hist = model.fit(training_data, target_data, epochs=30)

    score = hist.history['binary_accuracy'][-1]

    print('최종 정확도: ', score * 100, '%')

    return hist


if __name__ == "__main__":
    main()

# 레이어의 수나 레이어안에 있는 히든 노드의 수 , 학습하는 수를 조정하면서  최종 정확도를 높임