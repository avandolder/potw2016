import http.client
conn = http.client.HTTPConnection("potw.quinnftw.com")
conn.request("GET", "/problem/s3cret")
r1 = conn.getresponse()
data1 = r1.read()  # This will return entire content.
print(data1)
