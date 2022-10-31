import time

'''
 Api response timing
'''
class MyMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print("one time inisitlization")

    def __call__(self,request):
        request.start_time = time.time()
        print("before view")
        response=self.get_response(request)
        total = time.time() - request.start_time
        print("its total time ",total)
        print("after view")
        return response