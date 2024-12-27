import os, subprocess

from ffmpeg.asyncio import FFmpeg
from pytubefix import YouTube
from .help import formatTime

class Video:
    def __init__(self, url, count):
        self.url = url
        self.yt = YouTube(url)
        
        self.count = count

    async def download(self):
        unformatted, formatted = self._getRes()
        formatted = f"{formatted[0]}p"

        audio_name = f"{self.count}_audio.mp4"
        video_name = f"{self.count}_video.mp4"

        video_path, audio_path, output_path = f"./tube/temp/videos_t/{video_name}", f"./tube/temp/audios/{audio_name}", f"./tube/videos/{video_name}"

        try:
            video = self.yt.streams.filter(res=formatted).first()
            audio = self.yt.streams.filter(only_audio=True, mime_type="audio/mp4").order_by('bitrate').desc().first()
            audio.download(output_path="./tube/temp/audios/", filename=audio_name)
            video.download(output_path="./tube/temp/videos_t/", filename=video_name)
        except KeyError:
            return "Запрашиваемое видео недоступно."
        except ValueError:
            return "Неверная ссылка."
        except Exception as e:
            return "Произошла непредвиденная ошибка при загрузке видео: " + str(e)

        ffmpeg = (
            FFmpeg()
            .input(url=video_path)
            .input(url=audio_path)
            .output(output_path, **{"c:v": "copy"})
        )
        print(audio_path, video_path, output_path)
        await ffmpeg.execute()

        os.remove(video_path)
        os.remove(audio_path)
        
        self.count += 1
        return output_path, self.count

    # get info about video
    def getInfo(self):
        return self._getName(), self._getAuthor(), self._getLen(), self._getRes()

    # help for getting info...
    def _getName(self):
        return self.yt.title
    
    def _getAuthor(self):
        return self.yt.author
    
    def _getLen(self):
        len = formatTime(self.yt.length)

        return len

    def _getRes(self):
        arr = []

        for stream in self.yt.streams:
            if stream.resolution != None:
                before = str(stream.resolution).replace("p", "")
                after = int(before)
            if after in arr or stream.resolution == None: continue;
            else: arr.append(after)

        arr_copy = sorted(arr, reverse=True)
        return arr, arr_copy
    
