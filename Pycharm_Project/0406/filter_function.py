#filter 函数
movie_people=['djf','ldd','djh','sbll','llsbsb']

def showsb(n):
    return n.endswith('sb')


def filter_test(func,array):
    ret=[]
    for p in array:
        if not showsb(p):
            ret.append(p)
    return ret

print(filter_test(showsb,movie_people))

# res = filter_test(lambda p:p.endswith('sb'),movie_people)

res = filter(lambda n:not n.startswith('sb'),movie_people)

print(list(res))