from fastapi import FastAPI
import requests
import json

app = FastAPI()


@app.get("/")
async def root():
    res = requests.post("https://www.kuaishou.com/graphql", json={
        "operationName": "visionVideoDetail",
        "variables": {
            "photoId": "3xsqwz5zjkebj3i",
            "page": "detail",
            "webPageArea": "homexxbrilliant"
        },
        "query": "query visionVideoDetail($photoId: String, $type: String, $page: String, $webPageArea: String) {\n visionVideoDetail(photoId: $photoId, type: $type, page: $page, webPageArea: $webPageArea) {\n status\n type\n author {\n id\n name\n following\n headerUrl\n __typename\n }\n photo {\n id\n duration\n caption\n likeCount\n realLikeCount\n coverUrl\n photoUrl\n liked\n timestamp\n expTag\n llsid\n viewCount\n videoRatio\n stereoType\n croppedPhotoUrl\n manifest {\n mediaType\n businessType\n version\n adaptationSet {\n id\n duration\n representation {\n id\n defaultSelect\n backupUrl\n codecs\n url\n height\n width\n avgBitrate\n maxBitrate\n m3u8Slice\n qualityType\n qualityLabel\n frameRate\n featureP2sp\n hidden\n disableAdaptive\n __typename\n }\n __typename\n }\n __typename\n }\n __typename\n }\n tags {\n type\n name\n __typename\n }\n commentLimit {\n canAddComment\n __typename\n }\n llsid\n danmakuSwitch\n __typename\n }\n}\n"
    }, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
    })
    data = json.loads(res.text)
    return data
