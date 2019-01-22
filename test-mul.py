import tensorflow as tf

a = tf.constant(10)
b = tf.constant(20)
c = tf.constant(30)

mul_op = (a + b)  * c

sess = tf.Session()
res = sess.run(mul_op)
print(res)