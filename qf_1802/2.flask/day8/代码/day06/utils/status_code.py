
OK = 200
SUCCESS = {'code': 200, 'msg': '请求成功'}
DATABASE_ERROR = {'code': 0, 'msg': '数据库错误，请稍后重试'}

# 用户模块
USER_REGISTER_DATA_NOT_NULL = {'code': '1001', 'msg': '请填写完整的参数'}
USER_REGISTER_MOBILE_ERROR = {'code': '1002', 'msg': '手机号码不正确'}
USER_REGISTER_PASSWORD_IS_NOT_VALID = {'code': '1003', 'msg': '密码不正确'}
USER_REGISTER_MOBILE_EXSITS = {'code': '1004', 'msg': '该用户已注册，请直接登录'}

USER_LOGIN_USER_NOT_EXSITS = {'code': '1005', 'msg': '该用户未注册，请去注册'}
USER_LOGIN_PASSWORD_IS_NOT_VALID = {'code': '1006', 'msg': '密码不正确'}

USER_CHANGE_PROFILE_IMAGES = {'code': '1007', 'msg': '上传图片格式不正确'}
USER_CHANGE_PRONAME_IS_INVALID = {'code': '1008', 'msg': '用户名已重复，请重新输入'}

USER_AUTH_DATA_IS_NOT_NULL = {'code': '1009', 'msg': '实名认证信息请填写完整'}
USER_AUTH_ID_CARD_IS_NOT_VALID = {'code': '1010', 'msg': '身份证号不匹配'}

#订单模块
ORDER_BEGIN_END_DATA_NOT_NULL = {'code': '1100', 'msg': '房屋预约时间不能为空'}
ORDER_BEGIN_DATA_GT_END_DATE_ERROR = {'code': '1101', 'msg': '开始时间大于结束时间，请重新提交'}
