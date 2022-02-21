from appium.webdriver.common.mobileby import MobileBy

class LoginPageElement:
    skip_guide_button = (MobileBy.ID, 'au.com.lexisnexis.lexisred.preview:id/tvSkipTour')
    # 国家
    region_choose = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Australia")')
    # 邮箱
    email_input = (MobileBy.ID, 'au.com.lexisnexis.lexisred.preview:id/etEmail')
    # 密码
    password_input = (MobileBy.ID, 'au.com.lexisnexis.lexisred.preview:id/etPassword')
    # 记住密码
    remember_pwd = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.ImageView").resourceId("au.com.lexisnexis.lexisred.preview:id/ivRememberPasswordCheckBox")')
    # 忘记密码
    # 提报问题
    # 登录
    login_button = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("LOGIN")')

    # 登陆失败（密码或者账号错误）
    login_fail = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("The email address you entered is not correct.")')


    # 选择billing account ，这里为了方便测试，就只选我们想要的
    billing_account = (MobileBy.XPATH,'//android.widget.TextView[@*="Staging Shanghai-999999"]')
    open_billing_account = (MobileBy.ID, "au.com.lexisnexis.lexisred.preview:id/tvSave")