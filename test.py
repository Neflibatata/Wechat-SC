import requests

proxy={
    'http':'http://localhost:4780',
    'https':'http://localhost:4780'
}
response=requests.get("https://www.sephora.com/product/givenchy-le-rouge-holiday-edition-lipstick-P464249?skuId=2389351&icid2=products%20grid:p464249:product", proxies=proxy)

print(response.text)