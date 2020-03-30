import allure, pytest
class Test1:
    @allure.step("title=""测试登录的脚本")
    def test_login(self):
        print("login")
        assert  1

    @allure.step(title="测试用户名的脚本")
    def test_username(self):
        print("username")
        assert 1
    @allure.step("title=""测试密码的脚本")
    def test_password(self):
        print("password")
        assert 1