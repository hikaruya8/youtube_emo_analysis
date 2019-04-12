import requests
import json
import settings

url = 'https://www.googleapis.com/youtube/v3/'
API_KEY = settings.AP

def print_video_comment(video_id, n=10):
    params = {
        'key': API_KEY,
        'part': 'snippet',
        'videoId': video_id,
        'order': 'relevance',
        'textFormat': 'plaintext',
        'maxResults': n,
    }
    response = requests.get(url + 'commentThreads', params=params)
    print('URL')
    print(response.url)

    json_data = response.json()

    import pdb; pdb.set_trace()

    for item in json_data['items']:
        # コメント
        text = comment_info['snippet']['topLevelComment']['snippet']['textDisplay']
        # グッド数
        like_cnt = comment_info['snippet']['topLevelComment']['snippet']['likeCount']
        # 返信数
        reply_cnt = comment_info['snippet']['totalReplyCount']

        try:
            print('{}\nグッド数: {} 返信数: {}\n'.format(text, like_cnt, reply_cnt))

        except Exception as ex:
            # cp932以外の文字をエンコード時
            pass

def main():
    video_id = 'Os2OB4YisOM'
    n = 5
    print_video_comment(video_id, n)

if __name__ == '__main__':
    main()



# print('取得するコメント数を入力')
# n = input()
# print('video_idを入力')
# video_id = input()