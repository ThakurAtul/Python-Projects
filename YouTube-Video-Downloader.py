import pafy

url = input("Enter the complete URL of the video")

video = pafy.new(url)

print(video.title) #to get the title of the video
print(video.author) #to get the author of the video 
print(video.viewcount) #to get the number of views
print(video.length) #to get the length of video

streams = video.streams

for i in streams:
    print (i)

best = video.getbest()

print(best)
best.download()

print(" Video downloaded successfully")
