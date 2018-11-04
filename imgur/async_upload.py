from imgurpython import ImgurClient
import os
import asyncio

class uploader():

  def __init__(self):
    self.client_id = os.environ.get('Client_ID')
    self.client_secret = os.environ.get('Client_Secret')
    self.access_token = os.environ.get('access_token')
    self.refresh_token = os.environ.get('refresh_token')
    self.client = ImgurClient(self.client_id, self.client_secret, self.access_token, self.refresh_token)

  async def upload_photo(self, image_url, album):

    config = {
      'album': album,
    }
    print(config)

    print("Uploading image... ")
    try:  
      image = self.client.upload_from_url(image_url, config=config, anon=False)
    except Exception as e:
      print(e)
    print("Done")

if __name__ == "__main__":
  # print("refresh_token={}".format(os.environ.get('refresh_token')))
  # uploader = uploader()
  # uploader.upload_photo("http://images.performgroup.com/di/library/omnisport/d/49/rose-derrick-usnews-getty-ftr_g3codycqfuf91veyq2qtvdma1.jpg?t=-1980713401&w=960&quality=70",'P8Kuvtc')


# async def factorial(name, number):
#     f = 1
#     for i in range(2, number + 1):
#         print(f"Task {name}: Compute factorial({i})...")
#         await asyncio.sleep(1)
#         f *= i
#     print(f"Task {name}: factorial({number}) = {f}")

# async def main():
#     # Schedule three calls *concurrently*:
#     await asyncio.gather(
#         factorial("A", 2),
#         factorial("B", 3),
#         factorial("C", 4),
#     )

# asyncio.run(main())