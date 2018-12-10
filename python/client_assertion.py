import jwt
from datetime import datetime
from datetime import timedelta
import requests
from pathlib import Path

#info of party's API, in this example Warehouse 13
aud_id = "EU.EORI.NL000000003"
base_url = "https://w13.isharetest.net"
api = "/connect/token"

#info of requesting party, in this example Krijn B.V.
client_id = "EU.EORI.NL219048113"

req_url = base_url + api

#the x5c certificate value of Krijn B.V., necessary to create the jwt header used in client_assertion 
x5c_value = ["MIIEfzCCAmegAwIBAgIIenjHQA7HkjEwDQYJKoZIhvcNAQELBQAwSDEZMBcGA1UEAwwQaVNIQVJFVGVzdENBX1RMUzENMAsGA1UECwwEVGVzdDEPMA0GA1UECgwGaVNIQVJFMQswCQYDVQQGEwJOTDAeFw0xODExMjYxMDE3MTZaFw0yMDExMjUxMDE3MTZaMEAxEzARBgNVBAMMCktyaWpuIEIuVi4xHDAaBgNVBAUTE0VVLkVPUkkuTkwyMTkwNDgxMTMxCzAJBgNVBAYTAk5MMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1vtTf1bNurdO/VeYMF1Lm33ut1Ze8HXep1MbiJNFc0J0UtRaDHm/CWvf0RARrqkGkhiCaiz+E0qvyIEHhVpNVD9TtIJVStUX3CzNG9ZKrKC9r/Y7Dcy4KHANnT3W0LfuE3w4RXtbNDPrixfdCGqusG+veTCw1CS7Ean+xb25+tAG2EUdJeSdYV+QWOegTsmE7OoMG5FILunr6/Jt2FNLRE3IHkfbaakNYoliUMzH+/8sJw4GrkvghGcNOfvRQJfstFaN8ibL698wYhDU+xAVuxvgSIn/G9C/hW3z4/ufjKkc13cCAUe2rCpb1rvUKpAfZKnT0LQQGO2i1QTANnqr8wIDAQABo3UwczAMBgNVHRMBAf8EAjAAMB8GA1UdIwQYMBaAFBY85yDp1pTvH+Wi8bj8vurfLDeBMBMGA1UdJQQMMAoGCCsGAQUFBwMBMB0GA1UdDgQWBBRDWdWHFrD5hYhK8LCfWOhhJIEo7DAOBgNVHQ8BAf8EBAMCBaAwDQYJKoZIhvcNAQELBQADggIBAAV2FD5A4fMsB9Axqwcu8DPXyNXsF3npFuNyO7wYBWnghpLv0hC/B3lP9q84/aJcowC+QA3RPeonU1jRrR+gMWpKpOWFYSA39zoMQ8wZVHPHpwZsU8XRPuLQ+Y1S0CEu5dsjf0byL+bXKh9d4xOEiwzaJ6wZd7kLL+Zv78T3OiNDg5cAnk6kiNacs3H7wrSpnf1dSxzSjr835UkuKXxb+W8vjQroXCZQW1JjdIqyx8cYiGIEBnF56j47Qlk+1eeC4cZH+FXTCDdGpWdzuev/3+3upc5S/2TOEyrR92FqZK2ofC1yA1WzzLUELptrKB4LjMipzOlgKPOyPo9z6DIuPMUOZBGcMaEHBQ4R8EiH2bSKt/FkoTjiEe4CeC5ce8GMypfjiDSDBwIiAUJEC4PfvJQlGL5xrmEMfP+gL411tI5wU7joaAhRZNHi/slRKO9FppwVZw54Vc6V9F0RiyeGdRlNPGc7Mjt0GrnvMk0qr0KGQbq32iOp7nYugnnza0EBLjB4nbPNXzdpPqHVk38ytoAbqr0MkT3ScAbFUFS/d0rn30tSyzV45zLLcOpQfJsNZrRxKZw1v+8kT+wCIfT1TC3MEmmYKX1BKSTa1Yxhgc+0L/Lf3fXAPJsOOZFeKcmHQgSLO0XJZomrGRbnQRYQV+fRVBihjKRnj8DbfDgFKXWg"]

#reading the file ~/privkey.pem 
home = str(Path.home())
privkeyfile = home + '/privkey.pem'
with open(privkeyfile, 'r') as myfile:
    priv_key=myfile.read()
    
#function to create an encoded iSHARE Client assertion (a JWT)
def iSHARE_client_assertion(a, b, c):
    encoded_jwt = jwt.encode(
        {
      "iss": a,
      "sub": a,
      "aud": [
        b,
        c
      ],
      "jti": "378a47c4-2822-4ca5-a49a-7e5a1cc7ea59",
      "exp": datetime.utcnow() + timedelta(seconds=30),
      "iat": datetime.utcnow(),
      }, priv_key, algorithm='RS256', headers={ 'x5c': x5c_value})
    return encoded_jwt

print(iSHARE_client_assertion(client_id, aud_id, req_url))


