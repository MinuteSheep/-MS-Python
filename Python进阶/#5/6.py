# 在Python2中


class A(object):
    pass


class B(A):
    pass


class C(B):
    pass


class D(A, B, C):
    pass


D()
