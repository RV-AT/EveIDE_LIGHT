
# EveIDE_LIGHT 使用手册
![EveIDE_LIGHT](./img/EveIDE_LIGHT.png)  
 
当前版本 : v0.0.3  （支持windows7以上版本 64位操作系统）（支持ubuntu16.04以上linux操作系统）    
作者 : Adancurusul
*****

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<!--**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*-->

- [版本说明](#%E7%89%88%E6%9C%AC%E8%AF%B4%E6%98%8E)
  - [版本部分特性](#%E7%89%88%E6%9C%AC%E9%83%A8%E5%88%86%E7%89%B9%E6%80%A7)
  - [使用方式](#%E4%BD%BF%E7%94%A8%E6%96%B9%E5%BC%8F)
    - [python脚本运行](#python%E8%84%9A%E6%9C%AC%E8%BF%90%E8%A1%8C)
    - [可执行文件运行](#%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%96%87%E4%BB%B6%E8%BF%90%E8%A1%8C)
- [概述](#%E6%A6%82%E8%BF%B0)
  - [什么是EveIDE_LIGHT](#%E4%BB%80%E4%B9%88%E6%98%AFeveide_light)
- [使用介绍](#%E4%BD%BF%E7%94%A8%E4%BB%8B%E7%BB%8D)
  - [选择工作区](#%E9%80%89%E6%8B%A9%E5%B7%A5%E4%BD%9C%E5%8C%BA)
  - [进入主界面](#%E8%BF%9B%E5%85%A5%E4%B8%BB%E7%95%8C%E9%9D%A2)
    - [左侧模组区](#%E5%B7%A6%E4%BE%A7%E6%A8%A1%E7%BB%84%E5%8C%BA)
      - [工程视图](#%E5%B7%A5%E7%A8%8B%E8%A7%86%E5%9B%BE)
      - [编译设置](#%E7%BC%96%E8%AF%91%E8%AE%BE%E7%BD%AE)
      - [仿真设置](#%E4%BB%BF%E7%9C%9F%E8%AE%BE%E7%BD%AE)
    - [右侧编辑器](#%E5%8F%B3%E4%BE%A7%E7%BC%96%E8%BE%91%E5%99%A8)
    - [顶部菜单](#%E9%A1%B6%E9%83%A8%E8%8F%9C%E5%8D%95)
      - [文件](#%E6%96%87%E4%BB%B6)
      - [视图](#%E8%A7%86%E5%9B%BE)
      - [工程](#%E5%B7%A5%E7%A8%8B)
      - [模组](#%E6%A8%A1%E7%BB%84)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

***

## 版本说明
*V003版本目前发现启动时可能出现bug正在排查中，先从release中撤下，排查完后再上架      
当前为v0.0.3  版本，在[releases](https://github.com/Adancurusul/EveIDE_LIGHT/releases   )中可以直接下载，v0.0.3为测试版本，测试版本会保留命令行窗口以便使用出现bug时可以及时向开发团队反馈    
*由于开发人员只有一个，bug可能会比较多，请见谅。    
如果使用中存在任何问题可联系 chen.yuheng@nexuslink.cn 或者 QQ：1016867898
### 版本部分特性
- 包含windows版本和linux版本
- 工程目录和ide所在目录需放在同一磁盘中（如C盘）
- 新增自定义字长打开后缀为.bin的纯二进制文件并显示
- 目前只支持UTF-8格式编码文件工程若遇无法打开IDE或文件无法打开应检查编码，或使用[批量转换工具]( https://github.com/Adancurusul/EveIDE_LIGHT/tree/main/source/modules/ChangeEncoding )批量转换为UTF-8
- 自动例化已用Racket重写，优化输出文件格式、支持一个文件下多个模组且可以独立使用，但是仍然具备一定局限，[自动例化器](https://github.com/Adancurusul/EveIDE_LIGHT/tree/main/source/modules/CreateInstance   )
  - 例化代码中input 与output 应当每行一个不能一行多个
  - 例化的模组中parameter定义前需要加上“parameter” eg：“parameter a = 0”
  - ***可能会出现例化后信号丢失或者信号多出现象，请注意检查***
- 自动查找例化算法目前支持多层查找但只在IDE中显示一层例化，后期会添加自定义层数接口
- 本版本编译时只能对工程下的main.c或main.s或main.S自动编译，此特性会在后续版本中修复

### 使用方式
#### python脚本运行 
***需要python3.8环境***

    pip install -r requirements.txt  
    python EveIDE_LIGHT.py
#### 可执行文件运行
[releases](https://github.com/Adancurusul/EveIDE_LIGHT/releases   )中可以直接下载并在source目录下找到对应平台的可执行文件并运行
    
##   概述 
###   什么是EveIDE_LIGHT
EveIDE_LIGHT 目的是为RiscV核心设计者打造一个轻量化解包即用、快速开发与验证的集成开发环境。
EveIDE_LIGHT目前集成了编辑器，仿真器和烧录器，后期还会添加Git等版本管理模块。打包后可执行很小 ,且能做到解包即用不用配置其他环境

##   使用介绍 
###   选择工作区
![选择工作区](./img/选择工作区.png)

EveIDE_LIGHT 工程管理方式为工作区，工作区下可以创建或导入多个仿真工程和编译工程，首次打开IDE时会弹出工作区目录选择，只需根据自己需要选择工作区。
可以点击select从文件管理系统中选择文件夹，曾经使用的工作区也可以通过输入框右侧下拉选项选择    
每次启动IDE默认会弹出选择窗口，也可以通过点击左下角设为默认  
选择完工作区后点击OK按钮即可进入IDE主界面,当所选文件夹不存在时IDE会报错    
![选择工作区_错误](./img/选择工作区_错误.png)

###  进入主界面
![主界面视图](./img/主界面视图.png)
选择工作目录后会进入到主界面，主界面由顶部菜单栏，左侧模组区，右侧编辑器和下部输出区域组成，EveIDE_LIGHT 本着轻量化易使用原则采用扁平化ui设计，不会有过多弹窗弹出，主要逻辑功能都在主界面可以快速使用


####  左侧模组区
左侧模组区由工程视图区，编译区和仿真区组成
#####  工程视图
工程视图提供了工作区下包含的所有编译工程的树状视图右上角三个按键分别是：展开所有节点、收缩所有节点和刷新树状视图   
![工程视图0](./img/工程视图0.png)   
点击展开所有节点后树状视图会被完全展开，点击收缩后节点会自动收缩，刷新树状视图可以重新扫描文件获得新的树状结构。   
这里以两个示例工程为例介绍下树状结构

![树状视图0](./img/树状视图0.png)  

树状结构在折叠状态为工程列表，对于所有目录下有文件的文件夹都可以通过双击或者点击小箭头打开与折叠，对于IDE支持查看的文件和能打开的文件夹都会在名字前加上图标。   

![删除文件](./img/删除文件.png)    
所有节点右键都会弹出删除节点的选项，点击删除后会弹出警告，选择yes：文件夹会连同内部文件一同被删除，文件会被直接删除选择No则不会做任何操作。   
对于c语言，EveIDE_LIGHT有一套函数识别机制（有待优化）可以帮助使用者更加直观的看到c语言下的函数，并可以通过双击函数打开该文件，同时IDE目前仅支持打开UTF-8的文件格式，其他格式会报错并无法打开，双击会产生报错警告   
![打开文件失败](./img/打开文件失败.png)   

#####  编译设置
点击左侧模组视图左边的第二个标签会进入到编译设置页面，编译后IDE会保存该工程的配置    
![编译设置](./img/编译设置.png)   
最上方左侧是工程选择，可以点击展开下拉列表选取需要编译的工程名字    
 ![选择工程](./img/选择工程.png)     
可以在toolchain那一栏配置自己的工具链，可以将自己的工具链bin文件路径填入，IDE会自动识别工具链前缀，如该目录下无gcc工具则会在点击编译后抛出警告并停止编译   
![错误的gcc路径](./img/错误的gcc路径.png)      

gcc选择下面为指令集选择，可以根据自己工程的指令集来选择
*请使用 xxx-gcc -print-multi-lib查看支持的multilib来勾选指令集   

![选择isa](img/选择isa.png)

IDE支持自动为使用者编译，只需将Auto generate勾上即可（当为设置Auto generate时自定义编译设置将无效）  
*目前EveIDE_LIGHT只支持工程目录下的main.S和main.c自动生成，后面会继续完善    

![自动makefile](img/自动生成makefile.png)   
为了方便开发者在FPGA上和仿真器中验证，IDE为开发者设置了输出文件可选项，目前支持mif，coe，纯二进制bin，和与纯二进制区分后缀为elf的文件   

IDE默认编译输出结果存放在工程下的build文件夹（自动生成），也可以自定义输出位置    
![编译输出](img/输出文件夹选择.png)  
配置完所有选项后点击compile按钮即可编译，编译信息会在输出窗口显示   
![编译输出](img/编译输出.png)  
如果代码有错误无法成功编译则会用红色显示
![编译错误](img/编译报错.png)  
#####  仿真设置
EveIDE_LIGHT设计了一套自动寻找例化模组和头文件算法能帮助开发者实现一键仿真（有一定bug，优化中）

同时文件下模组也会显示在树状结构中
![仿真](img/仿真设置.png)  

右键树状结构中的文件可以弹出右键菜单列表，第一项为设置该文件为顶层，设置为顶层后文件名背景会变成蓝色，第二项为生成例化文件，IDE能对文件中信号进行自动例化（有bug，优化中）方便开发者调用，后面两个为打开和删除文件  
![右键菜单](img/仿真右键菜单.png)    
顶层文件中应加上例如：
   
	initial begin
    	$dumpfile("tb.lxt");
    	$dumpvars(0, counter);
	end   
以便后续能显示波形，若未添加ide会弹出警告窗口    
![仿真出错](img/仿真出错.png)           
点击仿真后会调用iverilog进行仿真，仿真结果会输出到输出框中，若无误则会弹出gtkwave用以显示波形，警告会以粉色显示在输出框，错误以红色显示
![仿真警告](img/仿真警告.png)   
![仿真报错](img/仿真报错.png)     
![仿真成功](img/仿真成功.png)         
![仿真结果](img/仿真结果.png)         


#### 右侧编辑器
EveIDE_LIGHT 本着小巧稳定的原则取消了之前的自研编辑器改为采用更加稳定易用的[monaco editor](https://github.com/microsoft/monaco-editor   )
且目前支持c，verilog，riscv汇编的高亮功能，后续还会继续优化编辑器体验。  
 *双击后缀为bin的文件由于是纯二进制文件于是IDE会读取并以64位字长的小端序显示并不支持编辑    
 也可以右键bin的树状结构根据选项选择字长（目前支持32bit 64bit 和128bit)     
 ![自定义字长显示](img/自定义显示字长.png)    
 ![显示128bit](img/字长128显示.png)
![显示bin文件](img/显示bin文件.png)    
为避免同一个工作区下不同工程的同名文件之间的干扰，当前打开文件若处于树状图中则会展开当前文件所在节点，切换文件时左侧树状结构也会同时切换     
![切换文件](img/切换显示文件.png)    
文件在被修改后会在小窗口名字后面产生一个*作为改动标记，点击保存或者Ctr+s保存后即消失    
![改动标记](img/改动标记.png)

####  顶部菜单 
#####  文件
![](img/文件菜单.png)
#####  视图 
视图菜单栏目前用于控制模组和输出区域的显示和隐藏当被选中状态时该视图会显示，可以通过单击列表项来改变视图的显示和隐藏    
![](img/视图菜单.png)
##### 工程    
用于新建工程和切换工作区    
![工程菜单](img/工程菜单栏.png)    
点击新建工程子列表后的任意一个会弹出新建工程窗口，在输入框中输入新建工程路径点击create即可生成新工程同时更新在树状视图     
![新建工程](img/新建工程.png)     
若选择的文件夹不是空文件夹IDE会弹出警告但不会修改其中内容     
![新建工程警告](img/新建工程警告.png)
#####  模组   
本版本中暂无用途