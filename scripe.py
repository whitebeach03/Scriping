import time
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from utils import get_usernames_from_dialog, reflesh_sleep, go_to_profile

def main():
    # Instagramのログイン情報
    parser = argparse.ArgumentParser(description='username and password')
    parser.add_argument('--username', help='your username')
    parser.add_argument('--password', help='your password')
    args = parser.parse_args()
    
    USERNAME = args.username
    PASSWORD = args.password

    # Seleniumの設定
    driver = webdriver.Chrome()
    driver.get('https://www.instagram.com/')

    # ログイン処理
    time.sleep(3)
    username_input = driver.find_element(By.NAME, 'username')
    password_input = driver.find_element(By.NAME, 'password')
    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)

    # プロフィールページへ移動
    go_to_profile(driver, USERNAME)

    # フォロー中リストをクリック
    driver.find_element(By.XPATH, '//a[contains(@href, "/following/")]').click()
    time.sleep(3)
    # フォロー中ユーザの抽出
    follows_usernames = get_usernames_from_dialog(driver, '//div[@role="dialog"]//div[contains(@class, "xyi19xy x1ccrb07 xtf3nb5 x1pc53ja x1lliihq x1iyjqo2 xs83m0k xz65tgg x1rife3k x1n2onr6")]')
    
    # フォローリスト取得後，profileに戻る
    reflesh_sleep(driver)

    # # フォロワーリストをクリック
    driver.find_element(By.XPATH, '//a[contains(@href, "/followers/")]').click()
    time.sleep(3)
    # フォロワーユーザの抽出
    followers_usernames = get_usernames_from_dialog(driver, '//div[@role="dialog"]//div[contains(@class, "xyi19xy x1ccrb07 xtf3nb5 x1pc53ja x1lliihq x1iyjqo2 xs83m0k xz65tgg x1rife3k x1n2onr6")]')

    # フォロー中だがフォロワーではないユーザーを探す
    not_following_back = [user for user in follows_usernames if user not in followers_usernames]

    print("フォロー中だがフォロワーではないユーザーリスト:")
    print(not_following_back)

    # ブラウザを閉じる
    driver.quit()

if __name__ == '__main__':
    main()
