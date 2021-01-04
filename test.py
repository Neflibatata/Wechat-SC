import requests
from bs4 import BeautifulSoup

proxy={
    'http':'http://localhost:4780',
    'https':'http://localhost:4780'
}


def get_one_url(url, proxy):
    response=requests.get(url, proxies=proxy)
    return response.text


if __name__ == "__main__":
    url = 'https://www.sephora.com/product/le-rose-perfecto-P440027?skuId=2185577&icid2=products%20grid:p440027:product'
    html = get_one_url(url, proxy)
    soup = BeautifulSoup(html,'lxml')
    a = soup.select('#qty_2185577')
    print(a)
    

#产品图片，修改2388098即可为对应的skuid即可 https://www.sephora.com/productimages/sku/s2388098-main-zoom.jpg