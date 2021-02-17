# Geektime-Html-Purify

这个仓库是我个人在使用极客时间学习过程中，想要将专栏文章保存在自己本地，既方便阅读又能将笔记本地化存储而选择的一种方案。

实际上现在已经有不少成熟的方案可以将极客时间专栏转为pdf了。但是几乎都是利用浏览器的打印服务，本人尝试了[geektime-dl](https://github.com/mmzou/geektime-dl) 以及 [geektime_dl](https://github.com/jachinlin/geektime_dl)。但是效果都不尽人意。故在学习专栏的过程中使用Devonthink3 中的clip功能顺便将专栏文章保存为html格式。

原始格式虽然也能做到快速检索，但是在Devonthink中直接搜索，也会搜索到html源码里面的东西。所以需要移除掉原始文件里面的多余元素。如下所示：


```
#gkui-message-list

#gkui-modal-controller

#app > div._2sRsF5RP_0

## svg
body > svg


## 左侧目录
#app > div._1ysv2txS_0._2bUO5eUH_0 > div._3-b6SqNP_0

## 顶部课程详情
#app > div._1ysv2txS_0._2bUO5eUH_0 > div._1Q_izgym_0 > div.rBDXhMZ0_0

## 浮动菜单栏 右边
#app > div._1ysv2txS_0._2bUO5eUH_0 > div._1Q_izgym_0 > div._35V_pofE_0

## 左侧显示目录的那个三角形按钮
#app > div._1ysv2txS_0._2bUO5eUH_0 > div._1Q_izgym_0 > div.k7LpsVQS_0

## 音频播放
#app > div > div > div > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div > div._2SKlnZlt_0 > div._1QFlQFbV_0.EdaaidhQ_0
## 留言框,自己的
#app > div._1ysv2txS_0._2bUO5eUH_0 > div._1Q_izgym_0 > div.ibY_sXau_0 > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div > div._2Vlfl3UO_0


## 学习推荐
#app > div._1ysv2txS_0._2bUO5eUH_0 > div._1Q_izgym_0 > div.ibY_sXau_0 > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div > div._2SKlnZlt_0 > div._23_U6jTI_0

## 版权信息（本人只是为自己阅读方便，所以删掉了所有不相关内容）

#app > div._1ysv2txS_0._2bUO5eUH_0 > div._1Q_izgym_0 > div.ibY_sXau_0 > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div > div._2SKlnZlt_0 > div._2sg1Tei__0

## 水平滚轮
#app > div > div > div > div > div.simplebar-track.simplebar-horizontal

## 垂直滚轮
#app > div > div > div > div > div.simplebar-track.simplebar-vertical

## 收起评论

#app > div > div > div > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div > div._3-W_zrq4_0 > div

## 文章和精选留言之前的东西
#app > div > div > div > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div > div._2SKlnZlt_0 > div._1kh1ihh6_0._2i1ytqT9_0 > div._2w-W27j5_0
#app > div > div > div > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div > div._2SKlnZlt_0 > div._1kh1ihh6_0._2i1ytqT9_0 > div.zbKHG1ec_0
```

此外通过注入css代码，实现去除打印限制。

--- 

## 使用方法

确保安装了BeautifulSoup，然后克隆本仓库。

克隆本仓库，然后在仓库文件夹下新建两个文件夹：new_htmls 和 origin_htmls。将需要转换的html文件放入文件夹origin_htmls下。然后运行remove.py即可。转换之后的文件会保存到new_htmls。

## 结果说明

通过执行此脚本，可以移除html中大多数与内容不相关的元素。可以有相对较好的阅读体验与搜索体验。

转换过程中，我保留了所有评论，我相信看评论也是一种很好的学习方式。如果各位移除评论板块，可以自行在源文件中通过选择器选择对应的元素然后加入到 './helper.py' 中removeElementsList里面。

## 关于网页转pdf的几种方式优劣性的说明

这几天尝试了一些本地应用以及一些在线应用。

本地应用有[wkhtmltopdf](https://github.com/wkhtmltopdf/wkhtmltopdf)、[pandoc](https://pandoc.org)、Adobe Acrobat以及Safari、Chrome，Devonthink的打印功能。各有千秋吧：

1. [wkhtmltopdf](https://github.com/wkhtmltopdf/wkhtmltopdf)和Adobe Acrobat在没有数学公式的情况下效果最佳，可能是因为极客时间里面用到的是katex。但是有数学公式的话，部分公式就不能正常显示了。但是生成的pdf都是可完美复制，完美搜索，以及拥有很完美的分页且生成了书签。
2. 使用Safari、Chrome和Devonthink打印的话，Chrome的视觉效果最好，因为避免了将文字，图片和图表从中间直接拆分。但是可能是因为编码问题，或是这个本来就是类似于屏幕拼图一样导致pdf不可搜索。Safari的话是既没有避免拆分，又不能良好的搜索。Devonthink是可以较好的搜索，而没有避免拆分。（这里其实很奇怪，Devonthink的pdf引擎也是调用的也是苹果家的pdfkit，但是结果要比safari好许多。）

在线应用的话包括[html2pdf](https://html2pdf.com)以及[pdfcrowd](https://pdfcrowd.com)。

html2pdf应该就是用了[wkhtmltopdf](https://github.com/wkhtmltopdf/wkhtmltopdf)，结果几乎一摸一样。部分数学公式不能正常显示。说几乎一摸一样的原因是，我使用wkhtmltopdf是直接将html文件传入到程序里面的。所以可能会存在一些相对路径与绝对路径的小问题。但是html2pdf应该是将上传的html先存到服务器然后传入url。总体来说html2pdf略胜wkhtmltopdf一筹。

pdfcrowd如果需要自定义纸张大小的话是需要收费的，它可以自动分页，以及完美的显示katex的数学公式。不足之处就是没有生成书签，以及使用了**本地文件协议file**而不是**超文本传输协议http**。

总结：一般没有使用katex引擎数学公式的html用adobe acrobat与wkhtmltopdf都是足够的，但是用的是file文件系统。在此基础上使用了http文件系统的[html2pdf](https://html2pdf.com)的效果要比前面两者都要好一些。

如果能使用css调整好分页规则，那么使用Devonthink将会是一个最佳的选择。

## To-Do

- [ ] 打印专用的css

期待有一个大神可以解决这个问题。