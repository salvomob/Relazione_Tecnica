from pytube import YouTube
path = "/home/salvatore/Scrivania" #in here specify the path in which you want to download the video 
url = input("inserisci ulr del video da scaricare : ")
my_video = YouTube(url)
print("nome video in fase di download:")
print(my_video.title)
print("in fase di downolad :), aspetta ancora un po'! ")
my_video = my_video.streams.get_highest_resolution()
my_video.download(path)
print("Video scaricato in : " + path)
