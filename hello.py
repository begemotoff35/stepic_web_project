def app(environ, start_responce):
	start_responce('200 OK', [('Content-Type', 'text/plain')])
	return [bytes('\r\n'.join(environ['QUERY_STRING'].split('&')), encoding="utf-8")]
