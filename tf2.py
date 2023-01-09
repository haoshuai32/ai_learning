import tensorflow
import numpy as np
# x = -1,,0,1,2,3,4
# y = -3.-3.1.3.5.7
# y = 2x - 1
# from tensorflow import keras
from tensorflow.python import keras
print(tensorflow.__version__)

model = keras.Sequential([keras.layers.Dense(units=1,input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')

# 通过输入 输出 确认运算函数也就是模型
xs = np.array([-1.0,0.0,1.0,2.0,3.0,4.0],dtype=float)
ys = np.array([-3.0,-1.0,1.0,3.0,5.0,7.0],dtype=float)

# 训练500次
model.fit(xs,ys,epochs=500)

print(model.predict([10.0]))
