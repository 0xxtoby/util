from pprint import pprint

s='''
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
cache-control: max-age=0
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"
sec-ch-ua-mobile: ?0
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: none
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'''

# print(s.split('\n'))

c='''buvid3=4A3FD166-1058-41E9-BCAC-002D2340590F155812infoc; LIVE_BUVID=AUTO3915846286049510; rpdid=|(J|kY~|uJkJ0J'ul)~u|lk|m; CURRENT_FNVAL=80; blackside_state=1; DedeUserID=28003538; DedeUserID__ckMd5=7e548edc03d108bc; SESSDATA=4bbdb4e5%2C1621868914%2Cb68f7*b1; bili_jct=b6c2b5cc42bb066ea1f1f7e704b5b10c; balh_server_inner=__custom__; balh_is_closed=; balh_=; balh_upos_server=; balh_mode=default; balh_server_custom=https://bili-proxy.98e.org; CURRENT_QUALITY=80; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1612432260,1612432270,1614334011; PVID=1; _uuid=E1216F7F-0915-05B8-8129-24541BEC4E2E19021infoc; fingerprint=61d13506026f39c47ec32467c7a4316b; buvid_fp=4A3FD166-1058-41E9-BCAC-002D2340590F155812infoc; buvid_fp_plain=4A3FD166-1058-41E9-BCAC-002D2340590F155812infoc; sid=c0ui8ud7; bp_t_offset_28003538=516858159700821068; bp_video_offset_28003538=517823234560793941
'''

def cookies_sqlit(cookies,str):
    cookies_data=cookies.split(';')
    cook={}
    for c in cookies_data:
        if c:
            cook[c.split(str)[0]]=c.split(str)[-1]

    return cook
def headers_sqlit(headers):
    headers_data=headers.split('\n')
    hh={}

    for h in headers_data:
        # print(h)
        # print('======')
        if h:
            hh[h.split(':')[0]]=h.split(':')[-1]

    return hh




# # pprint((cookies_sqlit(c)))
# print('1')
# pprint(headers_sqlit(s))
