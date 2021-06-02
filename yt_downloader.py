from pytube import YouTube
video_url = input("inserisci qui l'url del video che desideri scaricare : ") # YouTube video URL
youtube = YouTube(video_url)
video = youtube.streams.first()
video.download("/home/salvatore/Scrivania")
