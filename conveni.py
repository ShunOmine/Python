import math
print('1.累乗',
      '2.平方根',
      '3.対数',
      '4.角度をラジアンに変換',
      '5.ラジアンを角度に変換',
      '6.三平方の定理',
      '7.三角関数')
problem = input('問題はナニ？上から選んでね！>')


if (problem == '1'):
    num = input('累乗を計算するネ。値は？--->')
    index = input('指数は？--->')
    ans = int(math.pow(int(num), int(index)))
    print(str(ans))

elif(problem == '2'):
    root = input('平方根を求めるネ。値は？--->')
    ans = math.sqrt(int(root))
    print(str(ans))

elif(problem == '3'):
    print('対数を求めるネ！')
    m = input('真数は？--->')
    p = input('底とする値は？--->')
    ans = math.log(int(m), int(p))
    print(str(ans))

elif(problem == '4'):
    degree = input('角度をラジアンに変換するネ。角度は何度？--->')
    ans = math.radians(int(degree))
    print(str(ans))

elif(problem == '5'):
    radian = input('ラジアンを角度に変換するね。ラジアンは？--->')
    ans = math.degrees(float(radian))
    print(str(ans))

elif(problem == '6'):
    print('直角三角形の斜辺の長さを求めるヨ。')
    x = input('1辺の長さは？--->')
    y = input('他の1辺の長さは？--->')
    ans = math.hypot(int(x), int(y))
    print(str(ans))

elif(problem == '7'):
    angle = input('sin, cos, tanを求めるネ。角度θは？--->')
    sin = math.sin(math.radians(int(angle)))
    cos = math.cos(math.radians(int(angle)))
    tan = math.tan(math.radians(int(angle)))
    print('sin' + angle + '=' + str(sin))
    print('cos' + angle + '=' + str(cos))
    print('tan' + angle + '=' + str(tan))

else:
    print('?')
