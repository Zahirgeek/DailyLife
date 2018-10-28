# Exam

- 接口测试写在文件apitest.py

### 考点要求
- 数据库统一使用默认数据库SQLite
- 实现以下Api
  - 用户Api
    - 用户邮箱，手机号注册
    - 用户登录（删除用户不可登录）
      - 验证码和密码登录（密码实现数据安全）
    - 用户信息修改
    - 用户逻辑删除
      - 超级管理员可以操作
  - 博客Api
    - 博客创建
        + 只有登录用户可创建，并绑定到登录用户上
    - 博客修改
        + 只有博客创建者和超级管理员可修改
    - 博客删除
        + 只有超级管理员可以删除
  - 用户，博客结合操作
    - 收藏博客
    - 获取某用户的所有收藏
    - 获取收藏某博客的所有用户
- 热度API
    + 博客点击量统计
    + 最火博客排名

## 表参考

### 用户表

- u_phone
- u_password
- u_icon
- is_delete



### 博客表

- b_title
- b_content



### 收藏表

- u_id
- b_id
