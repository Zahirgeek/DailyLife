- Flask
    - 注册
        - register
            - 设计该表实现password只能存不能取(@property)
        
            
                class Student(db.Model):

                id = db.Column(db.Integer, primary_key=True, autoincrement=True)
                s_name = db.Column(db.String(16))
                _s_password = db.Column(db.String(256))
            
                @property
                def s_password(self):
                    raise Exception("Error Action: password can't be access")
            
                @s_password.setter
                def s_password(self, value):
                    self._s_password = generate_password_hash(value)
    
    
   - 登录
        - login    
            - 登录验证
                - models.py
                    
                        def check_passwd(self, pwd):
                            return check_password_hash(self._s_password, pwd)
                            
            - flush
                - 消息闪现
        