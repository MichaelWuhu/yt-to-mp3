from yt_dlp import YoutubeDL

def get_video_urls_from_playlist(playlist_url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': 'in_playlist',
        'skip_download': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(playlist_url, download=False)
        entries = info_dict.get('entries', [])
        video_urls = [f"https://www.youtube.com/watch?v={entry['id']}" for entry in entries]
    return video_urls

def download_video_as_mp3(url, output_path='.'):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False,
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_playlist_as_mp3(playlist_url, output_path='./downloads'):
    print("Fetching video URLs from playlist...")
    video_urls = get_video_urls_from_playlist(playlist_url)
    print(f"Found {len(video_urls)} videos.")

    for i, video_url in enumerate(video_urls, 1):
        print(f"\n[{i}/{len(video_urls)}] Downloading: {video_url}")
        download_video_as_mp3(video_url, output_path)

if __name__ == "__main__":
    playlist_url = input("Enter the YouTube playlist URL: ").strip()
    download_playlist_as_mp3(playlist_url)
