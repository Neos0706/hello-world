from rest_framework.views import exception_handler as exception_handler
from rest_framework.response import Response
def custom_exception_handler(exc, context):
    """
    自定义异常函数
    :exc 本次发生的异常对象，对象
    :context 本次发生异常时的上下文环境信息，字典
            所谓执行上下文就是python解释器在执行代码时保存在内存中的变量、函数、、类、对象、模块等一系列的信息组成的环境信息。
    """
    response = exception_handler(exc, context)
    print("hello world")
    if response is None:
        """当前发生的异常，drf没有进行处理 """
        if isinstance(exc,ZeroDivisionError):
            response = Response({"detail": "0不能作为除数"})

    return response