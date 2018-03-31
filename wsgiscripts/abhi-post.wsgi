def application(environ, start_response):
    """An example WSGI application that displays the
    content of a POST request"""
    
    if 'CONTENT_LENGTH' in environ and environ['CONTENT_LENGTH'] != '': 
        length = int(environ.get('CONTENT_LENGTH', '0'))
        input = "<p>Input: %s</p>" % environ['wsgi.input'].read(length).decode()
    else:
        length = 0
        input = "no input"
        
    # return a simple page with the sample form and POST input
    page = [b"<html>", input.encode(), b"</html>"]
    
    headers = [('content-type', 'text/html')]
    start_response('200 OK', headers)
    return page
