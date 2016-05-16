from cgi import parse_qs

#gunicorn -b 0.0.0.0:8080 hello:app

def app(environ, start_response):

	query = parse_qs(environ['QUERY_STRING'], keep_blank_values=True)
	body = []
	for key, values in query.items():
		for item in values:
			body.append(key + "=" + item + "\r\n")
   
	status = '200 OK'
	headers = [('Content-Type', 'text/plain')]
  
	start_response(status, headers)
	return iter(body)