#!/usr/bin/python
# coding:utf-8


import os


def iter(path):
    for root, dirs, files in os.walk(path):
        for fn in files:
            if fn.endswith(".html"):
                with open(root + '/' + fn, 'r') as f:   # 读入内容
                    content = f.read()
                content = content.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/ace/1.1.3/ace.js"></script>', '<script src="http://cdn.bootcss.com/ace/1.1.3/ace.js"></script>').replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/ace/1.1.3/mode-javascript.js"></script>', '<script src="http://cdn.bootcss.com/ace/1.1.3/mode-javascript.js"></script>')  # 替换cdn
                content = content.replace('</body>', '<script src="http://yandex.st/highlightjs/8.0/styles/default.min.css"></script><script src="http://yandex.st/highlightjs/8.0/highlight.min.js"></script><script text="javascript">$(\'pre code\').each(function(i, block) {hljs.highlightBlock(block);});</script></body>')   # 添加代码高亮

                content = content.replace('<meta name="description" content="其实，这是一件很普通的事：有了一份开源期刊，叫《开源杂志》。">','<meta name="description" content="这是一群志愿者自发组织起来推广geek文化的开源期刊，她包罗万象，深入浅出，友善亲切，纵横捭阖">') #添加关键词
                content = content.replace('<meta name="description" content="">','<meta name="description" content="这是一群志愿者自发组织起来推广geek文化的开源期刊，她包罗万象，深入浅出，友善亲切，纵横捭阖">') #添加关键词
                
                content = content.replace('<meta name="generator" content="GitBook 0.5.2">','<meta name="keywords" content="开源杂志,开源,硬件,软件,文化,arduino,processing,raspberrypi">') #添加关键词

                content = content.replace('<a href="https://github.com/obookcc" target="blank" class="author-link">About the author</a>','<a href="http://obook.cc" target="blank" class="author-link">返回首页</a>') #返回首页
                content = content.replace('<a href="https://github.com/obookcc/openbook9/issues" target="blank"class="issues-link">Questions and Issues</a>','<a href="http://doask.net" target="blank"class="issues-link">我要提问</a>') #我要提问
                intro1 = content.find('https://github.com/obookcc/openbook9/edit/master/')
                intro2 = content.find('Edit and Contribute')
                content = content[:intro1] + 'http://obook.cc/openbook8/chapter/README.html" target="blank" class="contribute-link">我要捐助' + content[intro2+19:]#我要捐助
                #content = content.replace('<a href="./" >开源杂志</a>','<a href="./" >开源杂志</a><a href="http://doask.net" target="_blank"> | 我要提问</a>') #修改标题
                content = content.replace('<a href="https://github.com/obookcc/openbook9" target="_blank" class="btn pull-left home-bookmark" aria-label="GitHub home"><i class="fa fa-bookmark-o"></i></a>', '')  #删掉书签
                content = content.replace('<a href="http://www.gitbook.io/" target="blank" class="gitbook-link">Generated using GitBook</a>', '<a href="http://obook.cc/" target="blank" class="gitbook-link">Return home</a>') #return home
                
                #删除Google Facebook twitter 等社交分享
                content = content.replace('<a href="#" target="_blank" class="btn pull-right google-plus-sharing-link sharing-link" data-sharing="google-plus" aria-label="Share on Google Plus"><i class="fa fa-google-plus"></i></a>', '')
                content = content.replace('<a href="#" target="_blank" class="btn pull-right facebook-sharing-link sharing-link" data-sharing="facebook" aria-label="Share on Facebook"><i class="fa fa-facebook"></i></a>', '')
                content = content.replace('<a href="#" target="_blank" class="btn pull-right twitter-sharing-link sharing-link" data-sharing="twitter" aria-label="Share on Twitter"><i class="fa fa-twitter"></i></a>', '')
                content = content.replace('<a href="https://github.com/obookcc/openbook9/stargazers" target="_blank" class="btn pull-right count-star hidden-xs"><i class="fa fa-star-o"></i> Star (<span>-</span>)</a>','')#删除star
                content = content.replace('<a href="https://github.com/obookcc/openbook9/watchers" target="_blank" class="btn pull-right count-watch hidden-xs"><i class="fa fa-eye"></i> Watch (<span>-</span>)</a>','') #删除watcher
                intro = content.find('content="black">')
                content = content[:intro+16] + '<script type="text/javascript"src="http://js.tongji.linezing.com/3483330/tongji.js"></script><noscript><a href="http://www.linezing.com"><img src="http://img.tongji.linezing.com/3483330/tongji.gif"/></a></noscript>' + content[intro + 17:]
                
                with open(root + '/' + fn, 'w') as f:    # 写入修改后的内容
                    f.write(content)

iter(os.getcwd())
