import pafy

url = input("Enter the complete URL of the video") # https://youtu.be/gTjXTRz4dDw

# create an object using pafy.new()
video = pafy.new(url)

print(video.title) #to get the title of the video
print(video.author) #to get the author of the video 
print(video.viewcount) #to get the number of views
print(video.length) #to get the length of video

streams = video.streams  #this will return A list of regular streams (streams containing both audio and video)

for i in streams:
    print (i) #print all the streams available for that video link

best = video.getbest() #this method returns the best resolution

print(best)
best.download()

print(" Video downloaded successfully")
