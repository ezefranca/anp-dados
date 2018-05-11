import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

cookies = {
    'c8a87cde00219887c6f7e6e31546f4f4': 'cuutp5j75o3knmgbqind8ecm26',
    '__utma': '46118004.1917473761.1526045635.1526045635.1526045635.1',
    '__utmc': '46118004',
    '__utmz': '46118004.1526045635.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    '__utmt': '1',
    'ASPSESSIONIDCUARQAQA': 'BGNDENFCGCHLHDEBFMHCMFHI',
    'ASPSESSIONIDCUCQTBRD': 'KGFMDAJCIDMFPFKHDOPPFMOL',
    '__utmb': '46118004.2.10.1526045635',
    'ASPSESSIONIDSWCRRCTA': 'GDJALPDDBDEEBMAIENPDEAJA',
    'ASPSESSIONIDCUBQRATD': 'CNJCEKCCMBMLAALKJANONJKJ',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'https://www.anp.gov.br/preco/prc/Resumo_Semanal_Index.asp',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,pt;q=0.8',
}

response = requests.get('https://www.anp.gov.br/preco/prc/Resumo_Semanal_Estado.asp', headers=headers, cookies=cookies, verify=False)
print(response.text)
