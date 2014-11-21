# coding: utf-8

class TokenEmptyException(BaseException):

    def __init__(self, message):
        super(BaseException, self).__init__()
        self.message = message

    def __repr__(self):
        return 'TokenEmptyException [ERROR]: %s' % self.message
