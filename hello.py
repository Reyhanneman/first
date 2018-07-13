def app(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    body = b'Krasavcheg'
    start_response(status, headers)
    return iter([body])
