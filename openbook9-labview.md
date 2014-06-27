
#基于Arduino与LabVIEW的直流电机转速控制系统
>沈金鑫 冯倩

多数的Arduino控制器都是基于Atmel公司的AVR系列单片机的，AVR单片机的片内资源非常的丰富，有ADC、定时器、外部中断、SPI、IIC、PWM等功能，且Arduino控制器的PWM采用的是定时器相位修正PWM（频率约为490Hz）和快速PWM（频率约为980Hz，Uno的5、6和Leonardo的3、11），这也就导致了全部的定时器都被被占用了，从而不能很方便的使用定时器设置一个中断来实现一个周期的任务，而一般需要通过读取系统已运行时间来判断定时时间是否已经达到。例如，通过增量式编码器来测量电机的转速，常规的单片机的程序架构是通过定时器来实现精确的时间定时，并利用外部中断来实现对脉冲数目的计数，然后计算出一定时间内脉冲的数目，从而得到转速数值并输出。

直流电机是Arduino机器人制作中的主要动力来源，但是由于电机的参数一致性有所差别，即使是相同型号的电机在相同电压下的转速都不完全相同，而且在带负载或负载不同的情况下，更加会导致电机转速发生变化，这就会导致制作的Arduino轮式机器人不能实现直线行走，因为这是一个开环控制，没有任何反馈信号返回。如果给直流电机加上编码器作为反馈器件，也就可以测量得到电机的当前转速，如果将其与设定值计算差值，并通过PID算法计算得到新的控制信号，从而可以动态的测量和控制电机的转速，形成一个闭环控制系统。

下面我们利用带有编码器的直流电机、Arduino控制器、直流电机驱动板和LabVIEW上位机软件以实验探索的形式来设计一个直流电机转速比例控制实验。

##1．TimerOne定时器库
###1.1下载及使用方法
TimerOne定时器库使用AVR单片机内部的定时器1实现定时中断的功能，其下载地址为：https://code.google.com/p/arduino-timerone/ 只需要更改几个参数即可使用定时器中断来实现周期性执行的任务。需要注意的是，如果使用了TimerOne定时器库，也就不能在相应的引脚输出PWM电压，Uno上的定时器与PWM引脚的关系如表1所示。

>表1 定时器与PWM引脚的关系

| 定时器 | OC0A | OC0B | OC1A | OC1B | OC2A | OC2B |
| -- | -- | -- | -- | -- | -- | -- |
| PWM引脚 | 6 | 5 | 9 | 10 | 11 | 3 |

TimerOne定时器库函数库中自带的ISRBlink程序如程序代码1所示，可以实现13号管脚上LED的5Hz频率的闪烁。

**程序代码1：ISRBlink示例程序**

```
#include <TimerOne.h>
void setup() {
  pinMode(13, OUTPUT);
  Timer1.initialize(100000); //设置定时器中断时间，基本单位为微秒，如设置为100000，则定时时间为0.1秒，频率为10Hz。
  Timer1.attachInterrupt( timerIsr ); // 设置用户自定义的定时器中断服务函数，每发生一次定时器中断，均会执行一次定时器中断服务函数。
}
void loop(){
//主函数，用于执行非周期性任务
}
 /*用户自定义的定时器中断服务函数*/
void timerIsr(){
    // 反转I/O口电平
    digitalWrite( 13, digitalRead( 13 ) ^ 1 );
}
```
###1.2评估定时时间的准确性
仅仅凭靠眼睛不能判断定时时间是否准确，下面我们设计一个实验来评估定时时间的准确性。我们需要将上面示例代码中的Timer1.initialize(100000)更改为Timer1.initialize(1000)，digitalWrite( 13, digitalRead( 13 ) ^ 1 )更改为digitalWrite(2, digitalRead( 2) ^ 1)，通过反转I/O的电平实现数字端口2输出500Hz的近似方波。

同时，我们使用NI USB-6009便携式数据采集卡和LabVIEW2012软件实现一个简易的模拟量采集器，将Arduino 控制器上的数字端口2和GND分别与NI USB-6009便携式数据采集卡上的AI0/AI0+和AI4/AI0-相连接，NI USB-6009便携式数据采集卡接口示意图如图1所示，Arduino Uno控制器与USB-6009便携式数据采集卡的连接图如图2所示。然后使用10kps的采样率，5秒的采样时间的参数采集Arduino 控制器上的数字端口2输出的方波信号，取其前20ms的波形如图3所示，通过波形频率分析工具测量得到其频率为499.901Hz。

另外，我们又将定时时间设置为100微秒、50微秒和25微秒，并使用NIUSB-6009便携式数据采集卡和LabVIEW 2012软件以45kps的采样率和2秒的采样时间分别采集了数字端口2输出的波形数据并进行频率分析，得到其频率分别为4999.01Hz，9998.03Hz，19996Hz。从以上数据对比分析可知，定时器的定时时间非常准确，频率测量误差主要来自于I/O反转操作延时导致的。

最后，我们还测试了OCROBOT MEGA 2560控制器、Arduino Uno控制器山寨版输出的500Hz的方波信号频率，分别为500.435Hz和499.764Hz。

![](http://doask.qiniudn.com/openbook9-labview1.png)
>图1 NI USB-6009接口示意图

![](http://doask.qiniudn.com/openbook9-labview2.png)
>图2 NI USB-6009接口示意图

![](http://doask.qiniudn.com/openbook9-labview3.png)
>图3定时器中断产生的500Hz方波信号

##2.转速测量
###2.1测量转速方法
测量转速方法有3种，分别为测频法(M法)、 测周法(T法)及混合法(M/T法)。
测频法是在一定时间内，通过测量旋转引起的单位时间内的脉冲数，实现对旋转轴转速测量的一种方法，适用于高、中转速的测量。该法本质上属于定时测角法，为提高测量的准确度，有时采用多标记或开齿的方法，其不确定度主要取决于时间测量和计数量化。

测周法是在转速脉冲的间隔内，用时钟脉冲来测量转速的一种方法，适合于低转速测量。该法实际上就是定角测量法，即用时标填充的方法来测量相当于某一旋转角度的时间间隔。在高、中转速时，可采用多周期平均来提高测量准确度，其不确定度主要取决于时间测量、计数量化及触发的不确定度。
混合法是在测频法的基础上，吸取测周法的优点汇集而成的一种转速测量方法。它是在转速传感器输出脉冲启动定时脉冲的同时，计取传感器输出脉冲个数和时钟脉冲个数，而当到达测量时间时，先停止对传感器输出脉冲的计数，在下一个定时脉冲启动之前再停止时钟脉冲的计数。因此，该种方法可在较宽的范围内使用。

此处，我们选择测频法来测量转速，其工作原理为：当被测信号在特定时间段T内的周期个数为N时，则被测信号的频率f=N/T。
###2.2转速测量程序设计
利用TimerOne定时器库来实现定时，通过外部中断对电机编码器输出的脉冲进行计数，计数值除以定时时间即为一定时间内的转速。实现1秒内转速测量的程序如程序代码2所示。

**程序代码2：转速测量程序**

```

#include <TimerOne.h>
long counter_val[2] = {0,0};  //定义数组，用于存放外部中断计数值
byte CurCnt = 0;  	//定义当前计数器标志，用于判断当前正在计数的数组
int j=0;		//定义定时器中断标志，用于判断是否发生中断
void setup() {
  delay(2000);
  Serial.begin(115200);//初始化波特率为115200
  attachInterrupt(0, counter, RISING);//设置中断方式为上升沿
  Timer1.initialize(1000000); // 设置定时器中断时间，单位微秒，此处为1秒
  Timer1.attachInterrupt( timerIsr ); // 打开定时器中断
  interrupts();  //打开外部中断
}

void loop()
{
  long lTemp = 0; //定义临时存储数据变量
  if(j==1)   //判断是否发生定时器中断，即定时时间是否到达
   {
     j=0;   //清除定时器中断标志位
    if((CurCnt&0x01) == 0) //当前使用的是偶数计数器，则上次频率值存放在第二个元素中
     {
         lTemp = counter_val[1];  //读取数组第二个元素中的数值
         counter_val[1]=0;       //读完清除原来的数值，以便下次使用
     }
     else   //当前使用的是奇数计数器，则上次频率值存放在第一个元素中
     {
       lTemp = counter_val[0];  //读取数组第二个元素中的数值
       counter_val[0]=0;  //读完清除原来的数值，以便下次使用
     }
        Serial.print("S");    //发送帧头大写S
        Serial.print( lTemp);  //发送频率数据，并回车换行
     }
}

//外部中断处理函数
void counter()
{
	//通过当前计数器来实现对外部中断计数值存储的切换
     counter_val[CurCnt& 0x01] += 1;    //发生一次中断则加1
}

//定时器中断处理函数
void timerIsr()
{
  j=1;     //置位定时器中断标志位
  CurCnt++; //当前计数器的值加1，实现另一个计数值切换
}


```

###2.3验证频率测量的准确性
前面提到了Arduino的模拟输出（PWM）的频率约为490Hz，且转速测量采用的是测频法，此时用来正好来验证一下程序设计的正确性。在上面的转速测量程序中的void setup()里面delay(2000)之前增加如下代码，以产生方波。串口输出的频率测量结果如图4所示。

```
pinMode(3,OUTPUT);
analogWrite(3,127);
```
![](http://doask.qiniudn.com/openbook9-labview4.png)
>图4 PWM频率测量结果

在图4所示的PWM频率测量结果中，去除前两个，可以发现频率值稳定在490和491，且4个490之后出现一个491，基本可以认为是490Hz。

同时，为了进一步的确认PWM的频率为490Hz，已验证频率测量的准确性，利用NI USB-6009便携式数据采集卡和LabVIEW 2012软件实现一个简易的模拟量采集器，使用10kps的采样率，5秒的采样时间的参数分别采集了PWM的占空比为10/255、127/255和245/255时的波形图，取波形图的前0.01秒，如图5、图6和图7所示，在0.01秒内约有5个周期，同时使用频率分析工具对占空比为127/255的波形数据进行分许，得到其频率为490.099Hz。

通过对基于Arduino与TimerOne定时器库的频率测量与基于LabVIEW和数据采集卡的数据对比与分析，得出频率测量非常准确。

![](http://doask.qiniudn.com/openbook9-labview5.png)
>图5 占空比为10/255时的波形

![](http://doask.qiniudn.com/openbook9-labview6.png)
>图6 占空比为127/255时的波形

![](http://doask.qiniudn.com/openbook9-labview7.png)
>图7 占空比为245/255时的波形

##2.4搭建测量转速的平台
在验证了基于Arduino与TimerOne定时器库的频率测量的准确性之后，我们就可以着手搭建一个直流电机转速测量系统。
###2.4.1 硬件平台
直流电机转速测量系统的直流电机和编码器有两者分离式，使用联轴器将两者连接起来，也有带有编码器的直流电机，此处为了简化设计，直接选用带有编码器的直流电机。JGB37-371-12V-228RPM带有编码器的直流减速电机如图8所示，额定电压为12V，额定空载转速为228rpm，其编码器为334线增量式光电编码器，其接口有6根数据线，黄色和橙色是电机电源，绿色和白色是AB相脉冲输出，红色和黑色是编码器的电源端和接地端。

![](http://doask.qiniudn.com/openbook9-labview8.png)
>图8 带有编码器的直流减速电机

![](http://doask.qiniudn.com/openbook9-labview9.png)
>图9 OCROBOT Motor Shield

OCROBOT Motor Shield 是基于Arduino Motor Shield 设计的增强版本的电机驱动器，如图9所示，电机驱动器采用独立供电、GND分离技术，且与Arduino控制器之间采用光耦隔离，这充分保证了Arduino控制器在大负载、大功率、急刹车、瞬时正反转等恶劣电磁环境下的稳定性。需要注意的是：Arduino控制器与电机驱动器应使用两块电池或者两个独立的电源，保证电机驱动板与Arduino控制板电源完全独立，从而保证其电气隔离性。OCROBOT Motor Shield的I/O口的控制功能如表2所示，如果使用电机时还会接驳其他设备应避免占用这些I/O口。

>表2 OCROBOT Motor Shield的控制引脚

| 功能 | 电机A | 电机B |
| -- | -- | -- |
| 方向 | D12 | D13 |
| 速度（PWM） | D3 | D11 |
| 制动（刹车） | D9 | D8 |

搭建的直流电机转速测量系统如图10所示。OCROBOT Motor Shield 直接堆叠在Arduino Uno控制器上，OCROBOT Motor Shield采用7.4V的锂电池供电，Arduino Uno控制器使用方口USB线连接至计算机上，提供电源且可以方便的通过串口上传数据至计算机上。电机的黄色和橙色连接至OCROBOT Motor Shield电机接口A，绿色和白色分别连接至Arduino Uno控制器的数字端口2、3，红色和黑色连接至Arduino Uno控制器的电源端口5V、GND。

![](http://doask.qiniudn.com/openbook9-labview10.png)
>图10 直流电机转速测量系统

###2.4.2 软件设计
由于JGB37-371-12V-228RPM直流减速电机的编码器输出AB相脉冲，为了充分利用两相脉冲以提高测量准确性，在程序代码2转速测量程序中的attachInterrupt(0, counter, RISING)之后增加如下代码，将B相脉冲输出也用来计数，以实现2倍频测量。JGB37-371-12V-228RPM直流减速电机的编码器为334线增量式光电编码器，也就说电机旋转一圈输出334个脉冲，2倍频之后即为668个脉冲。

>attachInterrupt(1, counter, RISING);//设置编码器B相位上升沿中断

修改完编码器部分，需要增加电机驱动部分的代码，以实现驱动直流电机旋转。由于硬件上将直流电机的电源线接在L298P的A端口，其控制信号为3、9和12，分别为PWM信号、制动信号和方向信号。需要在void setup()中的delay(2000)之后增加如下代码。当PWM值为80时，串口输出的转速如图8所示，且当PWM低于80时，减速电机输出轴不转动；将PWM设置为255时，串口输出的转速如图9所示。

```
  pinMode(12,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(9,OUTPUT);      //启用电机A的三个管脚，全部设置为输出状态
  digitalWrite(9, LOW);       //松开电机A的制动
  digitalWrite(12, HIGH);     //设置方向为正向
  analogWrite(3,80);         //设置PWM值
```
![](http://doask.qiniudn.com/openbook9-labview11.png)
>图11 PWM为80时转速数据

![](http://doask.qiniudn.com/openbook9-labview12.png)
>图12 PWM为80时转速数据

##3.转速的比例控制
###3.1PID控制方法
PID控制器（比例-积分-微分控制器），由比例单元P、积分单元I和微分单元D组成。通过Kp，Ki和Kd三个参数的设定来实现对某个变量的实时控制，主要适用于基本上线性，且动态特性不随时间变化的系统。

PID控制器是一个在工业控制应用中常见的反馈控制方法，其原理如图10所示，其将采集的数据和设定参考值进行比较，然后将这个差值通过PID三个模块计算出新的控制值用于执行，计算差值的目的是让系统的数据达到或者保持在设定的参考值。PID控制器可以根据历史数据和差别的出现率来调整输入值，使系统更加准确而稳定。

![](http://doask.qiniudn.com/openbook9-labview13.png)
>图13  PD控制基本原理

###3.2 转速比例控制的程序设计
实现了电机转速的测量，下面就要对电机转速进行比例控制了。为了提高控制系统响应的速度，将程序代码2转速测量程序中的定时时间更改为10毫秒，也就是转速的采样频率为100Hz，且由图8和图9可知，电机减速前的1秒钟转速在4500和12650之间，即10毫秒的转速在45至127之间，此处将转速设置为100，比例系数设置为3。转速比例控制的程序设计如程序代码3所示。

>程序代码3：转速比例控制的程序设计

```
#include <TimerOne.h>
#define Kp 3
#define set_point 100
long counter_val[2] = {0,0};
byte CurCnt = 0;
int j=0;
int output_value=0;
void setup()
{
  delay(2000);
  pinMode(12,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(9,OUTPUT);       //启用电机A的三个管脚，全部设置为输出状态
  digitalWrite(9, LOW);       //松开电机A的制动
  digitalWrite(12, HIGH);      //设置方向为正向旋转
  Serial.begin(115200);//初始化波特率为115200
  attachInterrupt(0, counter, RISING);//设置编码器A相位上升沿中断
  attachInterrupt(1, counter, RISING);//设置编码器B相位上升沿中断
  Timer1.initialize(10000); // 设置定时器中断时间，单位微秒
  Timer1.attachInterrupt( timerIsr ); // 打开定时器中断
  interrupts();  //打开外部中断
}
void loop()
{
  long lTemp = 0; //定义临时存储数据变量
  if(j==1)   //判断是否发生定时器中断，即定时时间是否到达
   {
     j=0;   //清除定时器中断标志位
    if((CurCnt&0x01) == 0) //当前使用的是偶数计数器，则上次频率值存放在第二个元素中
     {
         lTemp = counter_val[1];  //读取数组第二个元素中的数值
         counter_val[1]=0;       //读完清除原来的数值，以便下次使用
     }
     else   //当前使用的是奇数计数器，则上次频率值存放在第一个元素中
     {
       lTemp = counter_val[0];  //读取数组第二个元素中的数值
       counter_val[0]=0;  //读完清除原来的数值，以便下次使用
     }
        Serial.print("A");      //发送转速帧头大写A
        Serial.print( lTemp);   //发送转速数据
        output_value =( set_point -lTemp)*Kp+ output_value;  //比例计算得到控制量
        if(output_value >255)   //限制PWM在0-255范围内
        output_value =255;
if(output_value <0)   //限制PWM在0-255范围内
        output_value =0;
        analogWrite(3, output_value);      //将计算得到的控制量输出
	Serial.print("B");                //发送PWM帧头大写B
        Serial.println(output_value);       //发送PWM数据
     }
}
//外部中断处理函数
void counter()
{
     counter_val[CurCnt& 0x01] += 1;    //每一个中断加一
}
//定时器中断处理函数
void timerIsr()
{
  j=1;     //定时时间达到标志
  CurCnt++; //切换计数数组
}
```
通过串口输出的电机实际转速与PWM值的数据如图11和图12所示。其中图11为系统刚启动的时候，此时可以看出电机逐渐上升，达到128之后逐渐降至100以下，这属于系统初期的振荡；图12是系统运行一段时间之后的转速和PWM数据，转速稳定在100±2，PWM稳定在145左右。

![](http://doask.qiniudn.com/openbook9-labview14.png)
>图14 PWM为80时转速数据

![](http://doask.qiniudn.com/openbook9-labview15.png)
>图15 PWM为255时转速数据

图11和图12中的串口输出数据看起来没有图形那么直观，为此我们使用LabVIEW2012和VISA 5.3编写一个转速显示程序。前面板如图13所示，程序框图如图14所示，其中的数据解析子VI的程序框图如图15所示，其功能是解析出串口数据中的转速值和PWM值。

除了上位机显示程序之外，我们还需要对转速的比例控制程序进行部分修改，具体如下:
将

    Serial.print( lTemp);   //发送转速数据

修改为

```
if((lTemp/100) ==0)
  {
     Serial.print( 0);
     if((lTemp%100/10) == 0)
        Serial.print( 0);
  }
Serial.print( lTemp);
```
将

>Serial.println(output_value);       //发送PWM数据

修改为

```
if((output_value /100) ==0)
  {
     Serial.print( 0);
     if((output_value %100/10) == 0)
        Serial.print( 0);
  }
Serial.print(output_value);
```
![](http://doask.qiniudn.com/openbook9-labview16.png)
>图16 LabVIEW上位机前面板

![](http://doask.qiniudn.com/openbook9-labview17.png)
>图17 LabVIEW上位机程序框图

![](http://doask.qiniudn.com/openbook9-labview18.png)
>图18 数据解析程序框图

在LabVIEW上位机软件上选择Arduino Uno控制器对应的串口号，即可将电机的转速和PWM值实时的显示在LabVIEW前面板上，如图19所示。



![](http://doask.qiniudn.com/openbook9-labview20.png)
图19 转速和PWM显示在LabVIEW上位机上

###3.3 比例参数的整定及采样时间设置
搭建LabVIEW上位机软件的目的正是通过图形化的显示方式，观察转速和PWM的曲线来判断比例系数的设置值是否合适，同时借助LabVIEW上位机软件也可以较方便的实现PID控制参数的整定。下面我们在转速采样频率为100Hz的情况下将多次调整比例系数且获取其转速和PWM曲线，并对其进行分析，以寻找到合适的比例系数，而且也是一个探索的实验过程。

图20为Kp=3时转速和PWM波形图，从图中可以看出，系统前期的振荡较大，在800ms内经过7次振荡以后逐渐趋于稳定，且稳定之后的PWM波形变化较大，说明Kp的取值略过大，使得系统对转速偏差过于敏感。
###3.3 比例参数的整定及采样时间设置
搭建LabVIEW上位机软件的目的正是通过图形化的显示方式，观察转速和PWM的曲线来判断比例系数的设置值是否合适，同时借助LabVIEW上位机软件也可以较方便的实现PID控制参数的整定。下面我们在转速采样频率为100Hz的情况下将多次调整比例系数且获取其转速和PWM曲线，并对其进行分析，以寻找到合适的比例系数，而且也是一个探索的实验过程。

图17为Kp=3时转速和PWM波形图，从图中可以看出，系统前期的振荡较大，在800ms内经过7次振荡以后逐渐趋于稳定，且稳定之后的PWM波形变化较大，说明Kp的取值略过大，使得系统对转速偏差过于敏感。

![](http://doask.qiniudn.com/openbook9-labview21.png)
>图20 Kp=3时转速和PWM波形图

图21为Kp=4时转速和PWM波形图，从图中可以看出，由于Kp的取值过大，直接导致系统振荡而不能正常工作。

![](http://doask.qiniudn.com/openbook9-labview22.png)
>图21 Kp=4时转速和PWM波形图

图22为Kp=2时转速和PWM波形图，从图中可以看出，系统前期的振荡幅度较大，次数较多，PWM在600ms内经过4次振荡以后逐渐趋于稳定，且PWM波动较小，转速在30ms时达到最大值，并在400ms内经过3次振荡之后趋于稳定。

![](http://doask.qiniudn.com/openbook9-labview23.png)
>图22 Kp=2时转速和PWM波形图

图23为Kp=1时转速和PWM波形图，从图中可以看出，系统前期的振荡较小，PWM在400ms内经过2次振荡之后逐渐趋于稳定，且PWM波形很小，转速在30ms时达到最大值，并在400ms内经过2次小幅振荡后逐渐趋于稳定。

![](http://doask.qiniudn.com/openbook9-labview24.png)
>图23 Kp=1时转速和PWM波形图

图24为Kp=0.5时转速和PWM波形图，从图中可以看出，系统前期的振荡较小，PWM在400ms内经过1次调整之后逐渐趋于稳定，且PWM波形很小，转速在50ms时达到最大值，并在400ms内经过1次小幅调整后逐渐趋于稳定。转速的上升速度略微有点慢。

![](http://doask.qiniudn.com/openbook9-labview25.png)
>图24 Kp=0.5时转速和PWM波形图

图25为Kp=0.3时转速和PWM波形图，从图中可以看出，系统前期的振荡较小，PWM在400ms内经过1次调整之后逐渐趋于稳定，且PWM波形很小，转速在200ms时达到最大值，在400ms内经过1次小幅调整后逐渐趋于稳定。系统的超调量较小，且转速的上升速度较慢，起始的响应较差。

![](http://doask.qiniudn.com/openbook9-labview26.png)
>图25 Kp=0.3时转速和PWM波形图

图26为Kp=0.1时转速和PWM波形图，从图中可以看出，系统基本无振荡，PWM在200ms之后逐渐趋于稳定，且PWM波形基本不变，转速在300ms之后逐渐趋于稳定。系统的超调量非常小，且转速的上升速度非常慢，起始的响应非常差。

![](http://doask.qiniudn.com/openbook9-labview27.png)
>图26 Kp=0.1时转速和PWM波形图

综合图20-图26的波形图，根据图27控制系统效果评判，得出比例系数在0.5～1之间比较合适，有较快的上升速度，超调量适当，稳定性较高。

![](http://doask.qiniudn.com/openbook9-labview28.png)
>图27 控制系统效果评判

图20～图26是在转速采样频率为100Hz的情况下调整比例系数获取的转速和PWM曲线，通过观察曲线的形状来寻求最优的比例系数。下面我们在比例系数为1的情况，分别更改采样周期为50Hz和200Hz，即定时时间分别为20ms和5ms，20ms内的转速为200，5ms内的转速为50，转速和PWM的曲线分别如图28和图29所示。与图23相比，图28的振荡明显过大，图29的稳定时间过长，这说明比例系数和采样速率有很大的关系，一般情况下，先确定采样频率，然后不断调整比例系数。

![](http://doask.qiniudn.com/openbook9-labview29.png)
图28 Kp=1采样频率为50Hz时转速和PWM波形图

![](http://doask.qiniudn.com/openbook9-labview30.png)
图29  Kp=1采样频率为200Hz时转速和PWM波形图
