accounts_raw.txt 装的是原始的用户名和密码，存储格式是一行用户名一行密码。
规定用户名首位为'a'则该用户为管理员。

main.py是测试程序，实际使用时可使用login_verify.check(1,name,password)命令
login_sys模块开始会进行数据库初始化，用到accounts_raw.txt。数据库中会添加密码加密值。

用到的状态返回值：
FORMATERROR（格式错误） = -1
nSUCCESSLOGIN（普通用户登录成功） = 1
aSUCCESSLOGIN（管理员登录成功） = 2
PAIRERROR（用户名和密码不匹配） = 3

格式错误判断依据：用户名长度为0或超过20；密码长度为0或超过32