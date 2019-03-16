import tflearn
from NLP.EnglishNumberRecognition import speech_data
import  tensorflow as tf

learning_rate = 0.0001  #学习率
training_iters = 300000 #训练次数
batch_size = 64

width  = 20
height =80
classes = 10

batch = word_batch = speech_data.mfcc_batch_generator(batch_size)
X,Y = next(batch)
trainX,trainY = X,Y
testX,testY = X,Y

net = tflearn.input_data([None,width,height])
net = tflearn.lstm(net,128,dropout=0.8)
net = tflearn.fully_connected(net,classes,activation='softmax')
net = tflearn.regression(net,optimizer='adam',learning_rate=learning_rate,loss='categorical_crossentropy')

model = tflearn.DNN(net,tensorboard_verbose=0)

while 1:#training_iters
    model.fit(trainX,trainY,n_epoch=10,validation_set=(testX,testY),show_metric=True,batch_size=batch_size)
    _y=model.predict(X)
model.save("tflearn.lstm.model")