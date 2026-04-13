
import os
import subprocess

def download_video(url, path="downloads/"):
    os.makedirs(path, exist_ok=True)  

    title_cmd = f'yt-dlp --get-title {url}'    # to get video title using yt-dlp
    title = os.popen(title_cmd).read().strip()
    
    safe_title = "".join(c for c in title if c.isalnum() or c in " -_").rstrip()   #cleaning of illegal characters for filename 

    video_file = os.path.join(path, f"{safe_title}_video.mp4")
    audio_file = os.path.join(path, f"{safe_title}_audio.m4a")
    final_file = os.path.join(path, f"{safe_title}.mp4")

    os.system(f'yt-dlp -f bestvideo -o "{video_file}" {url}')  # for video the only

    os.system(f'yt-dlp -f bestaudio -o "{audio_file}" {url}')  #for audio the only

    subprocess.run([
        "ffmpeg", "-i", video_file, "-i", audio_file,          #for the  both audio and videos
        "-c:v", "copy", "-c:a", "aac", "-strict", "experimental",
        final_file
    ])

    print(f"\n Download complete: {final_file}")


if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=uXRaGStWd7s&list=RDuXRaGStWd7s&start_radio=1"
    download_video(url)







   

                 
