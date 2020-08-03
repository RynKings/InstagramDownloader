# Thanks to InstaBot
# Thanks to Alm. Hamzah (Zero Cool)

# Copyright by Ryns
# There are times when you will appreciate the developer (Hamzah)

from instabot import API
from instabot.bot.bot import get_media_id_from_link

client = API()

client.login()

def get_media_download_url(self, media_id, media=False):
    url_results = []
    if not media:
        self.media_info(media_id)
        if not self.last_json.get("items"):
            return True
        media = self.last_json["items"][0]
    if media["media_type"] == 1:
        images = media["image_versions2"]["candidates"]
        url_results.append({'url': images[0]["url"], 'video': False})            
    elif media["media_type"] == 2:
        clips = media["video_versions"]
        url_results.append({'url': clips[0]["url"], 'video': True})
    else:
        for index in range(len(media["carousel_media"])):
            if media["carousel_media"][index]["media_type"] != 1:
                videos = media["carousel_media"][index]["video_versions"][0]["url"]
                url_results.append({'url': videos, 'video': True})
            images = media["carousel_media"][index]["image_versions2"]["candidates"]
            url_results.append({'url': images[0]["url"], 'video': False})
    return url_results

def getMedia(url):
    media_id = get_media_id_from_link(client, url)
    response = get_media_download_url(client, media_id)
    return response

if __name__ == '__main__':
    result = getMedia('https://www.instagram.com/p/B_Xpnx6D6Bn/?utm_source=ig_web_copy_link')
    print(result)
