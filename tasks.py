import youtube_dl
from os import environ as env
from worker import celery

download_dir = env.get("DOWNLOAD_DIR", "/download/").rstrip("/")
out_tmpl = "%(title)s/%(title)s__-__%(id)s_%(uploader)s.%(ext)s"
ytdl_opts = {
    'ignoreerrors': True,
    'writesubtitles': True,
    'writeautomaticsub': True,
    'subtitleslang': "en",
    'download_archive': f"{download_dir}/ytdl-archive",
    'restrictfilenames': True,
    'writedescription': True,
    'writeinfojson': True,
    'writeannotations': True,
    'writethumbnail': True,
    'geo_bypass': True,
    'outtmpl': f"{download_dir}/{out_tmpl}"
}


@celery.task(name='tasks.download')
def download(video_url: str) -> str:
    with youtube_dl.YoutubeDL(ytdl_opts) as ydl:
        ydl.download([video_url])

    return "ok"
