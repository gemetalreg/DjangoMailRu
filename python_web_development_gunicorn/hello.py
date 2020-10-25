def app(environ, start_response):
    query_req = environ['QUERY_STRING']
    query_list = query_req.split('&')
    query_multi_lines = '\n'.join(query_list).encode('utf-8')

    start_response('200 OK', [
        ('Content-Type', 'text/plain')
    ])
    return [query_multi_lines]
