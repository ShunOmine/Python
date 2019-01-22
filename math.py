import math

num = input('累乗を計算するね。値は？--->')
index = input('指数は？--->')
ans = math.pow(int(num), int(index))
print(str(ans))

root = input('平方根を求めるね。値は？--->')
ans = math.sqrt(int(root))
print(str(ans))

print('対数を求めるよ')
m = input('真数は？--->')
a = input('底とする値は？--->')
ans = math.log(int(m), int(a))
print(str(ans))
degree = input('角度を変換するよ。値は？--->')
ans = math.radians(int(degree))
print(str(ans))

radian = input('ラジアンを角度に変換するね。ラジアンは？--->')
ans = math.degrees(float(radian))
print(str(ans))

print('直角三角形の斜辺の長さを求めるよ。')
x = input('1辺の長さは？--->')
y = input('他の1辺の長さは？--->')
ans = math.hypot(int(x), int(y))
print(str(ans))

angle = input('sin, cos, tanを求めるね。中心角は？--->')
sin = math.sin(math.radians(int(angle)))
cos = math.cos(math.radians(int(angle)))
tan = math.tan(math.radians(int(angle)))
print('sin' + angle + '=' + str(sin))
print('cos' + angle + '=' + str(cos))
print('tan' + angle + '=' + str(tan))
