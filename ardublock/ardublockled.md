#《Ardublock玩转机器人》—点亮LED（上）
##走进Ardublock的世界

没有谁不喜欢机器人的。但是面对繁琐的语法，复杂的代码，还要折腾冷冰冰的器材，最终只能望而远之。手持创客神器Arduino的我们，急需一种简单易学、功能同样强大的软件来实现我们的ideas。而Ardublock完美地满足了我们这个需求。本专题将从上篇《点亮LED》开始，带领大家认识Ardublock，走进Arduino的世界，玩转机器人。
##一、认识Arduino
在认识Ardublock之前，我们应当先了解一下Arduino。因为Ardublock是为Arduino定制的编程工具。

Arduino的美丽故事起源于意大利的一所设计学校。Massimo Banzi的学生们经常抱怨找不到便宜好用的微控制器，2005年冬天，Massimo Banzi跟朋友David Cuartielles讨论了这个问题，David Cuartielles是一个西班牙籍晶片工程师，当时在这所学校做访问学者。两人决定设计自己的电路板，并引入了Banzi的学生David Mellis为电路板设计编程语言。两天以后，David Mellis就写出了程式码。又过了三天，电路板就完工了。这块电路板被命名为Arduino。几乎任何人，即使不懂电脑编程，也能用Arduino做出很酷的东西，比如对感测器作出回应，闪烁灯光，还能控制马达。认识一下Arduino的创始人吧。

![](http://doask.qiniudn.com/openbook9-arduinoblockone11.PNG)

Arduino目前广泛地应用于欧美等国家和地区的电子设计以及互动艺术设计领域，得到了Make magazine（中文版名称为《爱上制作》）等出版物和Instructable等网站的认可和推荐。Arduino被称为“科技艺术”，作为一种新的“玩具”，甚至新的艺术载体，吸引了各个领域的人们加入到Arduino的神奇世界里来。
##二、Arduino板卡种类
Arduino先后发布了很多种型号的板卡，比如可以缝在衣服上的LiLiPad。是的，初次见到它的时候，我也惊艳了。

![](http://doask.qiniudn.com/openbook9-arduinoblockone12.png)
>Arduino先后发布了很多种型号的板卡，比如可以缝在衣服上的LiLiPad。是的，初次见到它的时候，我也惊艳了。

![](http://doask.qiniudn.com/openbook9-arduinoblockone13.PNG)
>有专门为Andriod设计的Mega，是不是想试试了？

![](http://doask.qiniudn.com/openbook9-arduinoblockone14.PNG)
>还有最基础，使用最广泛的UNO。我们将会频频接触到的。

我们整个课程系列使用DFRobot出品的Arduino Romeo V1。该控制器基于UNO板卡设计，继承了Arduino 328控制器所有的特性而且集成了电机驱动、键盘、IO扩展板、无线数据串行通讯等接口。它不仅可以兼容几乎所有Arduino系列的传感器和扩展板，而且可以直接驱动12个舵机。除此之外，它还提供了更多人性化设计，采用了3P彩色排针，能够对应传感器连接线，防止插错。其中红色对应电源，黑色对应GND，蓝色对应模拟口，绿色对应数字口。

![](http://doask.qiniudn.com/openbook9-arduinoblockone15.png)

##三、Ardublock编程环境
ArduBlock由上海新车间的创客李大维和何琪辰开发，是Arduino官方编程环境的第三方软件，必须依附于Arduino IDE软件运行。使用图形化积木搭建的方式编程，可视化和交互性强，编程门槛低，即使没有编程经验的人也可以尝试给Arduino控制器编写程序。

我们使用的ArduBlock是何琪辰为教育定制的版本。你也可以直接登录百度云盘，下载我们提供的已经集成的ArduBlock的最新版Arduino。网址：http://pan.baidu.com/s/1qWFJ0EK 。这个教育版本不仅分类清晰，而且功能更加强大。

ArduBlock教育版的使用说明：http://blog.sina.com.cn/s/blog_6611ddcf0101kfs7.html

![](http://doask.qiniudn.com/openbook9-arduinoblockone16.png)

程序中的各个模块都是从左侧的模块库里“拖进”编程界面的，然后用这些模块积木进行拼接，拼接对了，会发出一声“咔”的清脆响声。如果要删去模块，直接把不需要的模块“拖出”编程界面即可。当我们编写好一个程序，点击编程环境上方的“上载到Arduino”按钮，会发现Arduino文本式的编程环境上的“上传”图标也开始工作了，而且在Arduino文本式的编程环境里还生成了文本式的代码。程序上传成功之后，文本式的文本环境下面会提示我们上传成功。

##四、驱动安装
在使用Ardublock编程实现机器人的控制之前，需要给Arduino控制器安装驱动。以WIN7为例，简单介绍驱动安装过程。使用USB连接线连接计算机和Arduino控制器。会弹出以下窗口：

![](http://doask.qiniudn.com/openbook9-arduinoblockone17.png)

我们选择第二项“浏览计算机以查找驱动程序软件”，找到我们这款软件的驱动文件夹“drivers”,点击选择下一步。

![](http://doask.qiniudn.com/openbook9-arduinoblockone18.png)

如果计算机出现“安全提示”，选择“安装”。

![](http://doask.qiniudn.com/openbook9-arduinoblockone19.png)

最后系统提示“Windows已经成功地更新驱动程序文件”。

![](http://doask.qiniudn.com/openbook9-arduinoblockone110.png)

驱动程序安装之后，在“设备管理器”的端口中可以找到新增的端口，比如这里的COM4。

![](http://doask.qiniudn.com/openbook9-arduinoblockone111.png)

如果在连接Arduino控制器和电脑以后，没有弹出安装驱动窗口，我们可以打开“设备管理器”，手动更新驱动。如下图。右击，选择“更新驱动程序软件”，接下来的步骤同上。

![](http://doask.qiniudn.com/openbook9-arduinoblockone112.png)

值得注意的是，我们要记下之前的端口号，在下载程序之前，选择工具——端口，将这里的端口与上面相对应。

 ##五、小试牛刀
驱动安装完之后，你还要正确设置端口和板卡类型，Romeo V1是基于UNO的基础开发，所以选择UNO，如图所示：

![](http://doask.qiniudn.com/openbook9-arduinoblockone113.png)

端口就选择COM4（安装驱动时看到的端口号），接下来就可以开始体验Ardublock了。

在【引脚】里面拖出【设定针脚数字值】，将“1”改成13，点击【上传到Arduino】，稍等数秒钟，你会发现板卡上有两个小LED灯在快速闪烁。等LED停止闪烁，程序也就上传成功了。你就可以看到板卡上的有个LED灯会一直亮着。程序如下。

![](http://doask.qiniudn.com/openbook9-arduinoblockone114.png)

板卡上的13号灯如下图。

![](http://doask.qiniudn.com/openbook9-arduinoblockone115.png)

**注意：如果发现LED没有变亮，请检查端口和板卡设置是否正确。**

如果把积木块上的“HIGH”改为“低（数字）”呢？再次下载程序，看看LED灯是不是灭了？

![](http://doask.qiniudn.com/openbook9-arduinoblockone116.png)

怎么样？体会到ArduBlock的强大功能了吧？这个LED就是第一个受我们编程控制的电子元件了。既然可以控制LED，我们就可以控制继电器、蜂鸣器、舵机、电磁阀等等。编程不再是阻止我们玩机器人的最大障碍了。继续跟我们学习用ArduBlock玩转机器人吧。
