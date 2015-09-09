"""lib can be used to grape website:
urllib
urllib2
httplib
httplib2
"""
import urllib
import urllib2
import sys
import chardet




req = urllib2.Request("http://www.163.com/")##这里可以换成http://www.baidu.com,http://www.sohu.com
content = urllib2.urlopen(req).read()
typeEncode = sys.getfilesystemencoding()##系统默认编码
infoencode = chardet.detect(content).get('encoding','utf-8')##通过第3方模块来自动提取网页的编码
html = content.decode(infoencode,'ignore').encode(typeEncode)##先转换成unicode编码，然后转换系统编码输出
print html
