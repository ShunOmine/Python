import tensorflow as tf

#定数を定義 ---
a = tf.constant(10, name='10')
b = tf.constant(20, name='20')
c = tf.constant(30, name='30')

#演算を定義 ---
add_op = tf.add(a, b, name='add')
mul_op = tf.multiply(add_op, c, name='mul_op')

#セッションを開始 ---
sess = tf.Session()
res = sess.run(mul_op)
print(res)

#TensorBoard　のためにグラフを出力 ---
tf.summary.FileWriter('./logs', sess.graph)







