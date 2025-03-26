from fastapi import APIRouter, Request
from app.services.youtube_service import download_audio, search_youtube_url
from app.services.spotify_service import get_track_info

router = APIRouter()

@router.post("/play")
async def play_audio(request: Request):
    # request.body에 JSON 데이터가 들어있는지 확인
    try:
        data = await request.json()
    except Exception:
        return {"error": "Invalid JSON in request body"}

    youtube_url = data.get("youtube_url")
    query = data.get("query")
    track_id = data.get("track_id")

    # 1순위: track_id → Spotify → query
    if track_id:
        track = get_track_info(track_id)
        query = f"{track['artist']} - {track['title']}"

    # 2순위: query → YouTube
    if query and not youtube_url:
        youtube_url = search_youtube_url(query)

    if not youtube_url:
        return {"error": "No valid input provided."}

    file_info = download_audio(youtube_url)

    return {
        "stream_url": f"/stream/{file_info['filename']}",
        "title": file_info["title"]
    }


@router.get("/stream/{filename}")
async def stream_audio(filename: str):
    from fastapi.responses import FileResponse
    return FileResponse(f"static/{filename}", media_type="audio/mpeg")
