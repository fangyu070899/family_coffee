from linebot.models import ImagemapSendMessage,ImagemapArea,URIImagemapAction,BaseSize

def get_new_image():
  return ImagemapSendMessage(
    base_url='../imagemap',
    alt_text='新品上市!',
    base_size=BaseSize(height=1040, width=1040),
    actions=[
        URIImagemapAction(
            link_uri='https://google.com/',
            area=ImagemapArea(
                x=0, y=0, width=1040, height=1040
            )
        )
    ]
)