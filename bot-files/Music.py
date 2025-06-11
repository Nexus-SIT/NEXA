from ytmusicapi import YTMusic
import vlc
import time
import subprocess

def get_audio_url_with_yt_dlp(video_url):
    """
    Fetches the best audio stream URL using yt-dlp.
    """
    try:
        yt_dlp_executable = r'.\Music\yt-dlp.exe'

        command = [
            yt_dlp_executable,
            '-f', 'bestaudio', 
            '-g',             
            video_url
        ]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            audio_url = stdout.decode('utf-8').strip()
            return audio_url.split('\n')[0]
        else:
            print(f"yt-dlp error: {stderr.decode('utf-8')}")
            return None
    except FileNotFoundError:
        print("yt-dlp not found. Please ensure it's installed and in your PATH.")
        return None
    except Exception as e:
        print(f"An error occurred while fetching audio URL with yt-dlp: {e}")
        return None

def search_and_play(song_name):
    """
    Searches for a song on YouTube Music, retrieves its audio stream
    using yt-dlp, and plays it using VLC.
    """
    try:
        ytmusic = YTMusic()
        print(f"Searching for: {song_name}...")
        results = ytmusic.search(song_name, filter='songs')

        if not results:
            print("No song found.")
            return

        song = results[0]
        video_id = song['videoId']
        artist_name = song['artists'][0]['name'] if song.get('artists') and song['artists'] else "Unknown Artist"
        title = f"{song['title']} - {artist_name}"
        
        print(f"Found: {title}")
        print(f"Video ID: {video_id}")

        youtube_url = f"https://www.youtube.com/watch?v={video_id}"
        
        print("Fetching audio stream using yt-dlp...")
        audio_url = get_audio_url_with_yt_dlp(youtube_url)

        if not audio_url:
            print("No audio stream URL found using yt-dlp.")
            return

        print(f"Audio URL: {audio_url}")

        instance = vlc.Instance()
        if not instance:
            print("Could not create VLC instance.")
            return
            
        player = instance.media_player_new()
        if not player:
            print("Could not create VLC media player.")
            return

        media = instance.media_new(audio_url)
        if not media:
            print("Could not create VLC media.")
            return
            
        player.set_media(media)
        player.play()
        print(f"Playing: {title}")

        time.sleep(5) 

        while player.is_playing() or player.get_state() == vlc.State.Opening or player.get_state() == vlc.State.Buffering:
            time.sleep(1)
        
        print("Playback finished.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    search_and_play("Steal My girl by Imagine Dragons")
