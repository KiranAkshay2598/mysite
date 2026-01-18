from django.shortcuts import redirect

class ParseHostMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        # If the user visits 127.0.0.1 (with or without port or https), redirect to localhost
        if '127.0.0.1' in host:
            # Replace 127.0.0.1 with localhost in the full URL
            new_url = request.build_absolute_uri().replace('127.0.0.1', 'localhost')
            return redirect(new_url)

        response = self.get_response(request)
        return response
