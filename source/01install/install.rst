安装介绍
====================================

我们提供了Linux,MacOS,Windows上的python预编译包供安装，目前pyChemiQ支持3.8、3.9、3.10版本的python。

如果您已经安装好了python环境和pip工具，pyChemiQ可通过如下命令进行安装：

.. code-block::

   pip install pychemiq


除了调用pyChemiQ的基础接口进行计算，您也可以设置配置文件直接运算，更多高级功能开放在配置文件里使用。您可以通过使用内置优化方法缩短量子线路，减少运行时间，还有切片数设置、拟设截断、MP2初参设置等丰富功能的接口可调用。如果您想试用pyChemiQ这些高级功能，请前往 `本源量子商城 <https://mall.originqc.com.cn>`_ 购买获取。ChemiQ和pyChemiQ的license是通用的，如果您已有ChemiQ的license，直接填进配置文件中全局设置的license参数即可。详细参数配置请见 :doc:`../06API/Configs`一节。