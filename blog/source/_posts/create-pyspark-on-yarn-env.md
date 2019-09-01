---
title: 使用jupyterlab启动pyspark任务：一种pyspark-notebook-on-yarn解决办法
date: 2019-02-02 22:29:39
tags:
---

### 背景介绍

我们集群的基本环境信息：

- 大数据组件发行版：hdp 2.6.5
- OS：centos 7.2 with python 2.7
- 每个节点固定目录配置了anaconda  with python 3.6，并安装升级了jupyter lab/notebook等

jupyter notebook的搭建方法有很多，最简单莫过于用[jupyter/all-spark-notebook](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/specifics.html#apache-spark)这个docker镜像。这个东东开发环境跑跑local模式还行，数据量一大就抓瞎了。我们集群的资源调度用的是yarn，所以需要找一种pyspark-notebook-on-yarn的方法。

<!-- more -->

[Jupyter kernels](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels)列表里面有一些pyspark的kernel，其中[sparkmagic](https://github.com/jupyter-incubator/sparkmagic)是livy server代理来访问yarn的，这样达到了自定义notebook资源的目的。实验中发现，livy总是崩溃，而且[post sessions](https://livy.incubator.apache.org/docs/latest/rest-api.html#post-sessions)的param支持不全，所以决定回归大自然，用anaconda4时代的方法。

### spark-submit

基于yarn提交任务时，加上--conf PYSPARK_PYTHON=<aux_python_path>，具体参数释意[在这里](https://spark.apache.org/docs/2.3.0/configuration.html#environment-variables) 。举个例子

```shell
spark-submit  \
--master yarn \
--deploy-mode client \
--num-executors 10 \
--executor-memory 2G \
--conf PYSPARK_PYTHON=/opt/anaconda3/bin/python \
xxx.py
```

### 修改 topology_script.py脚本

1. 使用ambari配置hdfs中`net.topology.script.file.name `，value值由`/etc/hadoop/conf/topology_script.py`改为`/etc/hadoop/conf/topology_script_py3.py`（文件随意命名，是cp原始文件来的，以后有啥问题，再恢复回去）

2. 针对性的修改topology_script_py3.py这个文件，以适配当前python环境，修改的地方有两处

   1）Replace the following print line in: 

   ```python
   def execute(self, args):
       rack_map = self.load_rack_map()
       rack = self.get_racks(rack_map, args)
       print rack
   ```

   With the following: 

   ```python
   def execute(self, args):
       rack_map = self.load_rack_map()
       rack = self.get_racks(rack_map, args)
       print (rack) # <----- this is the only change
   ```

   2）Then replace the following: 

   ```python
   import sys, os
   from string import join
   import ConfigParser
   ```

   With the following: 

   ```python
   from __future__ import print_function
   import sys, os
   try:
     from string import join
   except ImportError:
     join = lambda s: " ".join(s)
   try:
     import ConfigParser
   except ModuleNotFoundError:
     import configparser as ConfigParser
   ```

3. 将修改后的topology_script_py3.py分发到每一个hdp节点，重启响应组件

### 配置notebook

```shell
#ls /usr/hdp/看一下版本号, 这个变量的效果是防止hdp-select脚本报错
export HDP_VERSION=2.6.5.2-292 

export PYSPARK_PYTHON=/opt/anaconda3/bin/python
export PYSPARK_DRIVER_PYTHON=''/opt/anaconda3/bin/jupyter'
export PYSPARK_DRIVER_PYTHON_OPTS=' lab --port=xxxx --ip=xx.xx.xx.xx --no-browser'

#这个不用
export SPARK_HOME=
export SPARK_CONF_DIR=
export HADOOP_HOME=
export HADOOP_CONF_DIR=
```

大功告成

```shell
pyspark --master yarn --deploy-mode client  etc.  --conf spark.port.maxRetries=200 etc.
```



### 参考

1. [Unable to start Pyspark jobs when running with Python 3](https://community.hortonworks.com/content/supportkb/186304/unable-to-start-pyspark-jobs-when-running-with-pyt.html) 