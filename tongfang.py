import requests
from io import BytesIO
from PIL import Image

host= "http://210.44.159.4"
mainurl='/xs_main.aspx'
contenturl = '/content.aspx'
cha_url = 'http://210.44.159.4/xscj.aspx?xh=201311011011&xm=%BA%FA%BA%E9%D'
headers_content={'Connection': 'keep-alive',
                    'Cache-Control': 'max-age=0',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'DNT': '1',
                    'Referer': 'http://210.44.159.4/xs_main.aspx?xh=201311011011',
                    'Accept-Encoding': 'gzip, deflate, sdch',
                    'Accept-Language': 'zh-CN,zh;q=0.8',
                    'Cookie': 'ASP.NET_SessionId=vs5whnadcp3zbh55rp4nhd45',
                    'Host':'210.44.159.4'
                }
params = {
        'xh':'201311011011',
        }
xscj_post_data = {
'ddlXN':'2013-2014',
'ddlXQ':'2',
'txtQSCJ':'0',
'txtZZCJ':'100',
'Button2':"%D4%DA%D0%A3%D1%A7%CF%B0%B3%C9%BC%A8%B2%E9%D1%AF",
'__VIEWSTATEGENERATOR':'8963BEEC',
'__VIEWSTATE':'dDw0MTg3MjExMDA7dDw7bDxpPDE+Oz47bDx0PDtsPGk8MT47aTwxNT47aTwxNz47aTwyMz47aTwyNT47aTwyNz47aTwyOT47aTwzMD47aTwzMj47aTwzND47aTwzNj47aTw0OD47aTw1Mj47PjtsPHQ8dDw7dDxpPDE3PjtAPFxlOzIwMDEtMjAwMjsyMDAyLTIwMDM7MjAwMy0yMDA0OzIwMDQtMjAwNTsyMDA1LTIwMDY7MjAwNi0yMDA3OzIwMDctMjAwODsyMDA4LTIwMDk7MjAwOS0yMDEwOzIwMTAtMjAxMTsyMDExLTIwMTI7MjAxMi0yMDEzOzIwMTMtMjAxNDsyMDE0LTIwMTU7MjAxNS0yMDE2OzIwMTYtMjAxNzs+O0A8XGU7MjAwMS0yMDAyOzIwMDItMjAwMzsyMDAzLTIwMDQ7MjAwNC0yMDA1OzIwMDUtMjAwNjsyMDA2LTIwMDc7MjAwNy0yMDA4OzIwMDgtMjAwOTsyMDA5LTIwMTA7MjAxMC0yMDExOzIwMTEtMjAxMjsyMDEyLTIwMTM7MjAxMy0yMDE0OzIwMTQtMjAxNTsyMDE1LTIwMTY7MjAxNi0yMDE3Oz4+Oz47Oz47dDxwPDtwPGw8b25jbGljazs+O2w8cHJldmlldygpXDs7Pj4+Ozs+O3Q8cDw7cDxsPG9uY2xpY2s7PjtsPHdpbmRvdy5jbG9zZSgpXDs7Pj4+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85a2m5Y+377yaMjAxMzExMDExMDExOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlp5PlkI3vvJrog6HmtKrmupA7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWtpumZou+8mueQhuWtpumZojs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85LiT5Lia77yaOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzkv6Hmga/kuI7orqHnrpfnp5HlraY7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOihjOaUv+ePre+8muS/oeiuoTEzLTE7Pj47Pjs7Pjt0PEAwPDs7Ozs7Ozs7Ozs+Ozs+O3Q8QDA8Ozs7Ozs7Ozs7Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDxTRElMSTs+Pjs+Ozs+O3Q8QDA8Ozs7Ozs7Ozs7Oz47Oz47Pj47Pj47PsQvjfu59bOE7N1IZ1sZdQ6WiCJH'
}
xscj_url="http://210.44.159.4/xscj.aspx?xh=201311011011&xm=%BA%FA%BA%E9%D4%B4&gnmkdm=N121605"
headers_xscj={
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Content-Length':'42977',
        'Content-Type':'application/x-www-form-urlencoded',
        'Cookie':'ASP.NET_SessionId=vs5whnadcp3zbh55rp4nhd45',
        'DNT':'1',
        'Host':'210.44.159.4',
        'Origin':'http://210.44.159.4',
        'Referer':'http://210.44.159.4/xscj.aspx?xh=201311011011&xm=%BA%FA%BA%E9%D4%B4&gnmkdm=N121605',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36'
}

checkcode_url='/CheckCode.aspx'
headers_checkcode={   'Connection': 'keep-alive',
                    'Cache-Control': 'max-age=0',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'DNT': '1',
                    'Accept-Encoding': 'gzip, deflate, sdch',
                    'Accept-Language': 'zh-CN,zh;q=0.8',
                    'Cookie': 'ASP.NET_SessionId=vs5whnadcp3zbh55rp4nhd45',
                    'Host':'210.44.159.4'
                }
def getImage(url, headers):
    r = requests.get(url,headers=headers)
    img = Image.open(BytesIO(r.content))
    return img
