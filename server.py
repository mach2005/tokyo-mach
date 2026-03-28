import http.server
import os

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.dirname(os.path.abspath(__file__)), **kwargs)

    def do_GET(self):
        routes = {
            '/': '/index.html',
            '/schedule': '/schedule.html',
            '/songs': '/songs.html',
            '/gallery': '/gallery.html',
            '/faq': '/faq.html',
        }
        if self.path in routes:
            self.path = routes[self.path]
        super().do_GET()

if __name__ == '__main__':
    port = 3000
    server = http.server.HTTPServer(('localhost', port), Handler)
    print(f'Server running on http://localhost:{port}')
    server.serve_forever()
