import tensorflow as tf

a = tf.placeholder(tf.int32, [None, 2])

two = tf.constant(2)
x2_op = a * two

sess = tf.Session()

sample_list = [[1, 1], [2, 2], [3, 3], [4, 4]]
res = sess.run(x2_op, feed_dict={ a : sample_list })
print(res)