from imgurpython import ImgurClient
import os

class uploader():

  def __init__(self):
    self.client_id = os.environ.get('Client_ID')
    self.client_secret = os.environ.get('Client_Secret')
    self.access_token = os.environ.get('access_token')
    self.refresh_token = os.environ.get('refresh_token')
    self.client = ImgurClient(self.client_id, self.client_secret, self.access_token, self.refresh_token)

  def upload_photo(self, image_url, album):

    config = {
      'album': album,
    }
    print(config)

    print("Uploading image... ")
    image = self.client.upload_from_url(image_url, config=config, anon=False)
    print("Done")

if __name__ == "__main__":
  print("refresh_token={}".format(os.environ.get('refresh_token')))
  uploader = uploader()
  uploader.upload_photo("http://images.performgroup.com/di/library/omnisport/d/49/rose-derrick-usnews-getty-ftr_g3codycqfuf91veyq2qtvdma1.jpg?t=-1980713401&w=960&quality=70",'P8Kuvtc')
