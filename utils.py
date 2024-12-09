import time
from selenium.webdriver.common.by import By 

# フォロワークラス名：xyi19xy x1ccrb07 xtf3nb5 x1pc53ja x1lliihq x1iyjqo2 xs83m0k xz65tgg x1rife3k x1n2onr6

def go_to_profile(driver, username):
    driver.get(f'https://www.instagram.com/{username}/')
    time.sleep(3)

def get_usernames_from_dialog(driver, dialog_xpath):
    # スクロールボックスの要素を取得
    scroll_box = driver.find_element(By.XPATH, dialog_xpath)

    # スクロール処理
    last_height = 0
    while True:
        # JavaScriptでスクロールを実行
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", scroll_box)
        time.sleep(3)  # 読み込み待機

        # 新しい高さを取得して終了判定
        new_height = driver.execute_script("return arguments[0].scrollHeight;", scroll_box)
        if new_height == last_height:
            break
        last_height = new_height

    # ユーザー名の取得
    users = driver.find_elements(By.XPATH, '//div[@role="dialog"]//a[contains(@href, "/")]')
    usernames = [user.text for user in users if user.text.strip() != ""]
    return usernames

def reflesh_sleep(driver):
    time.sleep(3)
    driver.refresh()
    time.sleep(3)