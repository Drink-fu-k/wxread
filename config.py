# config.py 自定义配置,包括阅读次数、推送token的填写
import os
import re

"""
可修改区域
默认使用本地值如果不存在从环境变量中获取值
"""

# 阅读次数 默认120次/60分钟
READ_NUM = int(os.getenv('READ_NUM') or 120)
# 需要推送时可选，可选pushplus、wxpusher、telegram
PUSH_METHOD = "" or os.getenv('PUSH_METHOD')
# pushplus推送时需填
PUSHPLUS_TOKEN = "" or os.getenv("PUSHPLUS_TOKEN")
# telegram推送时需填
TELEGRAM_BOT_TOKEN = "" or os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = "" or os.getenv("TELEGRAM_CHAT_ID")
# wxpusher推送时需填
WXPUSHER_SPT = "" or os.getenv("WXPUSHER_SPT")
# read接口的bash命令，本地部署时可对应替换headers、cookies
curl_str = os.getenv('WXREAD_CURL_BASH')

# headers、cookies是一个省略模版，本地或者docker部署时对应替换
cookies = {
    pgv_pvid = 5125076764;
    RK = lCH8NpImX6;
    ptcz = d6d15ee88ed93fb9b2427fa29954326907088cc9f53b264e9be1903728d4e662;
    _ga = GA1 .2 .2140382047 .1716444266;
    sensorsdata2015jssdkcross = % 7 B % 22 distinct_id % 22 % 3 A % 22362197 % 22 % 2 C % 22 first_id % 22 % 3 A % 2218 fa40cfd9c826 - 09 b401f76e7a108 - 26001 d51 - 1327104 - 18 fa40cfd9de78 % 22 % 2 C % 22 props % 22 % 3 A % 7 B % 22 % 24 latest_traffic_source_type % 22 % 3 A % 22 % E7 % 9 B % B4 % E6 % 8E % A5 % E6 % B5 % 81 % E9 % 87 % 8 F % 22 % 7 D % 2 C % 22 identities % 22 % 3 A % 22e yIkaWRlbnRpdHlfY29va2llX2lkIjoiMThmYTQwY2ZkOWM4MjYtMDliNDAxZjc2ZTdhMTA4LTI2MDAxZDUxLTEzMjcxMDQtMThmYTQwY2ZkOWRlNzgiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIzNjIxOTcifQ % 3 D % 3 D % 22 % 2 C % 22 history_login_id % 22 % 3 A % 7 B % 22 name % 22 % 3 A % 22 % 24 identity_login_id % 22 % 2 C % 22 value % 22 % 3 A % 22362197 % 22 % 7 D % 2 C % 22 % 24 device_id % 22 % 3 A % 2218 fa40cfd9c826 - 09 b401f76e7a108 - 26001 d51 - 1327104 - 18 fa40cfd9de78 % 22 % 7 D;
    fqm_pvqid = aab5c428 - e24c - 4 d42 - 967 a - 55e2 f54eb3f8;
    _qimei_uuid42 = 1881 a0b11291006ef626e9b841eb0d3f2e43f5f093;
    _qimei_fingerprint = 9 ca7bd83b4794cdc3edb9f89418b7770;
    _qimei_q36 = ;
    _qimei_h38 = e14774baf626e9b841eb0d3f0200000ee1881a;
    qq_domain_video_guid_verify = 6 c43cdc6f6745a62;
    _clck = xfwin3 | 1 | frd | 0;
    wr_vid = 19717591;
    wr_rt = web % 40 N~AqWYSZ~dXoqqvDrYF_AL;
    wr_localvid = 83 a32190712cddd783a3ed5;
    wr_name = % E7 % 83 % AD % E8 % 8 C % B6;
    wr_avatar = https % 3 A % 2 F % 2 Fres.weread.qq.com % 2 Fwravatar % 2 FWV0007 - NuFv_iPevZH929q60FZMTb4 % 2 F0;
    wr_gender = 1;
    wr_pf = NaN;
    pac_uid = 0 _Z3aN1FR1GGfwn;
    eas_sid = puQII00mfbAvHzCrOi7LAyOrUo;
    wr_fp = 1696554709;
    wr_skey = zionImA8;
    wr_gid = 238665485
}

headers = {
    : authority:
    	weread.qq.com: method:
    	POST: path:
    	/web/book / read: scheme:
    	https
    accept:
	    application / json, text / plain, *
    /*
    accept-encoding:
    gzip, deflate, br, zstd
    accept-language:
    zh-CN,zh;q=0.9,en;q=0.8
    baggage:
    sentry-environment=production,sentry-release=dev-1738835404736,sentry-public_key=ed67ed71f7804a038e898ba54bd66e44,sentry-trace_id=c4f8ee5780b84784a7d5f0810eb4171b
    content-length:
    357
    content-type:
    application/json;charset=UTF-8
    cookie:
    pgv_pvid=5125076764; RK=lCH8NpImX6; ptcz=d6d15ee88ed93fb9b2427fa29954326907088cc9f53b264e9be1903728d4e662; _ga=GA1.2.2140382047.1716444266; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22362197%22%2C%22first_id%22%3A%2218fa40cfd9c826-09b401f76e7a108-26001d51-1327104-18fa40cfd9de78%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThmYTQwY2ZkOWM4MjYtMDliNDAxZjc2ZTdhMTA4LTI2MDAxZDUxLTEzMjcxMDQtMThmYTQwY2ZkOWRlNzgiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIzNjIxOTcifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22362197%22%7D%2C%22%24device_id%22%3A%2218fa40cfd9c826-09b401f76e7a108-26001d51-1327104-18fa40cfd9de78%22%7D; fqm_pvqid=aab5c428-e24c-4d42-967a-55e2f54eb3f8; _qimei_uuid42=1881a0b11291006ef626e9b841eb0d3f2e43f5f093; _qimei_fingerprint=9ca7bd83b4794cdc3edb9f89418b7770; _qimei_q36=; _qimei_h38=e14774baf626e9b841eb0d3f0200000ee1881a; qq_domain_video_guid_verify=6c43cdc6f6745a62; _clck=xfwin3|1|frd|0; wr_vid=19717591; wr_rt=web%40N~AqWYSZ~dXoqqvDrYF_AL; wr_localvid=83a32190712cddd783a3ed5; wr_name=%E7%83%AD%E8%8C%B6; wr_avatar=https%3A%2F%2Fres.weread.qq.com%2Fwravatar%2FWV0007-NuFv_iPevZH929q60FZMTb4%2F0; wr_gender=1; wr_pf=NaN; pac_uid=0_Z3aN1FR1GGfwn; eas_sid=puQII00mfbAvHzCrOi7LAyOrUo; wr_fp=1696554709; wr_skey=zionImA8; wr_gid=238665485
    origin:
    https://weread.qq.com
    priority:
    u=1, i
    referer:
    https://weread.qq.com/web/reader/b6032660813ab90ebg010b40kc9f326d018c9f0f895fb5e4
    sec-ch-ua:
    "Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"
    sec-ch-ua-mobile:
    ?0
    sec-ch-ua-platform:
    "Windows"
    sec-fetch-dest:
    empty
    sec-fetch-mode:
    cors
    sec-fetch-site:
    same-origin
    sentry-trace:
    c4f8ee5780b84784a7d5f0810eb4171b-a8b67be3eae1aa75
    user-agent:
    Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36
}


"""
建议保留区域|默认读三体，其它书籍自行测试时间是否增加
"""
data = {
    "appId": "wb182564874663h152492176",
    "b": "ce032b305a9bc1ce0b0dd2a",
    "c": "7cb321502467cbbc409e62d",
    "ci": 70,
    "co": 0,
    "sm": "[插图]第三部广播纪元7年，程心艾AA说",
    "pr": 74,
    "rt": 30,
    "ts": 1727660516749,
    "rn": 31,
    "sg": "991118cc229871a5442993ecb08b5d2844d7f001dbad9a9bc7b2ecf73dc8db7e",
    "ct": 1727660516,
    "ps": "b1d32a307a4c3259g016b67",
    "pc": "080327b07a4c3259g018787",
}


# def convert(curl_command):
#     """提取bash接口中的headers与cookies"""
#     # 提取 headers
#     for match in re.findall(r"-H '([^:]+): ([^']+)'", curl_command):
#         headers[match[0]] = match[1]

#     # 提取 cookies
#     cookies = {}
#     cookie_string = headers.pop('cookie', '')
#     for cookie in cookie_string.split('; '):
#         key, value = cookie.split('=', 1)
#         cookies[key] = value

#     return headers, cookies


#headers, cookies = convert(curl_str) if curl_str else (headers, cookies)
