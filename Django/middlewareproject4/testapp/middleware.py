class FirstMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        print('This Line is provided by middleware-1 before preprocessiong request')
        response=self.get_response(request)
        print('This Line is provided by middleware-1 After preprocessiong request')
        return response
class SecondMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        print('This Line is provided by middleware-2 before preprocessiong request')
        response=self.get_response(request)
        print('This Line is provided by middleware-2 After preprocessiong request')
        return response