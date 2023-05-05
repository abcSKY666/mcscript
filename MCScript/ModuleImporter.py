"""
MCScript | ModuleImporter
参考: https://blog.csdn.net/weixin_44733774/article/details/126553664
主页: https://blog.csdn.net/weixin_44733774

"""





import os
import sys

class Importer:
    def __init__(self, path):
        """
        path请传入globals()
        """
        self.__context=path
    def Import(self,module,args=None):
        '''
            module为模块名所在路径(不需要.py后缀)，支持相对路径：
                导入上一级名为M的模块，那么module='../M'
                导入目录A下的名为M的模块，那么module='A/M'
            args为从module中导入的变量名或者变量名列表：
                如果args为空，那么仅导入模块module
                如果args不为空，那么将导入模块module中的变量
                
            例子：
                Import('M')：导入模块M。【类似于import M】
                Import('M','info')：导入模块M中名为info的变量。【类似于from M import info】
                Import('M',('info','func'))：导入模块M中名为info和func的变量。【类似于from M import info,func】
                Import('M','*'):导入模块M中所有内容。【类似于from M import *】
                Import('../M')：导入上级目录中的模块M
                Import('A/M')：导入A目录下的模块M
            注：
                ①、请不要传入各种奇奇怪怪的值，我可没做好各种极端情况的预防工作
                ②、import失败必然会抛出异常，这没得洗的。请注意自己的代码规范
                ③、经常出现“鸡与蛋的先后问题”。请将该文件复制到要跨目录导入的脚本所在的目录下
        '''
        absolutePath = os.path.split(self.__context['__file__'])[0]#调用该函数的文件所在的路径(绝对路径)
        relativePath,__module=os.path.split(module)#模块所在目录(相对路径)、模块名
        path=os.path.join(absolutePath,relativePath)#模块所在路径(绝对路径)
        
        sys.path.append(path)
        context={}

        if(args):
            if(type(args)==str):
                exec(f'from {__module} import {args}',context)
            else:
                exec(f'from {__module} import {",".join(args)}',context)
        else:
            exec(f'import {__module}',context)
        self.__context.update(context)

        sys.path.pop()