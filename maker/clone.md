#来自法国的艺术家clone，与您分享视觉效果与交互体验
>作者 alexking 翻译:katrina

关于clone的介绍：


![](http://doask.qiniudn.com/openbook9-clonePortrait.jpg)

>clone其人为来自法国的艺术家IRWIN.QUEMENER，主要从事创造性的研究与概念开发。在视觉效果和交互体验方面尤为擅长，其知识和想法很多运用到了艺术及商业项目当中。并通过将实时技术的潜力发挥到极致来释放自己的创造力，从而为知名的客户和合作伙伴提供服务。

关于vvvv的介绍：
>vvvv是针对懒惰的开发者提供的一个混合视觉／文本的一流的开发环境，他将是下一代人的视觉编程语言，拥有极其广泛的节点／代码库，并且是一个跨平台的运行环境。除了自己的视觉语言环境也主机两种文本语言hlsl和c#。当然，不管你用什么样的编程语言，vvvv只有一个风格：运行时.这样就把“关闭程序以便重新编译”这样的事情变成了早期程序开发的标志。在必要时，编译发生在幕后，不会打断你的工作流程。想要扩展你自己的vvvv是轻而易举的事情，你可以使用vvvv的sdk来。事实上，许多的vvvv的节点库都通过用户发布在addonpack和contribution上了。

>不仅如此，vvvv在二维和三维动画方面也有非常好的交互实时性，并且拥有三个不同的行业标准引擎：SVG、DirectX9、DirectX11。同时，在多屏分屏及多屏同步方面也是轻而易举就可以实现所有的功能。如果你热爱动画，五个node就足以让你的计算机屏幕动起来。这种动画效果，你完全可以通过VVVV的投影映射功能，将其mapping到任何你想要投射的媒介之上，也可以自制裸眼3D效果，投射到建筑、汽车、模具等上面。如果你还在纠结Processing的代码繁琐，D3的限制性太大，脚本语言的难以理解，不妨用VVVV来做大数据处理，或者数据可视化，必然会事半功倍。大数据用到物理世界，模拟物理运动也是一个好的创新，因为VVVV在模拟物理世界，处理物理计算方面的能力，绝对要比一般的算法效率要高很多，因为，他也算是解释性语言之一。对物理计算没有兴趣也没关系，音乐是每个人都十分喜欢的，来一首歌曲，配上跟着节拍闪动的酷炫的画面，也别有一番乐趣，有人称只为VJ，因为VVVV对FFT的封装，以及其他音频算法的处理，使得VJ信手拈来。当然，这些都不是终极的效果，计算机视觉才是VVVV的杀手锏。简单的节点组合，简单的HLSL代码，简单的C#节点封装，你想计算机做的，一切，都如你所愿。跟随你的心，你就会得到你想要的！

下面，让Alexking带您近距离感受大神的修炼过程！

Alexking：clone您好，在早些时候，我跟您约到现在做一个关于vvvv的访谈，您现在方便吗？

clone：好的，没问题。

Alexking：非常感谢。您知道，为了更好的促进VVVV在中国的发展，我们将尝试用不同的方法来培养初学者的兴趣，激发他们学习vvvv的热情。您在计算机视觉艺术和VJ领域，走得比较远，对vvvv得运用驾轻就熟。中国的vvvver都很仰慕您。所以，我们以openbook的名义和您做一个交流，希望对初学者能有所帮助。非常感谢您在百忙之中与我们做这样一个分享。

clone  ： 这是我的荣幸

AlexKing  ：谢谢。您的童年一定非常有趣。你能先给我们讲讲您儿时的故事吗？
clone : 哈哈，好的。我出生在巴黎的郊区，并在那长大，我父母都是老师。年轻时，他们给我很多旅行的机会，也给了我好的教育和爱。我的姥爷你知道也是真正的极客，可以说小时候他是给我影响最深的人，他已经制作视频及图片30年了大概。他今年81岁了，仍然用电脑创作一些东西。我认为我的父母很热衷于教育我和我妹妹，他们给了我们宽广的视野去看世界。

AlexKing: 有这样的家庭，你真的太幸运了！

clone  : 的确如此！你知道我现在30岁了，我真的意识到我有多幸运。

AlexKing  :据我所知，在用vvvv之前，你是一个建筑师，你如何走上建筑设计这条道路的？

clone  :我已经很长时间没做建筑设计了，当然不是完全不做了。我少年时，我很叛逆，学习不怎么好。我总是我梦想从事实景特效方面的工作。但是我学习不好，我没法去选择。那会我女朋友有个在建筑领域的弟弟，她总是带我去巴黎，去学校看他。我看见学生们在做模型、画画、做3D图画…。我就觉得，看起来太酷了。那是在巴黎的中心，非常棒的地方。所以我决定开始学建筑，是因为我很容易被这个学校接收。当然还有，我很享受学建筑，还能在都市。建筑给了我空间和居住城市的视觉感。一些周围事物视野的某种临界点。

AlexKing  : 我猜这对你之后的工作有着巨大的影响

clone  : 是啊，的确

AlexKing :看得出来，你的作品里面有很多结构化的元素

clone  :是的，还有外层空间。那可能与建筑学有关

AlexKing : 那么，你是因为怎样的契机而第一次接触到vvvv的？

clone  :第一次接触正好是我获得建筑学学位后。应该追溯到2009年，当时我和女朋友住在巴黎，我们都拿到了文凭，并且我们都不想待在法国，而是想去看看世界。我们是自由的。同时我也在探寻一些东西。怎么说呢。啊，我想起来了。我在一个3D聊天室在线聊天，一个小孩在用一个小软件，叫FreeContextArt，它是一个基于视觉工具的编码，但非常简单。他在聊天过程中展示了他正在做什么，这就是“视觉制作的编码”，对我来说，这是疯狂的事情。我自己也试了，但是这个软件是很受限的，所以我花了很多时间在网上找资料。我尝试了很多不同的东西，我开始加工处理，但因为我是个新手，做一个简单的互动效果就花了我很多时间。有一天晚上我发现了vvvv，我可以在两分钟之内做些声音效果。就是他！我找到了！然后 我和我的女友Sonia 来了中国。在北京，是我开始真正学习如何编程的地方。

AlexKing  :恭喜您，找到了自己喜欢的工具和平台。我学会vvvv经历了漫长而痛苦的过程，能和我们谈谈您是如何从对vvvv一无所知到得心应手的么？

clone  : 好的。当我开始学习vvvv的时候，跟你一样十分艰难， 那是一个相当艰难的过程。因为我是一个编程的新手，但是对3D软件来说我不是新手，因为我在搞建筑的时候就用3D，编程背后的逻辑是很难理解的，但不管怎样，我还是很喜欢。开始会很难，因为每个功能都容易被卡住。因为你不了解，或者因为你不真正了解它是怎样工作的，所以全靠自学。一个node接着一个node，一个patch接着一个patch。一个人在电脑前工作。

AlexKing  :一个例子接着一个例子。

clone  : 的确是！

clone  :在vvvv官方网站上的contributions对我帮助很大。

AlexKing  : 是的，那确实非常有用。当您使用vvvv工作时，你的日常时间就全部投入在做vvvv的相关学习合设计上去了么？

clone  :阿哈，现在刚开始的时候有点不同，当我开始用vvvv，基本上，当我开始启用vvvv时，每件事情都花费了很多时间。因为我是初学者，很多节点和功能我都不懂，直到今天，我不能说我什么都懂，但不会在功能上被困住，但是在方法上。现在我的工作更多是关于项目编程的方法，编程的结构会是怎样的呢？而且我在修bug时候更快了，所以我可以专注在设计上，而不是在技术问题上花很多时间，而且，这是很有趣的。当我来中国之后，我学了编程，当我学了中文

AlexKing  :哈哈，是的，你中文拼音很棒！

clone  :哈哈。编程语言背后的逻辑远比中文口语要难得多。

AlexKing  :是的

clone  :我确信学中文对我学编程的帮助很大，编程也帮助了我的中文。我认为，这是你的大脑必须要工作的方式，是真的相似。

AlexKing  :他们彼此是互补的

clone  :大概是。而且，我必须生活在中国，这给了我很大激励，真的很强大并且有动力。

AlexKing  :你需要非常好的意志力。

clone  :是的，意志力显然是很重要的。我想要生活视觉化，我真的非常想，所以我很勤奋，我想知道实时的计算机绘图是怎样工作的。我是在中国首次做的，有点疯狂， 我认为。是的，我感觉非常绚丽。

AlexKing  :你知道，在中国有很多vvvv初学者，他们没有好方法学习，一直在探索走一条便捷的道路，你有什么建议吗？

clone  :我认为最好的方式就是经常去网络论坛

clone :如果可能，组织workshop，去一些工作坊。 同时，没有什么魔法，只有进取与勤奋，如果你想要，你就能做到。这就是我最想说的。

AlexKing  : 是的，你说的太对了。我经常看你的path，非常整洁。这对于熟练使用vvvv的人，怎样管理与建立vvvv库，怎样处理在更新模块时不同的版本冲突？可以谈一下您的方法和经验么？

clone  :这就是我每天要处理的，事实上，vvvv是用来创造不同种类的事物的，不同的项目。所以，对于很多项目，有时很难使用相同的方法或者patch结构，没有什么太多关于vvvv的方法论，有时这才是真正的问题。我可以说，去做才是最重要的，且让patch尽可能的干净。还有视觉组织性，所以如果你和其他人一起合作，他就能看懂你在做什么

AlexKing  :也许，让各种功能模块集承在同一个根patch下面，每个功能模块做为一个子patch，这也是好的习惯，对吧？

clone :是的，保持每个patch和模块其间不要有太多节点，最多可有6-10个，这样就可以快速阅读了。你就不至于被导航的一团糟了

AlexKing  :是的，这对于大型工程和团队合作是非常重要的。据我所致，您非常喜欢DX11的特效，这是一个非常强大的东西，但大多数节点是纯编码封装的，它关注的更多是节点的代码结构，对于初学者，怎样才能自己着手管理一些简单的代码呢？我的意思是，关于C#以及HLSL。

clone  :是的，但主要问题是，通常是要进入DX11和shaders的

AlexKing  :怎样开始且很有乐趣呢？

clone  :去理解"Graphics Pipeline”（“图形管线”）。我确定，教不会编程的人学shader是有方法的，但是现在所有教程都是为码农编的， 而不是艺术家，所以这真的很难理解。shaders和DX11可以做很多事情，并不是那么复杂，但和其他一样，都需要时间和并有动力去学习理解。我学习怎样编译shader（我必须说是简单的shader），通过看书。我花了很大一部分时间看书来学习shader编程，直到我足够理解到自己可以尝试了，我认为Patch编程开始的时候要简单一些。但是，shader是有不同逻辑和编码的，大多数都很短。

AlexKing  :是的，事实上，并不很难

clone  :所以，现在对于我，挑战是找到一个不同的方式来教初学者。

AlexKing  :Patch一般都是使用C#编程封装的，但是DX11的shader使用HLSL来封装的。

clone  :是的，HLSL是一种C语言，有几个函数需要知道，有时三行代码就能做很多事情。有时三行内很难知道是做了什么

AlexKing :我就曾经遇到过类似的问题。您能提供一些关于vvvv的效果图么，让读者知道vvvv都能干什么。比如2D/3D动画，多屏幕设置，运动图形，投影映射，数据可视化，物理计算，音频，计算机视觉等

clone  :好的，棒极了。

AlexKing  : 谢谢您。非常不好意思，耽误您太多时间了，在这次分享结束之前您还有什么想说吗？

clone  : 我想感谢大家，我想感谢我的家庭，我前女友Sonia，vvvv的QQ群聊天室，而且特别感谢北京的VJ Ink，还有上海戏剧学院的张敬平，还要感谢所有支持我及我工作的人，还有给所有vvvv的中国具有开创性的程序员，及其他人，他们都值得尊重，还有感谢你及openbook给我这次分享机会

AlexKing  :我们一定替您转达您的谢意。

clone ：谢谢。

AlexKing ：不客气。下次有机会我们将继续邀请您做进一步的分享。

##附作品：
作品一：

Title : Orchids

Year : 2014

Tools : freestyle live patching with vvvv
![](http://doask.qiniudn.com/openbook9-clone1.jpg)

￼
作品二：

Title : Geometry Shader Experiment

Year : 2014

Tools : vvvv and HLSL (shader language)

![](http://doask.qiniudn.com/openbook9-clone2.jpg)

作品三：

Title : Clone feat Kyle Lyons (vjloops.com)

Year : 2013

Tools : C-MiX

![](http://doask.qiniudn.com/openbook9-clone3.jpg)

作品四：

Title : Clone feat Kyle Lyons (vjloops.com)

Year : 2013

Tools : C-MiX

![](http://doask.qiniudn.com/openbook9-clone4.jpg)

作品五：

Title : Clone feat Kyle Lyons (vjloops.com)

Year : 2013

Tools : C-MiX

![](http://doask.qiniudn.com/openbook9-clone5.jpg)

作品六：

Title : Clone feat Kyle Lyons (vjloops.com)

Year : 2013

Tools : C-MiX

![](http://doask.qiniudn.com/openbook9-clone6.jpg)

作品七：

Title : Clone feat Kyle Lyons (vjloops.com)

Year : 2013

Tools : C-MiX

![](http://doask.qiniudn.com/openbook9-clone7.jpg)

作品八：

Title : Geometry Shader Experiment

Year : 2014

Tools : vvvv and HLSL (shader language)

![](http://doask.qiniudn.com/openbook9-clone8.jpg)

作品九：

Title : Geometry Shader Experiment

Year : 2014

Tools : vvvv and HLSL (shader language)

![](http://doask.qiniudn.com/openbook9-clone9.jpg)

作品十：

Title : Geometry Shader Experiment

Year : 2014

Tools : vvvv and HLSL (shader language)

![](http://doask.qiniudn.com/openbook9-clone10.jpg)

作品十一：

Title : Geometry Shader Experiment

Year : 2014

Tools : vvvv and HLSL (shader language)

![](http://doask.qiniudn.com/openbook9-clone11.jpg)

作品十二：

Title : Orchids

Year : 2014

Tools : freestyle live patching with vvvv

![](http://doask.qiniudn.com/openbook9-clone12.jpg)
