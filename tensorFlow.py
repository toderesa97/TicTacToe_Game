# Playing with tf
import tensorflow as tf
import numpy as np

# How do we multiply, add, subtract, divide two numbers using tf
a = tf.constant([2])
b = tf.constant([5])

c = tf.multiply(a, b)

# tf needs to initialize a session to run our code
with tf.Session() as session:
    result = session.run(c)
    print(result)


# Linear regression
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*3+2
y_data = np.vectorize(lambda y: y+np.random.normal(loc=0.0, scale=0.1))(y_data)

zip(x_data, y_data)

a = tf.Variable(1.0)
b = tf.Variable(0.2)

y = a*x_data+b

loss = tf.reduce_mean(tf.square(y-y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5) # learning rate
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

train_data = []
for step in range(200):
    evals = sess.run([train,a,b])[1:]
    if step % 10 == 0:
        print(step, evals)
        train_data.append(evals)

# Note that the predicted line is Y = 3.0017443*X + 1.9911561 very close to the real one