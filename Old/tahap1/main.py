from linreg import learn, test

learn('ex2x.dat', 'ex2y.dat', 'learn.json')
test('learn.json', 4.)