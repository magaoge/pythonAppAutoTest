from appium.webdriver.common.mobileby import MobileBy


class PublictionPageElement:
    # 3个月后显示的按钮
    snooz_button = (MobileBy.ID,"au.com.lexisnexis.lexisred.preview:id/tvSnooze")

    # 导航栏搜索、下载、帮助、更多图标
    image_views= (MobileBy.XPATH,"//android.widget.TextView[@resource-id,'au.com.lexisnexis.lexisred.preview:id/imageView1']")

    # DL
    DL_button = (MobileBy.ID,"au.com.lexisnexis.lexisred.preview:id/tvDigitalLibrary")

