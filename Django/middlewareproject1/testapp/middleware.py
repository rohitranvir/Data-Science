class middlewareexecution(object):
    def __init__(self,get_response):
        print('This line is by get_response function')
        self.get_response=get_response
    def __call__(self,requests):
        print('Preprocession of request')
        response=self.get_response(requests)
        print("Post preprossesion of request")
        return response