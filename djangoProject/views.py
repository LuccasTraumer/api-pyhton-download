import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from wsgiref.util import FileWrapper

from djangoProject import MyPytube, CONSTANTES
from djangoProject.DataResource import DataResourse
from djangoProject.VideoData import VideoData

@csrf_exempt
def index(request):
    dataInfo = object
    if request.method == 'POST':
        request.body
        objs = json.loads(request.body)
        dataRes = DataResourse(objs['url'], objs['typeFile'], objs['resolutionVideo'])

        videoData = getTypeFile(dataRes)
        selectedFile(videoData)
        videoData.name = CONSTANTES.TITLE
        return buildVideoResponse(videoData)


def buildVideoResponse(videoData = VideoData):
    path = (CONSTANTES.CAMINHO_DOWNLOAD + '-' + CONSTANTES.TITLE +'.'+ videoData.typeFile).replace('-', ('\ '.strip()))

    file = FileWrapper(open(path.replace('\\', '\ '), 'rb'))
    response = HttpResponse(file, content_type='video/mp4')
    response['Content-Disposition'] = 'attachment; filename='+ CONSTANTES.TITLE + videoData.typeFile
    return response
    # return HttpResponse('Hellow')


def getTypeFile(dataResourse):
    videoOrAudio = dataResourse.typeFile
    link_videos = dataResourse.url
    return VideoData(link_videos, videoOrAudio, '')


def getPlaylits(videoData=VideoData):
    print(MyPytube.download_playlist(videoData.linkVideo))

def getMP3(videoData=VideoData):
    return MyPytube.download_audio(videoData.linkVideo)

def getMP4(dataResourse = DataResourse):
    return MyPytube.download_video(dataResourse.url, dataResourse.resolutionVideo)


def selectedFile(videoData=VideoData):
    if videoData.typeFile in CONSTANTES.TYPE_FILES:
        if videoData.typeFile.lower() == CONSTANTES.MP3:

            return getMP3(videoData)

        elif videoData.typeFile.lower() == CONSTANTES.MP4:
            return getMP4(videoData)

        else:
            getPlaylits(videoData)
