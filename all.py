print('hello')
myLegalStrLst = ['1','2','3','4','5','6','7','8']

for ii in range(5):
    myStr = input('relay(s) -> ')
    myStrLst = myStr.split()
    allAreLegal = all( el in myLegalStrLst for el in myStrLst )
    print('allAreLegal', allAreLegal)

