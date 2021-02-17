from bs4 import BeautifulSoup
from helper import removeElementsList, style, script
import os


def findPaths(dir='./origin_htmls'):
    paths = []
    for maindir, _, file_name_list in os.walk(dir):
        for filename in file_name_list:
            if filename[-5:] == '.html':
                apath = os.path.join(maindir, filename)
                paths.append(apath)
    return paths


def htmlHandler(htmlfilePath, removeElementsList, style):
    htmlfile = open(htmlfilePath, 'r', encoding='utf-8')
    htmlhandle = htmlfile.read()
    soup = BeautifulSoup(htmlhandle, 'lxml')
    for i in removeElementsList:
        try:
            soup.select_one(i).decompose()
        except:
            print(i)
    # extract tag meta, if you want to remove meta data, please uncomment the following code
    # metas = soup.select('meta')
    # _ = [s.extract() for s in metas]

    # append the style to </head>
    styleTag = soup.new_tag('style')
    styleTag['type'] = 'text/css'
    styleTag.string = style
    soup.select_one('head').append(styleTag)

    # append the js to </html>
    scriptTag = soup.new_tag('script')
    scriptTag['type'] = 'text/javascript'
    scriptTag.string = script
    soup.select_one('html').append(scriptTag)

    newHtmlPath = './new_htmls' + htmlfilePath[14:]
    with open(newHtmlPath, 'wb') as f:
        f.write(soup.encode('utf8'))
    print(newHtmlPath)


if __name__ == '__main__':
    if os.path.exists('./new_htmls'):
        pass
    else:
        os.mkdir('./new_htmls')
    paths = findPaths()
    for path in paths:
        htmlHandler(path, removeElementsList, style)
