import requests

BASE_URL = "http://localhost:8080"


def demo01():
    """
    模拟GET请求提交参数
    :return:
    """
    req = requests.get(BASE_URL + "/demo1", {"name": "Andu", "age": "20"})
    print(req.text)


def demo02():
    """
    模拟POST请求提交参数
    :return:
    """
    req = requests.post(BASE_URL + "/demo2", data={"name": "Andu", "age": "20"})
    print(req.text)


def demo03():
    """
    模拟POST请求提交JSON
    :return:
    """
    req = requests.post(BASE_URL + "/demo3", json={"username": "Andu", "password": "admin123"})
    print(req.text)


def demo04():
    """
    修改请求头
    :return:
    """
    req = requests.post(BASE_URL + "/demo4", data={"name": "Andu", "age": "20"}, headers={
        "aaa": "NASDnmasd"
    })
    print(req.text)


def demo05():
    """
    模拟文件上传
    :return:
    """
    req = requests.post(BASE_URL + "/demo5", data={"name": "Anu"}, files={
        "file": open("C:\\Users\\BPDBSIR\\Desktop\\cmd.php", 'rb')
    })
    print(req.text)


def demo06():
    """
    携带Cookie请求知乎我的信息接口
    :return:
    """
    req = requests.get(
        "https://www.zhihu.com/api/v4/me?include=ad_type%2Cavailable_message_types%2Cdefault_notifications_count%2Cfollow_notifications_count%2Cvote_thank_notifications_count%2Cmessages_count%2Cemail%2Caccount_status%2Cis_bind_phone%2Curl_token",
        headers={
            "Cookie": '_zap=0bb67393-febb-4c4c-8793-9568a9976199; d_c0="AWBfbzknWBOPToreZpRljsfkqIGlDvDo3FI=|1625113376"; _xsrf=ockefMAOd0el4zQIe07eOVSt950kdog5; __snaker__id=q7MMYBUWTpOuvURl; _9755xjdesxxd_=32; YD00517437729195%3AWM_TID=mCwYQPmFIVZABUUEAFdq2i5BLMBif6sQ; gdxidpyhxdE=NtGh0JW3M4pw0rVSxpf59bLjgvawq2vn%5CLyfQ5lgcGEQ9SBLa4lfu%2Fir0d3lGgve8e%2Fky%5CyZ4NVpmCy%2FNONRvVVeZDxYkCmKrW4QzChAz%2FzdoH8%2FZxDnfb6GCrkdIiT4cGamLNam8g7%2FbMvmW09KSH9rP5vzp%2F5OaaDe8dsBfx8GVXVq%3A1630629989799; YD00517437729195%3AWM_NI=yR1V0M6VYBOn%2B30P18O4PyIvqohg0CHeMwsbqiphawrSVgj0myeSSiCvk2W7dP1q4BDfbdvcdYpPjhEcsIvaH3YirI90q3gp4G1lqxHQyHyGmN40vPeFWuRVeTcKZuZ0QVA%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eed2c94da9e78789ce73b88a8ab6d44e838b8e85f839b8b788a2e646a9f5fb8bb22af0fea7c3b92abb8effb7b347f68a97a3ce66e9ed00b1b4348deca09acc7eb3b1a888b3498cbb8398f26ab3b7c089e47db28d9a88e93cafa7abb4d26381aaa5d3d63da890ff92b74a88baae85f569a887c0b1e96487bdbdaaf56b8ced978af143fbf0bfd4e67cf899ff8df4748c8fb7a9fc4daf92fcd1f55ca79a9996d15ea78cadacd97f9af09fb7c437e2a3; z_c0=Mi4xNF9Wd0NBQUFBQUFCWUY5dk9TZFlFeGNBQUFCaEFsVk5DcnNlWWdBMm1NZzNPa01hTnl0RWt4RmJTVkw4YU5vcnF3|1630629130|95fa690e3678013e91b13875bdeb3ae8ff9161df; tst=r; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1638584280,1638584386,1638607687,1638778623; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1638778623; NOT_UNREGISTER_WAITING=1; SESSIONID=CpSPERZJE1hkZYTJgjj2qWtWUSoxakDpyrVhEFkKooX; KLBRSID=c450def82e5863a200934bb67541d696|1638778639|1638778621; JOID=UFoWC0pgmpD1GGFGFmoJDuxAOKkEI-vIrF4zHVcmq_mVSzsSXW5XP54bYEwU7KNC3XvPQ-TpLynRFjaS2--wrJo=; osd=VFgXAU1kmJH_H2VEF2AOCu5BMq4AIerCq1oxHF0hr_uUQTwWX29dOJoZYUYT6KFD13zLQeXjKC3TFzyV3-2xpp0=',
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
        })
    print(req.text)


if __name__ == "__main__":
    demo06()
