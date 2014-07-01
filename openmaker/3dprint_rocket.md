# 3D打印模型火箭建造工具箱
>[原文链接](http://www.instructables.com/id/Rockit-Model-Rocket-Construction-Kit/)  作者：vishnubob  翻译：babyw dragon

![](http://doask.qiniudn.com/openbook9-3drocket1.jpg)

![](http://doask.qiniudn.com/openbook9-3drocket2.jpg)

![](http://doask.qiniudn.com/openbook9-3drocket3.jpg)

![](http://doask.qiniudn.com/openbook9-3drocket4.jpg)

###视频

在我的成长过程中，我喜欢建造模型火箭，不过说实话，我曾经真的很糟。我时常会毫无准备得用一些我知道的工具。曾经我用热胶枪建造了一些火箭，但是火箭尾翼总是在飞行途中分离。如果把尾翼挂在上面，他们一般很难对齐，这却出现了一些有意思的飞行。我从来不怎么关心美学，我会用金色、银色和黑色在它上面喷涂一个人间炼狱。但是我觉得很好，很有趣，并且从中成长。

快进到现在，我很幸运能拥有一个家用3D打印机。我已经打印了一大堆东西，大部分都不好。我想试着去打印些更实用的东西。并且我觉得更复杂、更重要的是根据用户需要和制造工艺来制作成型。在网上有很多免费、实用和可下载的模型，但是大多数模型都是.STL文件的，这使得他们在渲染环节的操作和修改效率低下。用CAD设计很棒，但是这类系统都硕大无比而且灵活性不好。这个实验是测试使用轻量级、随处可得的工具可以做些什么。就是为了好玩，我选择了模型火箭，但我并不指望它能有多好。不过我彻底错了，这个模型制作的难以置信的出色。并且通过这个过程你可以打印精确、完整和可定制的模型火箭。

掌握一点编程技巧，你就可以使用这个设备去定制你自己的模型火箭并且打印它。取决于你的打印机和你如何打印你的火箭组件，你可以在两个小时内打印一个完整的火箭。所有你要做的就是把组件拼在一起，加上引擎，然后你可以走了。

这些火箭是实验品。保证你操作的安全并且在正确的监管之下是极其重要的。实验火箭非常危险，它们可能会伤害你和你爱的人，请一定小心。

##第一步：材料

![](http://doask.qiniudn.com/openbook9-3drocket5.jpg)

![](http://doask.qiniudn.com/openbook9-3drocket8.jpg)

![](http://doask.qiniudn.com/openbook9-3drocket6.jpg)

![](http://doask.qiniudn.com/openbook9-3drocket7.jpg)


-Python：构架是在Python里写的。我已经发表在GitHub里，欢迎大家提出请求。

-OpenSCAD：这是个免费、好用的编程语言。它能够轻松得将程序定义的模型转换成适合生产制造的3D模型。Rockit工具箱通过SCAD自动将你的火箭结构转换成.STL文件。

-3D打印：我只用过我的ultimaker2测试过它。如果你没有3D打印机，你也可以在在线打印店定制你的火箭组件。

-火箭引擎：你可以在大多数在线兴趣商店购买引擎这类东西。根据引擎的大小去设计和安装你的火箭很重要。许多火箭的规格是根据引擎的实际尺寸自动计算的。

-[发射系统](http://www.estesrockets.com/rockets/accessories/launch-systems)：发射台、点火器、电子发射控制器。你可以制定火箭的发射架尺寸并安装。

-露天场所：在一片开阔的露天场地发射你的火箭是很重要的，并且确认你和你的小伙伴们在远离发射区域的安全地方。要考虑到火箭的不可预测的情况，尤其当你想重复发射火箭。在回收火箭发射过的火箭的时候必须检查。不要发射损坏的火箭。

##第二步：软件安装

![](http://doask.qiniudn.com/openbook9-3drocket9.jpg)

根据发表在[rockit wiki](https://github.com/vishnubob/rockit/wiki/Rockit)上的安装指导进行安装。它会引导你下载python程序包并安装到你的电脑。


##第三步：建造你的组件

![](http://doask.qiniudn.com/openbook9-3drocket10.jpg)

![](http://doask.qiniudn.com/openbook9-3drocket11.jpg)

![](http://doask.qiniudn.com/openbook9-3drocket12.jpg)

建造你的第一个火箭不难。你可以从程序包一些预定义的模板开始。让我们运行atlas指令，使火箭组件适合最小尺寸的引擎。

    atlas -t mini -p -s

这个命令会为火箭的多个组件生成.STL和.PNG文件。你可以用这些.STL文件去3D打印。你可以在rockit wiki阅读更多有关建造火箭的信息。

##第四步：尾翼结构

![](http://doask.qiniudn.com/openbook9-3drocket13.jpg)

![](http://doask.qiniudn.com/openbook9-3drocket14.jpg)

![](http://doask.qiniudn.com/openbook9-3drocket15.jpg)

你可以使用JSON配置文件来修改火箭的结构。让我们来尝试改变尾翼。在你根据上一步制作小引擎火箭后，复制一份mini_engine.json文件，命名为“my_mini_engine.json”。

    $ cp mini_engine/mini_engine.json
    my_mini_engine.json

打开你喜欢的编译器，编译“my_mini_engine.json”文件，它应该像这样。转到文件的底部，看尾翼定义的那节：

    "tail": { "fin_count": 4 }

让我们在尾翼代码部分增加尾翼的数量，从4增加到8：

    "tail": { "fin_count": 8 }
一旦我们保存更改，我们可以运行带‘-p’选项的atlas为这个结构重新生成图片：
    $ atlas -i my_mini_engine.json -p
对于螺旋效应，你可以从0到4调整置文件里的“倾斜”值，使尾翼轨迹有4mm的倾斜。
    "fin": { "deflection": 4 }

##第五步：打印你的火箭组件

![](http://doask.qiniudn.com/openbook9-3drocket16.jpg)

你可以用你的打印管理软件在一个过程里打印多个火箭组件。然而，你需要在打印上多留个心眼，因为东西可能做的很糟。

##第六步：组合

![](http://doask.qiniudn.com/openbook9-3drocket17.jpg)

![](http://doask.qiniudn.com/openbook9-3drocket18.jpg)

火箭的组件通过接环连接在一起。你可以用任何一种丙烯酸胶连接，但是如果你在打印机里预留了接环尺寸，你就能感受到摩擦力作用。这些作用足够牢靠，火箭在升空后都不会分离。如果你打印备用部件，你可以在现场用备用部件再安装或修复火箭。采用松弛的摩擦作用，你可以让火箭在飞行中易于分离。这对于多引擎平台和基于前椎体回的收系统很有用。

##评论：

```
rf
好东西。不过我仍然在遵循传统的手工制作，模型火箭力学。
我敢打赌还有很多革新的方式影响回收系统，例如，除了管中管的抛射还有其他有趣的方式连接各种组件。
vishnubob
你好rf。我喜欢你的想法！如果你用Rockit（或其他的设计软件）去探索你的点子并然后分享你的成功那真是太好了。

jamttingly
非常漂亮。我之前打印了火箭，在发射时他们很受欢迎。你必须要注意的一点是（以你的视频为参考）重量和稳定性。我发现由于聚乳酸非常好使，你就可以打印大型的尾翼或者满载的整流罩来维持稳定性。那就是说，3D打印是一种制造独一无二设计的火箭和挑战极限的牛逼方式。
vishnubob
嗨jmattingly，你对极了。我之所以写这个工具箱就是想探索可编程CAD。我想把这项成果与[OpenRocket](http://openrocket.sourceforge.net/）衔接来实现软件驱动设计和仿真。如果你真的能“打印”你的火箭那真是太牛逼了。
顺便说一句，我认为用这样的工具链去教育孩子科学和工程学有很大的潜力。例如加载有效载荷传感器，学生可以清晰的比较小火箭的性能特征。
我希望有人能在这个项目里帮助我。我可以为它贡献我的点子、新设计、成熟的设计套路、查错能力、文档和经验等等。请查看GitHub页面并让我知道你的疑问。

```
