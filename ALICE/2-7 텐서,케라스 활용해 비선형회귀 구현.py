'''텐서플로우와 케라스를 활용하여 비선형회귀 구현하기
이번 실습에서는 텐서플로우와 케라스(Keras)를 활용하여 다층 퍼셉트론 모델을 직접 만들어 보고, 이를 활용해 비선형 데이터를 회귀 예측 해보겠습니다.

케라스는 텐서플로우 내의 딥러닝 모델 설계와 훈련을 위한 API 입니다. 케라스는 연속적으로(Sequential) 레이어(Layer)들을 쌓아가며 모델을 생성하고, 사이킷런과 같이 한 줄의 코드로 간단하게 학습 방법 설정, 학습, 평가를 진행할 수 있습니다.

텐서플로우와 케라스를 이용해 다층 퍼셉트론 모델을 만들기 위한 함수/메서드

tf.keras.models.Sequential()
: 연속적으로 층을 쌓아 만드는 Sequential 모델을 위한 함수
model.complie() : 학습 방법 설정
model.fit() : 모델 학습
model.predict() : 학습된 모델로 예측값 생성
tf.keras.layers.Dense(units, activation)
: 신경망 모델의 레이어를 구성하는데 필요한 keras 함수

units: 레이어 안의 노드 수
activation: 적용할 activation function
이 외에도 다양한 인자가 존재하는데 추가적인 인자에 대한 정보는 아래 링크를 통해 확인할 수 있습니다.
'''


import tensorflow as tf
import numpy as np
from visual import *

import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

np.random.seed(100)
tf.random.set_seed(100)


def main():
    # 비선형 데이터 생성

    x_data = np.linspace(0, 10, 100)
    y_data = 1.5 * x_data ** 2 - 12 * x_data + np.random.randn(*x_data.shape) * 2 + 0.5

    '''
    1. 다층 퍼셉트론 모델을 만듭니다.
    '''

    # 첫번쨰 레이어만 input_dim 꼭 지정해줘야함, 그뒤로는 동일하게 적용됨
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(20, input_dim=1, activation='relu'),
        tf.keras.layers.Dense(20, activation='relu'),
        tf.keras.layers.Dense(1)
    ])
    # 보통 마지막 레이어에는 activation function사용하지 않음

    '''
    2. 모델 학습 방법을 설정합니다.
    '''

    # model.compile(loss = None, optimizer = None)

    model.compile(loss='mean_squared_error', optimizer='adam')

    '''
    3. 모델을 학습시킵니다.
    '''

    # history = None
    history = model.fit(x_data, y_data, epochs=500, verbose=2)
    # epochs: 학습 몇회 반복할건지, 출력 결과물 어떻게 보여줄건지, 0은 아예 출력이 안되고 1,2넣으면 출력값에 따라 더 자세한 결과가 나옴

    '''
    4. 학습된 모델을 사용하여 예측값 생성 및 저장
    '''

    # predictions = None
    predictions = model.predict(x_data)

    Visualize(x_data, y_data, predictions)

    return history, model


if __name__ == '__main__':
    main()