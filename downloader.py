import yt_dlp
import sys

def get_size_mb(fmt, duration):
    if fmt.get('filesize'):
        return fmt['filesize'] / (1024 * 1024)
    if fmt.get('filesize_approx'):
        return fmt['filesize_approx'] / (1024 * 1024)
    if fmt.get('tbr') and duration:
        size_bytes = (fmt['tbr'] * 1000 / 8) * duration
        return size_bytes / (1024 * 1024)
    return 0

def download_video(url):
    print("\n------------------------------------------------")
    print("Analyzing video... please wait.")
    
    ydl_opts_info = {'quiet': True, 'no_warnings': True}
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts_info) as ydl:
            info = ydl.extract_info(url, download=False)
            title = info.get('title', 'Video')
            duration = info.get('duration', 0)
            
            best_audio_size = 0
            audio_formats = [f for f in info['formats'] if f.get('vcodec') == 'none' and f.get('acodec') != 'none']
            if audio_formats:
                best_audio = max(audio_formats, key=lambda x: x.get('abr', 0) or 0)
                best_audio_size = get_size_mb(best_audio, duration)

            resolutions = {}
            for f in info['formats']:
                if f.get('vcodec') != 'none' and f.get('height'):
                    height = f['height']
                    vid_size = get_size_mb(f, duration)
                    total_estimated = vid_size + best_audio_size
                    if height not in resolutions or total_estimated > resolutions[height]:
                        resolutions[height] = total_estimated
            
            sorted_res = sorted(resolutions.keys(), reverse=True)
            
            print(f"Title: {title}")
            print("Available Qualities:")
            
            options_map = {} 
            for i, res in enumerate(sorted_res):
                size = resolutions[res]
                label = f"{res}p (Max ~{size:.1f} MB)" if size > 0 else f"{res}p"
                print(f"{i+1}. {label}")
                options_map[i+1] = res
            
            choice = input("\nChoose a number (or press Enter to cancel this download): ")
            if not choice.strip():
                print("Download cancelled.")
                return

            try:
                selected_height = options_map[int(choice)]
            except (ValueError, KeyError):
                print("Invalid selection.")
                return

    except Exception as e:
        print(f"Error fetching info: {e}")
        return

    print(f"\nDownloading {selected_height}p version...")
    format_string = f'bestvideo[height={selected_height}]+bestaudio/best[height={selected_height}]'
    
    ydl_opts_download = {
        'format': format_string,
        'outtmpl': '%(title)s_%(height)sp.%(ext)s', 
        'merge_output_format': 'mp4',
        'quiet': False, # Show progress bar
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts_download) as ydl:
            ydl.download([url])
            print("\n Download complete!")
    except Exception as e:
        print(f"Download error: {e}")

if __name__ == "__main__":
    print("🎥 Your YouTube Downloader is Ready!")
    print("Press Ctrl+C to stop the program at any time.\n")
    
    while True:
        try:
            video_url = input(">> Enter YouTube URL (or 'q' to quit): ")
            
            # Allow user to type 'q' or 'exit' to leave gracefully
            if video_url.lower() in ['q', 'exit', 'quit']:
                print("Goodbye!")
                break
                
            if not video_url.strip():
                continue
                
            download_video(video_url)
            print("\nReady for the next one!")
            
        except KeyboardInterrupt:
            print("\n\nStopping program... Goodbye!")

            sys.exit()

