import cgi
from cgi import parse_qs, escape    

content_page =  """<html>
 <body>
   <h1>Content Page</h1>
   
   <p>This is the content page of the website with your name %s</p>
   <p>Go to the <a href="/">index page</a></p>

 </body>
</html>
""" 

def application(environ, start_response):
      d = parse_qs(environ['QUERY_STRING'])
      name = d.get('name',[''])[0]
      name = escape(name)
      txt = "<p> Your name as captured by the html form is: "+ name +"</p>" 
      page = [b"<html", txt.encode(), b"</html>"]
      status = '200 OK'
      headers = [('content-type', 'text/html')]
 
      start_response(status, headers)
      #return [content_page]
      return [name]             

