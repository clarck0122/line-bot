from helper.ptt_class import ptt_craw
from db.connect import Heroku_DB
from imgur.upload import uploader
import os 
import requests

if __name__ == "__main__":

    ptt_beauty_album_id = os.environ.get('ptt_beauty_Album_ID')

    # conn = Heroku_DB()
    uploader = uploader()
    ptt_craw = ptt_craw()

    content, index_list = ptt_craw.ptt_beauty(requests)

    print(index_list)

    # for index_url in index_list:
    #     uploader.upload_photo(index_url, ptt_beauty_album_id)