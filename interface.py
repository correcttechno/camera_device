def MyHtml():
    PAGE = """\
    <html>
    <head>
    <title>MSB Parking</title>
    </head>
    <body>
    <center><h1>MSB Camera</h1></center>
    <center><img style="object-fit:contain" src="stream.mjpg" width="640" height="480"></center>
    <center><img style="object-fit:contain" src="cropped.mjpg" width="200" height="200"></center>
    <center><img style="object-fit:contain" src="realtime.mjpg" width="200" height="200"></center>
    </body>
    </html>
    """
    return PAGE
