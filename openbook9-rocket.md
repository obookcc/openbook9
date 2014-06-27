#DFRocket

###看到网上各式各样的小模型很诱人，自己却不会画，无法3D打印出来玩？没问题！我来扫盲！

>Stuart Wang----S.W手把手教你用S.W！

[Rocket.pdf](http://www.dfrobot.com.cn/community/forum.php?mod=attachment&aid=NDE4N3w5YmQ0ODY1YXwxNDAyMDE2NDU5fDExMTh8MTg0NQ%3D%3D)

**这次教一个简单的模型 ----- Rocket！**

![1](http://doask.qiniudn.com/openbook9-rocket1.jpg)

>（本文使用Solidworks2013）

1.新建模型，选择草图”，选右视视图作为草图基准面，以草图原点作起点向上画一条构造线，标好长度为100，这是火箭身体的高。
![2](http://doask.qiniudn.com/openbook9-rocket2.jpg)

2.从原点向右，画一条长为5mm的构造线，此为火箭的底面半径，为了能够3D打印，不宜设置过大； 然后自上而下，制作样条曲线，这是火箭身体的轮廓，按需设计，但为了方便打印，下方弧度不宜倾斜过大。
![3](http://doask.qiniudn.com/openbook9-rocket3.jpg)


3.从样条曲线的末端点，斜向左绘制一条与5mm直线夹角为45°的直线，这是为了防止底面锤丝；然后从样条曲线的起始端点向下绘制一条直线，直线与100mm构造先重合，与45°斜向上的直线相交。
![4](http://doask.qiniudn.com/openbook9-rocket4.jpg)



4.点击右上角的退出草图，选择特征中的旋转凸台/基体命令，以草图1作为旋转轮廓，以草图1中的100mm长构造线为旋转中心，确认，然后得到：
![5](http://doask.qiniudn.com/openbook9-rocket5.jpg)
![6](http://doask.qiniudn.com/openbook9-rocket6.jpg)


5.选择绘制草图，以右视为基准面绘制草图，以原点为起点、火箭身体顶端为终点绘制构造线，并在离原点20mm处绘制一条水平的构造线，再由水平构造线与火箭身体轮廓线的交点为起点，到火箭底面轮廓右端点做直线，以此两点绘制一个直角三角形。
![7](http://doask.qiniudn.com/openbook9-rocket7.jpg)



6.退出草图，选择特征中的拉伸切除，勾选上方向1、方向2，均设置为10mm，得到：
!8](http://doask.qiniudn.com/openbook9-rocket8.jpg)



7.以步骤6中切割出来的平面作为草图平面绘制草图，选择草图工具中的转换实体引用功能，点击步骤6切割出的平面轮廓将其引用为草图轮廓；退出草图，以右视为基准面绘制草图，绘制一条直线，该直线与火箭底面夹角为135°，从火箭底面到直线下端点竖直距离为20mm。
![9](http://doask.qiniudn.com/openbook9-rocket9.jpg)
![10](http://doask.qiniudn.com/openbook9-rocket10.jpg)


8.退出草图，选择特征中的扫描，以草图4为轮廓，草图5为路径，扫描凸台体，得到：
![11](http://doask.qiniudn.com/openbook9-rocket11.jpg)



9.以右视为基准面，绘制草图，左键单击草图选择正视于，以步骤8中扫描结果的下端点为起点，向上绘制竖直直线，长度为40mm，以同样起点绘制水平向右长度为3mm的直线，以40mm直线上端点为起点，3mm直线右端点为终点绘制样条曲线（轮廓自定，与火箭身体要求一样），以40mm直线为中线，镜像该样条曲线，在顶部绘制圆角半径为4，再使用剪裁实体将左半部分剪掉。
![12](http://doask.qiniudn.com/openbook9-rocket12.jpg)



10.退出草图，选择特征中的旋转凸台体/基体，以草图6为轮廓，草图6中40mm直线为旋转中心，生成实体，得到：
![13](http://doask.qiniudn.com/openbook9-rocket13.jpg)



11.选择特征中的参考几何体下的基准轴，以火箭身体底面的锥面做基准轴。
![14](http://doask.qiniudn.com/openbook9-rocket14.jpg)
![15](http://doask.qiniudn.com/openbook9-rocket15.jpg)



12.选择特征中的线性阵列，以步骤6、7、8、9、10中，生成的3个实体为要阵列的特征，以步骤11中所绘制的基准轴1作为阵列轴，阵列角度为360°，实例数为3个，阵列实体得到：
![16](http://doask.qiniudn.com/openbook9-rocket16.jpg)



自此，小火箭完成了！

但小伙伴们看到我火箭身体上有字？这曲面上写字的技能，下期再说吧！



>（感谢Lutz提供的摄影支持）

![17](http://doask.qiniudn.com/openbook9-rocket17.jpg)
![18](http://doask.qiniudn.com/openbook9-rocket18.jpg)





