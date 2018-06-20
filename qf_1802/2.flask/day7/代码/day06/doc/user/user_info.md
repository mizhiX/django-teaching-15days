
### 获取用户信息

#### 请求

    GET /user/user/

##### params
    id int 用户id

#### 响应

成功响应：

    {
      "code": 200,
      "data": {
        "avatar": "upload\\page.png",
        "id": 2,
        "name": "\u59b2\u5df11",
        "phone": "18200384772"
      }
    }

失败响应：

    {
        'code': 0,
        'msg': '数据库错误，请稍后重试'
    }
