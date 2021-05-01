'''
BIDUPSID=ADF7CAD017A121C2A72BED8340099FDB;
PSTM=1579682096;
BAIDUID=222C5CAFDCBE1D2ECA095FD27F87EC5C:FG=1;
MCITY=-224%3A; __yjs_duid=1_6abe4b37b562f3ae0e8945c131bbbbce1617946944941;
PANWEB=1; BDCLND=5cCjPzAjlQpCHgh6KBYzprQV6OSByuqSAREZCBApAXI%3D; BDUSS_BFESS=ENTbjJaZlhOUmlHNWtlWjZaM0ZGcHZOQk5QandhZ3RuS0xVNHRCeWNTM0lrNTlnSUFBQUFBJCQAAAAAAAAAAAEAAADiTO8~AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMgGeGDIBnhgW; STOKEN=8557ccf74865c78e8746dae05e8a580972365a08610435b00454ed2a8f10abe1; H_PS_PSSID=33763_31660_33848_33675_26350_33608_33811; BAIDUID_BFESS=222C5CAFDCBE1D2ECA095FD27F87EC5C:FG=1; delPer=0; PSINO=5; csrfToken=68HATOFynUeDvYC1isTdMxhr; PANPSC=17881261515131536622%3AKkwrx6t0uHBpImnDD%2FxwH4YFB6Yu73HpzBhPI6TlThqkQTcdOb0hNUci2O0YbEjpAcOe8FJGc2d%2BXDTvtUy0SqKK%2FFH5WUxXk2vyMkqgzoLBxARvQH%2BibHZNBoZ8i0CTW8pfgMw2m%2FoeGDMyMjs7itnzWX47O8AWdVexAcWtW9O3ajUyYmLmFn1t8VXlRfZV; Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1619450843,1619451454,1619452268,1619514855; Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0=1619514855

'''
from pprint import pprint

from util.baiduyun import BaiDuPan
bd=BaiDuPan()

print(bd.verifyCookie())

# pprint(bd.getFileList(dir='/wink'))
# print(bd.delete(path='/wink/SNN.7z'))

'''
链接: https://pan.baidu.com/s/1rFs_70laSD9blGRjILyt0A 提取码: 88d6 复制这段内容后打开百度网盘手机App，操作更方便哦 
--来自百度网盘超级会员v2的分享
'''

print(bd.saveShare(url='https://pan.baidu.com/share/init?surl=-k-FDCPH83LcRMM1g8fotw'
                   ,pwd='l900',path='/wink'))

# https://pan.baidu.com/share/transfer?shareid=651034494&from=1278979120&channel=chunlei&web=1&app_id=250528&bdstoken=78ac8ceb59aced28b59f32ca74ab08ce&logid=MTU3MjM1NjQzMzgyMTAuMjUwNzU2MTY4MTc0NzQ0MQ==&clienttype=0
# https://pan.baidu.com/share/transfer?shareid=651034494&from=2760230365&channel=chunlei&web=1&app_id=250528&bdstoken=78ac8ceb59aced28b59f32ca74ab08ce&logid=MjIyQzVDQUZEQ0JFMUQyRUNBMDk1RkQyN0Y4N0VDNUM6Rkc9MQ==&clienttype=0
# https://pan.baidu.com/share/transfer?shareid=651034494&from=1278979120web=1&app_id=250528&bdstoken=78ac8ceb59aced28b59f32ca74ab08ce&logid=MTU3MjM1NjQzMzgyMTAuMjUwNzU2MTY4MTc0NzQ0MQ==&clienttype=0