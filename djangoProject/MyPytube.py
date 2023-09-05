import pytube
from djangoProject import CONSTANTES
from djangoProject.VideoData import VideoData

resolucoes = ['144p', '240p', '360p', '480p', '720p', '1080p', '144', '240', '360', '480', '720', '1080']
def download_video(link_video = str, resolução='360p'):
    try:
        youtube = pytube.YouTube(link_video).streams
        CONSTANTES.TITLE = str(pytube.YouTube(link_video).title)
        if resolução in resolucoes:
            for index in resolucoes:
                if resolução == resolucoes[index]:
                    resolução = (f"{resolução}p")
                    break

    except:
        return 'URL invalida!'
    else:
        return youtube.filter(res=resolução).first().download(CONSTANTES.CAMINHO_DOWNLOAD)

def download_audio(link_video=str):
    try:
        youtube = pytube.YouTube(link_video).streams.filter(only_audio=True).first().download(CONSTANTES.CAMINHO_DOWNLOAD)
        CONSTANTES.TITLE = str(pytube.YouTube(link_video).title)
        return youtube
    except:
        return "Erro ao Baixar Audio!"

# def download_playlist(link_playlist = str):
#     try:
#         playlist = pytube.Playlist(link_playlist)
#         print(f"Existem {len(playlist.video_urls)} videos na Playlist!")
#         playlist.download_all(CONSTANTES.CAMINHO_DOWNLOAD+"/playlist")
#     except:
#         return "Erro ao fazer Download da Playlist"
#     else:
#         return "Download Exceutado com Sucesso!"
