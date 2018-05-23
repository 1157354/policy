if __name__ == '__main__':
    # def log(func):
    #     def wrapper(*args, **kw):
    #         print('call %s():' % func.__name__)
    #         return func(*args, **kw)
    #     return wrapper
    # # @log
    # def now():
    #     print('2015-3-25')
    #
    # now = log(now)
    # now()
    def log(func):
        print('call %s():' % func.__name__)
        return func()

    def now():
        print('2015-3-25')

    log(now)