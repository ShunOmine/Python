import tensorflow as tf

a = tf.constant(100)
b = tf.constant(30)

add_op = a + b

sess = tf.Session()
res = sess.run(add_op)
print(res)