while True:
    a,b = map(int, input().split())
    if a==0: break
    else: print(['No','Yes'][a>b])