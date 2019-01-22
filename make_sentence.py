#第１文型
print('第１文型の例文を作るね')
subject = input('主語（s）は？>')
verb = input('動詞（v）は？>')
print('{s} {v}.'.format(s=subject, v=verb))

#第２文型
print('第２文型の例文を作るね')
subject = input('主語（s）は？>')
verb = input('動詞（v）は？>')
comp = input('補語（c）は？>')
print('{s} {v} {c}.'.format(s=subject, v=verb, c=comp))

#第３文型
print('第３文型の例文を作るね')
subject = input('主語（s）は？>')
verb = input('動詞（v）は？>')
obj = input('目的語（o）は？>')
print('{s} {v} {o}.'.format(s=subject, v=verb, o=obj))

#第４文型
print('第４文型の例文を作るね')
subject = input('主語（s）は？>')
verb = input('動詞（v）は？>')
i_obj = input('間接目的語（IO）は？>')
d_obj = input('直接目的語（DO）は？>')
print('{s} {v} {io} {do}.'.format(s=subject, v=verb, io=i_obj, do=d_obj))

#第５文型
print('第５文型の例文を作るね')
subject = input('主語（s）は？>')
verb = input('動詞（v）は？>')
obj = input('目的語（o）は？>')
comp = input('補語（c）は？>')
print('{s} {v} {o} {c}.'.format(s=subject, v=verb, o=obj, c=comp))
