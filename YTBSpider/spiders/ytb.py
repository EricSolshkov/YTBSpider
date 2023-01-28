import os.path

import requests
import scrapy
from YTBSpider.items import VideoItem
from YTBSpider.items import PlaylistItem
from YTBSpider.items import CommentItem
import re
import json
import YTBSpider.settings
from YTBSpider.pipelines import pre_process as pp

import googleapiclient.discovery as gac


def ytinit():
    pass


def timeParser(str):
    str = re.sub("PT", "", str)
    str = re.sub("H", "hour", str)
    str = re.sub("M", "min", str)
    str = re.sub("S", "sec", str)
    return str



class YtbSpider(scrapy.Spider):
    name = 'ytb'
    allowed_domains = ['www.youtube.com']
    start_urls = ['https://www.youtube.com/@raphafilms/playlists/']

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyCGtTXjhfCIVKqCRF0udSzKf8Ok1m73XOA"

    youtube = gac.build(
        api_service_name,
        api_version,
        developerKey=DEVELOPER_KEY
    )

    def parse(self, response):
        #prepare comment container
        path = os.path.abspath(".\\comments")
        if not os.path.exists(path):
            os.makedirs(path)
        filename = "total_comments.csv"
        out = open(os.path.join(path, filename), "w+", encoding="utf-8")

        # parse playlist site to get a list of playlists.
        response.body.decode(response.encoding)
        web_str = response.text
        videos = []
        words_count = {}
        # deal with ytInitialData
        str_head = 0
        str_tail = 0
        for i in re.finditer(r'var ytInitialData', web_str):
            str_head = i.span()[1]
        for i in re.finditer(r'frameworkUpdates', web_str):
            str_tail = i.span()[0]
        if str_head == 0:
            print("no matching head\n")
        if str_tail == 0:
            print("no matching tail")

        ytInitialDataStr = web_str[str_head + 3:str_tail - 2] + '}'
        ytInitialData = json.loads(ytInitialDataStr)

        # locate playlist containers and detect playlist items.
        with open("debug_playlists.txt", 'w+', encoding="utf-8") as f:
            f.write(ytInitialDataStr)
            f.flush()
        f.close()
        playlistsContainers = ytInitialData['contents']['twoColumnBrowseResultsRenderer']['tabs'][3]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['gridRenderer']['items']
        playlists = []

        for container in playlistsContainers:
            playlist_item = PlaylistItem()
            if 'gridPlaylistRenderer' in container:
                playlist_item["title"] = container['gridPlaylistRenderer']['title']['runs'][0]['text']
                playlist_item["video_count"] = container['gridPlaylistRenderer']['videoCountText']['runs'][0]['text']
                playlist_item["playlist_id"] = container['gridPlaylistRenderer']['playlistId']
                playlists.append(playlist_item)

        print(str(len(playlists))+" playlists found.\n")

        # get video links via playlists
        for playlist in playlists:
            my_request = self.youtube.playlistItems().list(
                part="snippet",
                maxResults=999,
                playlistId=playlist['playlist_id']
            )

            response = my_request.execute()
            #response_json = json.loads(response)
            print("playlist "+ playlist['playlist_id']+" contains "+str(len(response['items']))+" videos\n")
            for videoInfo in response['items']:
                video = videoInfo['snippet']['resourceId']['videoId']
                if video in videos:
                    continue
                else:
                    videos.append(video)

        # parse video meta and comments
        total = len(videos)
        print("total "+str(total)+" videos found.\n")
        index = 1
        for video_id in videos:
            print("processing "+video_id+" :"+str(index)+"/295\n")
            index += 1
            item = VideoItem()
            #parse video meta
            request = self.youtube.videos().list(
                part="snippet,contentDetails,statistics",
                id=video_id
            )
            response = request.execute()
            #meta = json.loads(response.text)

            response = response['items']
            # private video exception.
            if len(response) == 0:

                print(video_id+" is private\n")
                item['video_id'] = video_id
                item['release_time'] = '0'
                item['title'] = '0'
                item['description'] = '0'
                item['duration'] = '0'
                item['view_count'] = '0'
                item['like_count'] = '0'
                item['comment_count'] = '0'
                yield item
            else:
                response = response[0]

                snippet = response['snippet']
                details = response['contentDetails']
                statistics = response['statistics']

                item['video_id'] = video_id
                item['release_time'] = snippet['publishedAt']
                item['title'] = snippet['title']
                item['description'] = snippet['description']
                item['duration'] = timeParser(details['duration'])
                item['view_count'] = statistics['viewCount']
                item['like_count'] = statistics['likeCount']
                item['comment_count'] = statistics['commentCount']

                yield item

                # parse comments
                comments = []
                request = self.youtube.commentThreads().list(
                    part="snippet",
                    maxResults=999,
                    videoId=video_id
                )
                response = request.execute()
                comments_json = response
                for container in comments_json["items"]:
                    snippet = container['snippet']['topLevelComment']['snippet']
                    comment_item = CommentItem()
                    comment_item['user_id'] = snippet['authorDisplayName']
                    comment_item['comment_time'] = snippet['publishedAt']
                    comment_item['content'] = snippet['textOriginal']
                    comment_item['like_count'] = snippet['likeCount']

                    comments.append(comment_item)

                while "nextPageToken" in comments_json:
                    request = self.youtube.commentThreads().list(
                        part="snippet",
                        maxResults=999,
                        pageToken=comments_json['nextPageToken'],
                        videoId=video_id
                    )
                    response = request.execute()
                    comments_json = response
                    for container in comments_json["items"]:
                        snippet = container['snippet']['topLevelComment']['snippet']
                        comment_item = CommentItem()
                        comment_item["user_id"] = snippet['authorDisplayName']
                        comment_item["comment_time"] = snippet['publishedAt']
                        comment_item["content"] = ''.join((snippet['textOriginal']).splitlines())
                        comment_item['like_count'] = snippet['likeCount']

                        comments.append(comment_item)

                # output comments


                for comment in comments:
                    out.write(pp(video_id))
                    out.write(',')
                    out.write(pp(comment['user_id']))
                    out.write(',')
                    out.write(pp(comment['comment_time']))
                    out.write(',')
                    out.write(pp(comment['content']))
                    out.write(',')
                    out.write(str(comment['like_count']))
                    out.write('\n')
                    out.flush()
        out.close()







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
        print("parsing meta of "+str(video_id)+"| title is "+str(title)+"\n")
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

        comments = []
        request = self.youtube.commentThreads().list(
            part="snippet",
            maxResults=999,
            videoId=video_id
        )
        response = request.execute()
        comments_json = response
        for container in comments_json["items"]:
            snippet = container['snippet']['topLevelComment']['snippet']
            comment_item = CommentItem()
            comment_item['user_id'] = snippet['authorDisplayName']
            comment_item['comment_time'] = snippet['publishedAt']
            comment_item['content'] = snippet['textOriginal']
            comment_item['like_count'] = snippet['likeCount']

            comments.append(comment_item)

        while "nextPageToken" in comments_json:
            request = self.youtube.commentThreads().list(
                part="snippet",
                maxResults=999,
                pageToken=comments_json['nextPageToken'],
                videoId=video_id
            )
            response = request.execute()
            comments_json = response
            for container in comments_json["items"]:
                snippet = container['snippet']['topLevelComment']['snippet']
                comment_item = CommentItem()
                comment_item["user_id"] = snippet['authorDisplayName']
                comment_item["comment_time"] = snippet['publishedAt']
                comment_item["content"] = snippet['textOriginal']
                comment_item['like_count'] = snippet['likeCount']

                comments.append(comment_item)


        print("\n")

        item['video_id'] = video_id
        item['title'] = title
        item['duration'] = seconds
        item['keywords'] = keywords
        item['view_count'] = view_count
        item['description'] = description
        item['release_time'] = release_time
        item['likes'] = likes
        item['comments'] = comments

        yield item
