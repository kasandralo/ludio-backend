import yt_dlp
import os

def search_youtube_url(query: str) -> str:
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'noplaylist': True,
        'format': 'bestaudio/best',
        'default_search': 'ytsearch1',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(query, download=False)
        return info['entries'][0]['webpage_url']

def download_audio(youtube_url: str):
    output_dir = "static"
    os.makedirs(output_dir, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_dir}/%(id)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=True)
        filename = f"{info['id']}.mp3"

    return {"filename": filename, "title": info.get("title", "")}
