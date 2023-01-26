import requests
import scrapy
from YTBSpider.items import VideoItem
import re
import json
import YTBSpider.settings

import googleapiclient.discovery as gac


class YtbSpider(scrapy.Spider):
    name = 'ytb'
    allowed_domains = ['www.youtube.com']
    start_urls = ['https://www.youtube.com/@raphafilms/videos/']
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyCGtTXjhfCIVKqCRF0udSzKf8Ok1m73XOA"

    youtube = gac.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    request = youtube.comments().list(
        part="snippet",
        parentId="5nP8J0D0ynA"
    )

    def parse(self, response):
        pass

    def parse_videolist(self, response):
        response.body.decode(response.encoding)
        test_str = response.text
        with open("../debug_video_list.txt", "w+", encoding='utf-8') as f:
            print("writing...")
            f.write(str(response.text))
            f.flush()
            f.close()
        # deal with ytInitialData
        str_head = 0
        str_tail = 0
        for i in re.finditer(r'var ytInitialData', test_str):
            str_head = i.span()[1]
        for i in re.finditer(r'frameworkUpdates', test_str):
            str_tail = i.span()[0]
        if str_head == 0:
            print("no matching head\n")
        if str_tail == 0:
            print("no matching tail")

        ytInitialDataStr = test_str[str_head + 3:str_tail - 2] + '}'
        ytInitialData = json.loads(ytInitialDataStr)
        videos = ytInitialData['contents']['twoColumnBrowseResultsRenderer']['tabs'][1]['tabRenderer']['content'][
            'richGridRenderer']['contents']

        print('less than '+ str(len(videos)) + ' detected\n')

        urls=[]
        for rir in videos:
            if 'richItemRenderer' in rir:
                subfix = rir['richItemRenderer']['content']['videoRenderer']['videoId']
                print('constructing url with subfix: '+subfix+'\n')
                url = 'https://www.youtube.com/watch?v=' + subfix + '/'
                urls.append(url)
            else:
                break

        for url in urls:
            yield scrapy.Request(url=url, headers=YTBSpider.settings.header_video, callback=self.parse_video_meta,
                                 dont_filter=True)

    def parse_video_meta(self, response):
        item = VideoItem()
        response.body.decode(response.encoding)
        f = open("debug_video_detail.txt", 'w+', encoding='utf-8')

        test_str = response.text
        for i in re.finditer('var ytInitialPlayerResponse', test_str):
            str_head = i.span()[1]
        for i in re.finditer('var meta', test_str):
            str_tail = i.span()[0]

        ytInitialPlayerResponseStr = test_str[str_head + 3:str_tail - 1]
        ytInitialPlayerResponse = json.loads(ytInitialPlayerResponseStr)

        video_id = ytInitialPlayerResponse['videoDetails']['videoId']
        title = ytInitialPlayerResponse['videoDetails']['title']
        seconds = ytInitialPlayerResponse['videoDetails']['lengthSeconds']
        keywords = ytInitialPlayerResponse['videoDetails']['keywords']
        view_count = ytInitialPlayerResponse['videoDetails']['viewCount']

        # deal with ytInitialData
        for i in re.finditer('var ytInitialData', test_str):
            str_head = i.span()[1]
        for i in re.finditer('serverBuildLabel', test_str):
            str_tail = i.span()[0]

        ytInitialDataStr = test_str[str_head + 3:str_tail - 2] + "}}]}}}"
        try:
            ytInitialData = json.loads(ytInitialDataStr)

        finally:
            f.write(str(response.text))
            f.flush()
            f.close()

        for index in range(len(ytInitialData['engagementPanels'])):
            if 'structuredDescriptionContentRenderer' in ytInitialData['engagementPanels'][index]['engagementPanelSectionListRenderer']['content']:
                description = ytInitialData['engagementPanels'][index]['engagementPanelSectionListRenderer']['content']['structuredDescriptionContentRenderer']['items'][1]['expandableVideoDescriptionBodyRenderer']['descriptionBodyText']['runs'][0]['text']
                break
            else:
                description = ''
        release_time = ytInitialData['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0][
            'videoPrimaryInfoRenderer']['dateText']['simpleText']
        likes = ytInitialData['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0][
            'videoPrimaryInfoRenderer']['videoActions']['menuRenderer']['topLevelButtons'][0][
            'segmentedLikeDislikeButtonRenderer']['likeButton']['toggleButtonRenderer']['defaultText']['simpleText']
        commentCount = ytInitialData['engagementPanels'][3]['engagementPanelSectionListRenderer']['header']['engagementPanelTitleHeaderRenderer']['contextualInfo']['runs'][0]['text']

        all_data=[]
        for commentIndex in range(commentCount):
            pass

        print("\n")

        item['video_id'] = video_id
        item['title'] = title
        item['duration'] = seconds
        item['keywords'] = keywords
        item['view_count'] = view_count
        item['description'] = description
        item['release_time'] = release_time
        item['likes'] = likes

        yield item
