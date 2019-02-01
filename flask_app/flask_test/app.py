from flask import request

yoman = {'a' : 0 , 'b' : 1, 'c' : 2}

print(request.yoman['a'])
print(request.yoman.get('a'))