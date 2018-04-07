import matplotlib.pyplot as plt
import tensorflow as tf
from numpy import genfromtxt
fish_data = genfromtxt('data\data.csv', delimiter=',')

# long fish = 1, small fish = 0
for list in fish_data:
    if list[3] >= 2000:
        list[3] = 1
    else:
        list[3] = 0

print(fish_data)

plt.scatter(fish_data[:,1],fish_data[:,2],)
plt.xlabel('Age of Fish')
plt.ylabel('Water Temperature')
plt.legend(loc='best')
#plt.show()

# Parameters
learning_rate = 0.01
training_epochs = 25
display_step = 1
n_samples = 44

# tf Graph Input
x = tf.placeholder(tf.float32, name="x") # data image of shape 44*2=88
y = tf.placeholder(tf.float32, name="y") # 0-9 digits recognition => 10 classes

# Set model weights
W = tf.Variable(tf.zeros([88, 2]))
b = tf.Variable(tf.zeros([2]))

# Construct model
pred = tf.nn.softmax(tf.matmul(x, W) + b)

# Minimize error using cross entropy
cost = tf.reduce_mean(-tf.reduce_sum(y*tf.log(pred), reduction_indices=1))
# Gradient Descent
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# Initialize the variables (i.e. assign their default value)
init = tf.global_variables_initializer()

# Start training
with tf.Session() as sess:

    # Run the initializer
    sess.run(init)

    # Training cycle
    writer = tf.summary.FileWriter('./graphs/linear_reg', sess.graph)

    # Step 8: train the model
    for i in range(25):  # train the model for 25 epochs
        total_loss = 0
        for i,x1,x2, y1 in fish_data:
            # Session runs train_op and fetch values of loss
            _, c = sess.run([optimizer, cost], feed_dict={x:[x1,x2], y: y1})
            total_loss += c
        print('Epoch {0}: {1}'.format(i, total_loss / n_samples))

    # close the writer when you're done using it
    writer.close()

    W,b = sess.run([W,b])