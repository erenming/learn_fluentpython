class DemoException(Exception):
    """演示异常类型"""


def demo_exc_handing():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print("*** DemoException handled. Continuing...')")
        else:
            print('-> coroutine received: {!r}'.format(x))
    raise RuntimeError('This line show never run.')