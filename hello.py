#wsgi_aplication
def wsgi_aplication(environ, start_response):
    status = "200 OK"
    headers = [("Content-Type", "text/plain")]

    query_string = environ["QUERY_STRING"]
    query_list = query_string.split("&")
    body = "\n".join(query_list)

    start_response(status, headers)

    return [ body ]