def addOne(x):
    return x + 1

def testPositive():
    assert addOne(3) == 4

def testNegative():
    assert addOne(-1) == 0

def testZero():
    assert addOne(0) == 1