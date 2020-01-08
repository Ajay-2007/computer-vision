from IPython.display import display, HTML
import cv2
import base64


def imshow(name, imageArray):
    # print(name)
    _, png = cv2.imencode('.png', imageArray)
    encoded = base64.b64encode(png)
    return HTML(
        data='''<p>{2}</p><img alt="{0}" src="data:image/png;base64, {1}"/>'''.format(name, encoded.decode('ascii'),
                                                                                      name))
