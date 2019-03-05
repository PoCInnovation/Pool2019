import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Hyperparameters
LEARNING_RATE = 0.01
EPOCH = 1000

# Data loading

boston = tf.contrib.learn.datasets.load_dataset('boston')
X_train, Y_train = boston.data[:, 5], boston.target

# Graph building

a = tf.Variable(tf.random_uniform(()))
b = tf.Variable(tf.random_uniform(()))
x = tf.placeholder(tf.float32, [None])
y = tf.placeholder(tf.float32, [None])

out = a*x+b
loss = tf.losses.mean_squared_error(predictions=out, labels=y)

optimizer = tf.train.GradientDescentOptimizer(0.01)
train_op = optimizer.minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

# Training

for epoch in range(EPOCH):
    # Une étape en plus qui shuffle la data, ils ne sont pas obligé de le faire
    indices = np.arange(X_train.shape[0])
    np.random.shuffle(indices)

    epoch_loss, _ = sess.run([loss, train_op], feed_dict={x: X_train[indices], y: Y_train[indices]})
    print(epoch_loss)



