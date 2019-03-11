import random
import requests
import os
from linebot.models import TextSendMessage, ImageSendMessage, ButtonsTemplate, MessageTemplateAction, ImageCarouselTemplate, TemplateSendMessage, ImageCarouselColumn, URIAction, CarouselTemplate, CarouselColumn, MessageAction
from .function import *
from .ptt_class import ptt_craw
from imgurpython import ImgurClient

ptt_craw = ptt_craw()

client_id = os.environ.get('Client_ID')
client_secret = os.environ.get('Client_Secret')
access_token = os.environ.get('access_token')
refresh_token = os.environ.get('refresh_token')
album_id = os.environ.get('Album_ID')
ptt_beauty_album_id = os.environ.get('ptt_beauty_Album_ID')

def reply_content(event_text):

    if event_text.lower() == "eyny":
        content = eyny_movie()

    elif event_text == "蘋果即時新聞":
        content = apple_news()

    elif event_text == "PTT 表特版 近期大於 10 推的文章":
        content, index_list = ptt_craw.ptt_beauty(requests)
        # for index_url in index_list:
        #     uploader.upload_photo(index_url, ptt_beauty_album_id)
    elif event_text == "近期熱門廢文":
        content = ptt_craw.ptt_hot(requests)
        
    elif event_text == "即時廢文":
        content = ptt_craw.ptt_gossiping(requests)
        
    elif event_text == "近期上映電影":
        content = movie()

    elif event_text == "科技新報":
        content = technews()
        
    elif event_text == "PanX泛科技":
        content = panx()

    elif event_text == "油價查詢":
        content = oil_price()

    if content: return TextSendMessage(text=content)
    
    if event_text == "開始玩":
        buttons_template = TemplateSendMessage(
            alt_text='開始玩 template',
            template=ButtonsTemplate(
                title='選擇服務',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/xQF5dZT.jpg',
                actions=[
                    MessageTemplateAction(
                        label='新聞',
                        text='新聞'
                    ),
                    MessageTemplateAction(
                        label='電影',
                        text='電影'
                    ),
                    MessageTemplateAction(
                        label='看廢文',
                        text='看廢文'
                    ),
                    MessageTemplateAction(
                        label='正妹',
                        text='正妹'
                    )
                ]
            )
        )
        
    elif event_text == "新聞":
        buttons_template = TemplateSendMessage(
            alt_text='新聞 template',
            template=ButtonsTemplate(
                title='新聞類型',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/vkqbLnz.png',
                actions=[
                    MessageTemplateAction(
                        label='蘋果即時新聞',
                        text='蘋果即時新聞'
                    ),
                    MessageTemplateAction(
                        label='科技新報',
                        text='科技新報'
                    ),
                    MessageTemplateAction(
                        label='PanX泛科技',
                        text='PanX泛科技'
                    )
                ]
            )
        )
        
    elif event_text == "電影":
        buttons_template = TemplateSendMessage(
            alt_text='電影 template',
            template=ButtonsTemplate(
                title='服務類型',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/sbOTJt4.png',
                actions=[
                    MessageTemplateAction(
                        label='近期上映電影',
                        text='近期上映電影'
                    ),
                    MessageTemplateAction(
                        label='eyny',
                        text='eyny'
                    ),
                    MessageTemplateAction(
                        label='觸電網-youtube',
                        text='觸電網-youtube'
                    )
                ]
            )
        )
        
    elif event_text == "看廢文":
        buttons_template = TemplateSendMessage(
            alt_text='看廢文 template',
            template=ButtonsTemplate(
                title='你媽知道你在看廢文嗎',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/ocmxAdS.jpg',
                actions=[
                    MessageTemplateAction(
                        label='近期熱門廢文',
                        text='近期熱門廢文'
                    ),
                    MessageTemplateAction(
                        label='即時廢文',
                        text='即時廢文'
                    )
                ]
            )
        )
        
    elif event_text == "正妹":
        buttons_template = TemplateSendMessage(
            alt_text='正妹 template',
            template=ButtonsTemplate(
                title='選擇服務',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/qKkE2bj.jpg',
                actions=[
                    MessageTemplateAction(
                        label='PTT 表特版 近期大於 10 推的文章',
                        text='PTT 表特版 近期大於 10 推的文章'
                    ),
                    MessageTemplateAction(
                        label='來張 imgur 正妹圖片',
                        text='來張 imgur 正妹圖片'
                    ),
                    MessageTemplateAction(
                        label='隨便來張正妹圖片',
                        text='隨便來張正妹圖片'
                    )
                ]
            )
        )
        
    elif event_text == "imgur bot":
        buttons_template = TemplateSendMessage(
            alt_text='ImageCarousel template',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/g8zAYMq.jpg',
                        action=URIAction(
                            label='加我好友試玩',
                            uri='https://line.me/R/ti/p/%40gmy1077x'
                        ),
                    ),
                ]
            )
        )

    elif event_text == "目錄":
        buttons_template = TemplateSendMessage(
            alt_text='目錄 template',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/kzi5kKy.jpg',
                        title='選擇服務',
                        text='請選擇',
                        actions=[
                            MessageAction(
                                label='開始玩',
                                text='開始玩'
                            ),
                            URIAction(
                                label='影片介紹 阿肥bot',
                                uri='https://youtu.be/1IxtWgWxtlE'
                            ),
                            URIAction(
                                label='如何建立自己的 Line Bot',
                                uri='https://github.com/twtrubiks/line-bot-tutorial'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/DrsmtKS.jpg',
                        title='選擇服務',
                        text='請選擇',
                        actions=[
                            MessageAction(
                                label='other bot',
                                text='imgur bot'
                            ),
                            MessageAction(
                                label='油價查詢',
                                text='油價查詢'
                            ),
                            URIAction(
                                label='聯絡作者',
                                uri='https://www.facebook.com/TWTRubiks?ref=bookmarks'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/h4UzRit.jpg',
                        title='選擇服務',
                        text='請選擇',
                        actions=[
                            URIAction(
                                label='分享 bot',
                                uri='https://line.me/R/nv/recommendOA/@vbi2716y'
                            ),
                            URIAction(
                                label='PTT正妹網',
                                uri='https://ptt-beauty-infinite-scroll.herokuapp.com/'
                            ),
                            URIAction(
                                label='youtube 程式教學分享頻道',
                                uri='https://www.youtube.com/channel/UCPhn2rCqhu0HdktsFjixahA'
                            )
                        ]
                    )
                ]
            )
        )

    if buttons_template: return buttons_template


    elif event_text == "來張 imgur 正妹圖片":
        client = ImgurClient(client_id, client_secret, access_token, refresh_token)
        images = client.get_album_images(ptt_beauty_album_id)
        index = random.randint(0, len(images) - 1)
        url = images[index].link
        image_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
        return image_message
        
    # elif event_text == "隨便來張正妹圖片":
        # image = requests.get(API_Get_Image)
        # url = image.json().get('Url')
        # image_message = ImageSendMessage(
        #     original_content_url=url,
        #     preview_image_url=url
        # )
        # line_bot_api.reply_message(
        #     event.reply_token, image_message)
        # 

        
    elif event_text == "觸電網-youtube":
        target_url = 'https://www.youtube.com/user/truemovie1/videos'
        rs = requests.session()
        res = rs.get(target_url, verify=False)
        soup = BeautifulSoup(res.text, 'html.parser')
        seqs = ['https://www.youtube.com{}'.format(data.find('a')['href']) for data in soup.select('.yt-lockup-title')]
        return [
                TextSendMessage(text=seqs[random.randint(0, len(seqs) - 1)]),
                TextSendMessage(text=seqs[random.randint(0, len(seqs) - 1)])
            ]
        