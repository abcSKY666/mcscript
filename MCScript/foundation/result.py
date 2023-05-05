class Result:
    """
    *** 已弃用 ***

    [Class] 函数结果数据返回类型
    ------------------------------
    init:
    - content: 内容
    - descriptable: 备注
    - type: 数据类型(可不填，自动识别)
    """
    def __init__(self, content, descriptable, type=None):
        self.content = content
        self.descriptable = descriptable
        
        if type == None:
            self.type = str(type(content).__name__)
        else:
            self.type = type

        
    
