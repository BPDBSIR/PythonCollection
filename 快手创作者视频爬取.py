import requests
import json


def requestVideo():
    payload = {
        "operationName": "visionProfilePhotoList",
        "query": "query visionProfilePhotoList($pcursor: String, $userId: String, $page: String, $webPageArea: String) {\n  visionProfilePhotoList(pcursor: $pcursor, userId: $userId, page: $page, webPageArea: $webPageArea) {\n    result\n    llsid\n    webPageArea\n    feeds {\n      type\n      author {\n        id\n        name\n        following\n        headerUrl\n        headerUrls {\n          cdn\n          url\n          __typename\n        }\n        __typename\n      }\n      tags {\n        type\n        name\n        __typename\n      }\n      photo {\n        id\n        duration\n        caption\n        likeCount\n        realLikeCount\n        coverUrl\n        coverUrls {\n          cdn\n          url\n          __typename\n        }\n        photoUrls {\n          cdn\n          url\n          __typename\n        }\n        photoUrl\n        liked\n        timestamp\n        expTag\n        animatedCoverUrl\n        stereoType\n        videoRatio\n        __typename\n      }\n      canAddComment\n      currentPcursor\n      llsid\n      status\n      __typename\n    }\n    hostName\n    pcursor\n    __typename\n  }\n}\n",
        "variables": {
            "userId": "3x9ajiduhvmw872",
            "pcursor": "",
            "page": "profile"
        }
    }
    headers = {
        "cookie": "kpf=PC_WEB; kpn=KUAISHOU_VISION; clientid=3; did=web_ec6b7fc1d088b4d356efc720c1412339"
    }
    print(json.dumps(payload))
    response = requests.post("https://www.kuaishou.com/graphql", headers=headers, data=json.dumps(payload))
    print(response.text)


def get_full_name(first_name: str, last_name: str):
    pass


if __name__ == '__main__':
    requestVideo()
