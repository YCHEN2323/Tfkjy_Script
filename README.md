# Tfkjy_Script
刷天府科技云阅读数的脚本
#总述
##本脚本适用于网页版的“天府科技云”中的“科技苑”板块阅读数，有需求并会使用点编程软件的的小伙伴可以下载使用。
#1、总体操作流程
##1.1环境配置：你需要安装python3.5版以上的版本，安装教程请自行百度。
##1.2Selenium浏览器控制软件安装：具体链接https://www.selenium.dev/downloads/，根据自己Chrome浏览器版本选择对应selenium的版本，安装好后记得记住安装位置，后面会用到。
##上面都安装好后，一切准备就绪，开始吧
#2、总体架构
##2.1getCookie.py：负责扫码获取自己的登录cookie信息
##2.2__init__.py：主执行函数，内有很多方法，分别有不同的功能，注释很详细，具体请参照注释
##2.3/cookies:存储需要刷阅读数的账号的cookie信息，一条信息一个txt文件
#3、运行方法：
##3.1首先点入getCookie.py，运行该文件，扫码成功后，请等待两分钟后，浏览器自动关闭，main同级目录下的cookies.txt即为自身信息
##3.2获取成功后，请将该文件拷贝到/cookies文件夹下（如有多个账号需要刷，请扫码得到信息后，复制到下面，修改名称）即可
##3.3
。。。有点事，一会儿写
