from pytube import YouTube

# Function to download video in 1080p with audio and video
def download_video(url):
    try:
        # Create a YouTube object
        youtube = YouTube(url)

        # Filter the streams to get the ones with both audio and video
        streams = youtube.streams.filter(progressive=True,  resolution='720p')
    
        # Get the first stream (highest resolution with audio)
        stream = streams.first()
        
        if stream:
            # Download the video
            print(f"Downloading: {youtube.title}")
            stream.download()
            print("Download completed!")
        else:
            print("No suitable streams found for download.")

    except Exception as e:
        print(f"Error: {str(e)}")

# URL of the video you want to download
video_url =  input("Enter URL: ")

# Function call
download_video(video_url)
