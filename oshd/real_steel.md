# 铁甲钢拳3
###——臂带式体感交互控制器
![](http://doask.qiniudn.com/openbook9-realsteel1.png)

在用手柄玩了一段时间格斗机器人之后，制作过程参见前两期的《无线电》杂志，这次本人在控制器方面又进行了一次升级。不再使用类似游戏机的手柄，而是自制了一个臂带式体感交互控制器。

大家一定觉得这个名字太抽象了，具体的说就是用加速度传感器来获取手臂的姿态，然后通过无线的方式来控制机器人或者其他的东东。

我用到的器材如下，参见图1：

序号	器材	数量
1	Arduino UNO 或DFduino UNO	1
2	Xbee传感器扩展板 V5	1
3	电池盒	1
4	电池	5（与电池盒匹配）
5	numchuck连接器及连接线	1
6	MMA7361加速度传感器	1
7	护膝	1
8	Wii 副手柄numchuck	1
9	DFduino wireless无线模块	1

| 序号 | 器材 | 数量 |
| -- | -- | -- |
| 1 | Arduino UNO 或DFduino UNO | 1|
| 2 | Xbee传感器扩展板 V5 | 1 |
| 3 | 电池盒 | 1 |
| 4 | 电池 | 5（与电池盒匹配） |
| 5 | numchuck连接器及连接线 | 1 |
| 6 | MMA7361加速度传感器 | 1 |
| 7 | 护膝 | 1 |
| 8 | Wii 副手柄numchuck | 1 |
| 9 | DFduino wireless无线模块 | 1 |

![](http://doask.qiniudn.com/openbook9-realsteel2.png)
>图一所用器材

先来说说硬件的连接，首先将护膝带在左手手腕上，为什么选择一个护膝而不是直接用一个护腕呢，这是因为护膝内和手臂的空间比较大，制作起来比较方便。而如果是用护腕则是完全勒在手腕上的。

将护膝带到虎口位置即可，并将虎口的位置缝合起来，使其更像一个手套。同时把Arduino控制板和加速度传感器缝在护膝上，如图2所示，加速度传感器的连接线从护膝内穿过。

![](http://doask.qiniudn.com/openbook9-realsteel3.png)
>图2 控制板和加速度传感器的固定

第2步，将Xbee传感器扩展板V5插在Arduino控制板上，同时将加速度传感器的连接线连接到A0、A1和A2上，分别对应X、Y、Z三个轴向，并且把Numchuck连接器用连接线连到传感器扩展板上，连接是要注意引脚的定义，连接器的d端对应A4，c端对应A5。如图3所示。

![](http://doask.qiniudn.com/openbook9-realsteel4.png)
>图3 传感器扩展板的连接

第3步，将电池盒连接在传感器扩展板的电源输入端，并把其固定在护膝内，手臂内侧。如图4所示。

![](http://doask.qiniudn.com/openbook9-realsteel5.png)
>图4 电池盒的固定

第4步，将之前遥控器内的DFduino wireless无线模块拆下并安装在传感器扩展板上。如图5所示。

![](http://doask.qiniudn.com/openbook9-realsteel6.png)
>图5 安装无线模块

最后将Wii的副手柄numchuck接上，并将其握在右手内。如图6所示，这样，我们的臂带式体感交互控制器硬件部分就算完成了。

![](http://doask.qiniudn.com/openbook9-realsteel7.png)
>图6 连接numchuck

接下来说说软件部分。这个遥控器的控制思路是这样的，当我水平伸出手臂时，机器人作出摆臂的动作，如图7所示；当我向前挥动手臂时，机器人做出打拳的动作，如图8所示。

![](http://doask.qiniudn.com/openbook9-realsteel8.png)
>图7 水平伸出手臂

![](http://doask.qiniudn.com/openbook9-realsteel9.png)
>图8 向前挥动手臂

而机器人的移动依靠numchuck手柄上的摇杆，同时配合手柄上的Z键和C键完成机器人的移动。控制动作和机器人的动作对应关系如下表。


| 序号 | 动作说明 | 触发指令 | 控制动作 |
| -- | -- | -- | -- |
| 1 | 机器人前进一步 | 1 | 摇杆向前 |
| 2 | 机器人后退一步 | 2 | 摇杆向后 |
| 3 | 机器人左转 | 15 | 摇杆向左 |
| 4 | 机器人右转 | 14 | 摇杆向右 |
| 5 | 机器人向左滑动一步 | 8 |按下Z键同时摇杆向左 |
| 6 | 机器人向右滑动一步 | 7 | 按下Z键同时摇杆向右 |
| 7 | 机器人下蹲 | 12 | 按下Z键同时摇杆向后 |
| 8 | 机器人起身 | 13 | 按下Z键同时摇杆向前 |
| 9 | 左拳 | 6 | 左手向前伸 |
| 10 | 右拳 | 5 | 右手向前伸 |
| 11 | 左臂摆动 | 4 | 左手水平抬起 |
| 12 | 右臂摆动 | 3 | 右手水平抬起 |
| 13 | 向前倒下后起身 | 9 | 按下C键同时摇杆向前 |
| 14 | 向后倒下后起身 | 16 | 按下C键同时摇杆向后|

Wii的副手柄numchuck的使用《无线电》杂志的2010年第12期和2012年第6期都有介绍过，这里就简单的说明一下。Arduino使用这个副手柄需要单独下载一个WiiChuck库文件，有了这个库文件，在代码中直接调用wii.getAccelAxisX()、wii.getAccelAxisY()之类的函数就可以直接获得摇杆的值、手柄内加速的的值以及按钮的值。这里我还要对C键和Z键作一个说明，我手上的这个numchuck手柄，当Z键和C键都没有按下时，两者返回的都是1；当按下C键时，C键返回值为0，Z键返回值为1；但当按下Z键时，两者返回的值都是0；当C键和Z键都按下时，Z键的返回值为0，C键的返回值为1。

这里着重的说一下MMA7361加速度传感器的使用，如图9所示。加速度传感器是一种能够测量加速力的电子传感器。通过测量由于重力引起的加速度，可以计算出设备相对于水平面的倾斜角度，分析出设备移动的方式。

![](http://doask.qiniudn.com/openbook9-realsteel10.png)
>图9 MMA7361加速度传感器

MMA7361加速度传感器基于Freescale（飞思卡尔）公司生产的微型电容式三轴加速度传感器MMA7361芯片。该芯片采用信号调理、单极低通滤波器和温度补偿技术，提供±1.5g／6g两个量程，用户可在这2个灵敏度中选择，该器件还带有低通滤波并已做0g补偿。

传感器有3个模拟量的三芯接口，分别表示X、Y、Z三个轴的加速度值，同时预留排针焊接孔。前面已经说过，我们分别将X、Y、Z三个轴向的加速度值输出引脚连接到A0、A1和A2。

![](http://doask.qiniudn.com/openbook9-realsteel11.png)
>图10 静态加速度传感器输出值

我们使用的是1.5g的量程，上图中给出了静态加速度传感器几种状态下的各个轴向加速度的值，由于量程是从-1.5g到+1.5g，所以当加速度为0g时，引脚输出的电压大致为1.65V，再因为有重力的关系，所以方向向下的轴向上加速度值是1g（根据方向的不同可能是+1g或-1g）。我们可以通过如下的代码将传感器输出的模拟量值转换为电压值（以X轴为例）。

    vol_x=analogRead(A0)*5.0/1024;

然后根据1.5g量程下的灵敏度——800mV/g，通过电压值换算出轴向上当前的加速度值，代码如下。

    g_x =（vol_x-1.76)/0.8

但在实际的应用中，由于传感器的差异，当在0g是输出的电压值可能不是1.65V，所以在使用加速度传感器之前需要对其进行校准，以当前0g时输出的电压值作准。

但在这里不用这么麻烦，只需要通过判断返回的模拟量值是否在一个区间内就能够推断出传感器当前大致的姿态，进而发送命令控制机器人。

详细代码如下。
```
#include <math.h>
#include <stdlib.h>
#include "Wire.h"
#include "WiiChuck.h"

WiiChuck wii = WiiChuck();

int sensorAccelX,sensorAccelY,sensorAccelZ;
int sensorAccelWiiX,sensorAccelWiiY,sensorAccelWiiZ;
int sensorJoyX,sensorJoyY;
int buttonC,buttonZ;


void setup()
{
 wii.init(); 				//初始化Wii手柄
 Serial.begin(57600);
}

void loop()
{
      //获取加速度传感器的模拟量值
  sensorAccelX = analogRead(A0);
  sensorAccelY = analogRead(A1);
  sensorAccelZ = analogRead(A2);

  //获取Wii手柄的各个参数
  if (true == wii.read())
  {
    sensorAccelWiiX = wii.getAccelAxisX();
    sensorAccelWiiY = wii.getAccelAxisY();
    sensorAccelWiiZ = wii.getAccelAxisZ();

    sensorJoyX = wii.getJoyAxisX();
    sensorJoyY = wii.getJoyAxisY();

    buttonZ = wii.getButtonZ();
    buttonC = wii.getButtonC();
  }


  //通过各个参数值推断当前两手的姿态，进而控制机器人

  //在未按下Z和C键时通过摇杆控制机器人移动
  if((buttonZ == 1) && (buttonC == 1))
  {
    if(sensorJoyY > 200)
    {
      Serial.write(1);//向机器人发送1，机器人将做出前进的动作
    }
    else if((sensorJoyY < 76) && (sensorJoyY > 40))
    {
      Serial.write(2); //向机器人发送2，机器人将做出后退的动作
    }

    if((sensorJoyX < 76) && (sensorJoyX > 40))
    {
      Serial.write(15); //向机器人发送15，机器人将做出左转的动作
    }
    else if(sensorJoyX > 200)
    {
      Serial.write(14); //向机器人发送14，机器人将做出右转的动作
    }
  }

  //按下Z键时控制机器人的左右平移和蹲下起身
  if(buttonZ == 0)
  {
    if(sensorJoyY > 200)
    {
      Serial.write(13); //向机器人发送13，机器人将做出起身的动作
    }
    else if((sensorJoyY < 76) && (sensorJoyY > 40))
    {
      Serial.write(12); //向机器人发送12，机器人将做出蹲下的动作
    }

    if((sensorJoyX < 76) && (sensorJoyX > 40))
    {
      Serial.write(8); //向机器人发送8，机器人将做出左移的动作
    }
    else if(sensorJoyX > 200)
    {
      Serial.write(7); //向机器人发送7，机器人将做出右移的动作
    }
  }


  //按下C键时控制机器人在跌倒的情况下爬起来
  if((buttonZ == 1) && (buttonC == 0))
  {
    if(sensorJoyY > 200)
    {
      Serial.write(9); //向机器人发送9，机器人将从前爬起
    }
    else if((sensorJoyY < 76) && (sensorJoyY > 40))
    {
      Serial.write(16); //向机器人发送16，机器人将从后爬起
    }
  }


  //通过加速度传感器控制机器人左臂的动作
  if(sensorAccelX > 500)
  {
    Serial.write(4); //向机器人发送4，机器人将做出左摆的动作
  }
  if(sensorAccelZ > 450)
  {
    Serial.write(6); //向机器人发送6，机器人将做出左拳的动作
  }


  //通过Wii手柄控制机器人右臂的动作
  if(sensorAccelWiiY < 154)
  {
    Serial.write(3); //向机器人发送3，机器人将做出右摆的动作
  }
  if(sensorAccelWiiX < 115)
  {
    Serial.write(5); //向机器人发送5，机器人将做出右拳的动作
  }

  delay(200);
}

```

