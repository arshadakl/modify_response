from mitmproxy import http

def response(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_url == "https://test.xyz/api/payment":
        response_data = flow.response.get_text()
        response_data = response_data.replace('"amount":0', '"amount":10')
        response_data = response_data.replace('"isAvailable":false', '"isAvailable":true')
        response_data = response_data.replace('"level":0', '"level":10')
        flow.response.set_text(response_data)


# mitmproxy -s modifier.py