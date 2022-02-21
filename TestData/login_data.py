login_success_data = [
   # 正确数据，
    # 注：正确的数据一定要放在最后，否则直接登录进去了，就不能输入错误的数据了
    # 也可以通过用例执行类中，用例执行的函数名或者用例执行组类来控制执行顺序，将数据分成争取的数据和不正确的不同的数据组
{"Email":"Gaoge.Ma@Lexisnexis.com","password":"1234567a","expect":"可以是对 billing account 选择框是否出现的判断"}
]

login_erro_data = [
    # 密码不对
    {"phoneNum":"16621710374","password":"magaoge..","expect":"登录失败,请确认账号和密码正确"}
    # 账号不对
    ,{"phoneNum":"16621710375","password":"magaoge..00","expect":"登录失败,请确认账号和密码正确"}
    # 账号不对
    ,{"phoneNum": "16621710375", "password": "magaoge..00", "expect": "========故意做错的断言=========="}
]