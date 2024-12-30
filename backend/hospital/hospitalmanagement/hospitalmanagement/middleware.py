from django.http import JsonResponse

class CheckAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.path.startswith('/api/'):
            return self.get_response(request)
        
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Unauthorized access'}, status=401)
        
        return self.get_response(request)
