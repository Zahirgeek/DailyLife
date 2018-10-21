## Flask-RESTFul
- 在flask_restful基础上对request优化,增加reqparse
- reqparse
    - 定义RequestParser对象
        
            parser = reqparse.RequestParser()
            
    - 接收字段
        
            # 实现预校验
            # required=True    必须提交该字段
            # type=str    字段必须提交str类型
            # help    错误提示
            # action="append"    一个字段添加多个值
            # location = "form"    指定字段从表单中获取["form"->表单, "args"->url, "headers", "cookies","files"]
            # dest    起别名
            
            parser.add_argument("g_name", required=True, help="please input g_name")
    
    - args = parser.parse_args()
    
            args = parser.parse_args()

            g_name = args.get("g_name")