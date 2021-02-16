#모델 클래스 객체 생성
tf.keras.models.Sequential()

#모델의 layer 구성
tf.keras.layers.Dense(units,activation)
units:레이어 안의 Node 수
activation : 적용할 activation 함수 설정


#레이어 생성 ver1
model = tf.keras.models.Sequntial([
    tf.keras.layers.Dense(10,input_dim=2, activation = 'sigmoid'),
    tf.keras.layers.Dense(10,activation='sigmoid'),
    tf.keras.layers.Dense(1,activation='sigmoid'),
])

#레이어 추가 add. ver2
model=tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(10, input_dim=2, activation='sigmoid'))
model.add(tf.keras.layers.Dense(10, activation='sigmoid'))

#keras 메소드
#모델 학습방식 설정위한 함수
## optimizer : 모델 학습 최적화 방법 loss : 손실함수 설정
###optimization : w,b 어떤 값을 설정하면 가장 학습률 높은지 최적화
#### loss: 얼마나 나의 metric이 잘 예측 하는지
model.compile(optimizer, loss)
#모델 학습시키기 위한 함수
## x: 학습 데이터  y: 학습데이터의 label
### 모델 피팅, 학습시킴
model.fit(x,y)

#예시
model.compile(loss='mean_squared_error', optimizer='SGD')
model.fit(dataset, epoch =100)

#평가 및 예측하기
# ** 테스트 데이터 x, 레이블 y **
#모델 평가 위한 메소드, 얼마나 accuracy, 내가 얼마나 맞췄는지
model.evaluate(x,y)
#예측 수행위한 함수, 새로운 값x에 대해 y값이 무엇인지를 예측하는 함수
model.predict(x)

#평가 예측 코드 예시
##테스트데이터 준비
dataset_test = tf.data.Dataset.from_tensor_slices((data_test, labels_test))
dataset_test = dataset.batch(32)
##모델 평가 및 예측
model.evaluate(dataset_test)
predicted_labels_test = model.predict(data_test)