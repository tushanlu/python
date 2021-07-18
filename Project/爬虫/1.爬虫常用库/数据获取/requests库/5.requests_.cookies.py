import requests

# cookies参数的使用
url = 'https://github.com/guyuexuehu'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52',

}
temp ='_octo=GH1.1.815999488.1597771855; tz=Asia%2FShanghai; _device_id=c63501eb33dd963104d90774d91c60f9; user_session=rlvFP4JnhrUCMmXWPCMPYbcbuUWKJFyfOq4LUi2SKIM6UgMI; __Host-user_session_same_site=rlvFP4JnhrUCMmXWPCMPYbcbuUWKJFyfOq4LUi2SKIM6UgMI; tz=Asia%2FShanghai; logged_in=yes; dotcom_user=moyanmowen; has_recent_activity=1; _gh_sess=VdTyjeuvYxtg%2F2JQWCb7%2F65alWnhUuY6GFelkhVqkrHPHIVHUntv%2Fm8BwmpUkkHW5F8x8N3%2B2Bwe1X3D7McdkKDs6momBjVsNe5Exzw49w2c2uyr%2FwAuS7xgHj7Oa3ZZHsjxR1oibDuJSTEcVU07pv3AYLU7HNBYWEcmHkd04WiA1jRFR65%2BdV3I11l5xpl8hbRlx8iRJyF6RdPSJ67o5Qw25t%2Fhvh3O%2FI9zHnqnG6O3ehetiLv%2BwweW5ak7ZAqZBIDvyf8Pby5k4C9Nnaq2w5PomAKpNrYkW73a6MZtgLoCJfGk1VDCPq16kto9n2esgnRXVi58BWfgcEOVLn%2FV9w%2BKqritwWZbp%2BIOATmaIYWEvEya9ZzQl9V82Pl8gZUq86%2F0GHzhKOF2evQLsmIaMxjD2CSJmp%2BKTCtPgfnx7yzdGjpQXYe88wcxHQlmpm%2BqfRCZ%2FF4yvCrgjyvOAf%2BHZ4oDbNEUgTNnkD%2Fyv2Hp3aipf8gGH9zrYsesMb7tUs335AQYXRt0aJo2E0uucKkFkpC7S9MfX0aNti1PSjwimSzcj%2B6%2FAbB42kGLw%2B0eTuaV3Hk9MS3cahMR0ZlgR8UWpdG7hxA6XCuWnNDPRggAOxP2uJlnMBo6A4l2Mxoie61ZCxYfGufMasZHJOLAkE%2Fx4YLi6%2BBYq4ikn7V%2Fyw%3D%3D--vp5PWkFlwDu78DcH--AmnGqkv%2BlxdvGAO65M%2BYMQ%3D%3D'
cookie_list = temp.split(';')
cookies = {cookie.split('=')[0]: cookie.split('=')[1]for cookie in cookie_list}
# cookies_dict = {}
# for cookie in cookies:
#     cookies_dict[cookie.split('=')[0]] = cookie.split('=')[-1]

print(cookies)

response = requests.get(url, headers=headers, cookies=cookies)
print(response.content.decode())
# 注意：cookie一般是有过期时间的，一旦过期需要重新获取

