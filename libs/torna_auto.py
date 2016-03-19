
import glob
# app_urls_list = glob.glob("apps/*/urls.py")
# print app_urls_list


# for urls in app_urls_list:
#     print urls
#     urls = urls.replace('/','.')[0:-3]
#     print urls
#     # m = __import__(urls)
#     m = __import__(urls, globals(), locals(), ["urls_suffix"]) 
#     print m
#     urls = getattr(m, "urls_suffix")
#     print "------urls--------"
#     print urls
from libs import log

# def deco(f):
#     def _deco(perfix, suffix):
#         url = f(perfix,suffix)
#         print "[%s], [%s], [%s]" % (perfix,suffix,url)
#         return url
#     return _deco

# @deco
def global_url(perfix, suffix):
    if suffix.startswith('/'):
        suffix = suffix[1:]
    if perfix.endswith('/'):
        perfix = perfix[:-1]
    if not suffix:
        if not perfix:
            return "/"
        return perfix

    return perfix + '/' + suffix

def auto_get_urls(upaths=["apps/*/urls.py"]):
    urls = []
    for p in upaths:
        log.debug(p)
        app_urls_list = glob.glob(p)
        # print app_urls_list
        for app_urls in app_urls_list:
            app_urls = app_urls.replace('/','.')[0:-3]
            m = __import__(app_urls, globals(), locals(), ["urls_suffix"])
            app_urls = getattr(m, "urls_suffix")
            urls_perfix = getattr(m, "urls_perfix")
            app_urls = [ (global_url(urls_perfix, handler[0]),handler[1]) for handler in app_urls ]
            urls+=app_urls
    return urls

if __name__=="__main__":
    log.set_logger(level = 'DEBUG:INFO')
    print "============auto=========="
    print auto_get_urls(upaths=["apps/*/urls.py"])
