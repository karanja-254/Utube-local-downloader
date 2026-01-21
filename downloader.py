import yt_dlp
import sys
import os
import subprocess
import tkinter as tk
from tkinter import filedialog
import math

# --- HELPER FUNCTIONS ---

def get_size_mb(fmt, duration):
    """Calculates estimated file size for YouTube formats."""
    if fmt.get('filesize'):
        return fmt['filesize'] / (1024 * 1024)
    if fmt.get('filesize_approx'):
        return fmt['filesize_approx'] / (1024 * 1024)
    if fmt.get('tbr') and duration:
        size_bytes = (fmt['tbr'] * 1000 / 8) * duration
        return size_bytes / (1024 * 1024)
    return 0

def format_seconds(seconds):
    """Converts seconds (e.g., 312) to MM:SS format (e.g., 05:12)."""
    if not seconds: return "Unknown"
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    if h > 0:
        return f"{h}:{m:02d}:{s:02d}"
    return f"{m}:{s:02d}"

def timestamp_to_seconds(ts):
    """Converts MM:SS or HH:MM:SS string to integer seconds."""
    try:
        parts = list(map(int, ts.strip().split(':')))
        if len(parts) == 3: # HH:MM:SS
            return parts[0]*3600 + parts[1]*60 + parts[2]
        if len(parts) == 2: # MM:SS
            return parts[0]*60 + parts[1]
        if len(parts) == 1: # SS
            return parts[0]
        return 0
    except:
        return None

def compress_local_file():
    """Opens a Windows file picker and compresses the selected video."""
    print("\n📂 Opening File Picker... (Check your taskbar if it doesn't pop up)")
    
    root = tk.Tk()
    root.withdraw()
    
    file_path = filedialog.askopenfilename(
        title="Select a Video to Compress",
        filetypes=[("Video Files", "*.mp4 *.mkv *.mov *.avi *.flv *.webm")]
    )
    
    if not file_path:
        print("❌ No file selected. Returning to menu.")
        return

    print(f"✅ Selected: {file_path}")
    base, ext = os.path.splitext(file_path)
    output_path = f"{base}_compressed{ext}"
    
    print("⚡ Compressing... (This uses your PC's CPU)")
    
    cmd = [
        'ffmpeg', '-i', file_path,
        '-c:v', 'libx264', '-crf', '28', '-preset', 'fast',
        '-c:a', 'aac', '-b:a', '128k',
        output_path
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"\n✅ Done! Saved as: {output_path}")
    except Exception as e:
        print(f"\n❌ Compression Failed: {e}")

def download_video(url, force_compress=False):
    print("\n------------------------------------------------")
    print("🔍 Analyzing video metadata... please wait.")
    
    ydl_opts_info = {'quiet': True, 'no_warnings': True}
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts_info) as ydl:
            info = ydl.extract_info(url, download=False)
            title = info.get('title', 'Video')
            duration = info.get('duration', 0)
            duration_str = format_seconds(duration)
            
            # 1. SHOW VIDEO INFO
            print(f"\n🎬 Title: {title}")
            print(f"⏱️ Duration: {duration_str}")
            
            # 2. SHOW QUALITY OPTIONS
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
            print("\nAvailable Qualities:")
            options_map = {} 
            for i, res in enumerate(sorted_res):
                size = resolutions[res]
                label = f"{res}p (~{size:.1f} MB)" if size > 0 else f"{res}p"
                print(f"{i+1}. {label}")
                options_map[i+1] = res
            
            q_choice = input("\nChoose Quality (Number): ")
            if not q_choice.strip(): return
            selected_height = options_map.get(int(q_choice))
            if not selected_height:
                print("Invalid selection.")
                return

            # 3. ASK: FULL OR TRIMMED?
            print("\n------------------------------------------------")
            print(f"video Length: {duration_str}")
            print("1. Download Full Video")
            print("2. Trim Video (Cut a specific part)")
            mode_choice = input(">> Select Option (1 or 2): ").strip()
            
            start_time = None
            end_time = None
            
            if mode_choice == '2':
                print("\n✂️  Trim Mode")
                print("   Format: MM:SS (e.g., 1:30) or HH:MM:SS")
                s_input = input("   Start Time: ")
                e_input = input("   End Time:   ")
                
                start_time = timestamp_to_seconds(s_input)
                end_time = timestamp_to_seconds(e_input)
                
                if start_time is None or end_time is None:
                    print("❌ Invalid time format. Downloading full video instead.")
                    start_time = None
                    end_time = None
                else:
                    print(f"✅ Cutting from {s_input} to {e_input}")

    except Exception as e:
        print(f"Error fetching info: {e}")
        return

    # --- DOWNLOAD CONFIGURATION ---
    print(f"\n⬇️  Processing...")
    
    format_string = f'bestvideo[height={selected_height}]+bestaudio/best[height={selected_height}]'
    
    ydl_opts = {
        'format': format_string,
        'outtmpl': '%(title)s_%(height)sp.%(ext)s', 
        'merge_output_format': 'mp4',
        'quiet': False,
        # 'cookies_from_browser': 'chrome', # Uncomment if using local browser cookies
    }

    # APPLY TRIM SETTINGS
    if start_time is not None and end_time is not None:
        # This tells yt-dlp to download only the specific range
        ydl_opts['download_ranges'] = lambda info, ydl: [{'start_time': start_time, 'end_time': end_time}]
        # Force keyframes for accurate cutting (optional but recommended)
        ydl_opts['force_keyframes_at_cuts'] = True

    # APPLY COMPRESSION SETTINGS (From Main Menu option)
    if force_compress:
        print("⚡ Compression Enabled (CRF 28).")
        ydl_opts['postprocessor_args'] = {
            'merger': [
                '-c:v', 'libx264', '-crf', '28', '-preset', 'fast',
                '-c:a', 'aac', '-b:a', '128k'
            ]
        }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("\n✅ Process Complete!")
    except Exception as e:
        print(f"Download error: {e}")

# --- MAIN MENU SYSTEM ---

def main_menu():
    print("\n========================================")
    print("   🎥  ULTIMATE DOWNLOADER & TRIMMER   ")
    print("========================================")
    print("1. Download Video (Full or Trim)")
    print("2. Compression Tools 📉")
    print("3. Exit")
    
    choice = input("\n>> Select an Option (1-3): ").strip()
    
    if choice == '1':
        # Download (Sub-options happen inside the function after analysis)
        link = input("\n🔗 Paste Link: ")
        if link: download_video(link, force_compress=False)
        
    elif choice == '2':
        # Compression Menu
        print("\n--- 📉 Compression Menu ---")
        print("1. Download from Link & Compress")
        print("2. Compress a Local File")
        print("3. Back")
        
        sub_choice = input("\n>> Select: ").strip()
        
        if sub_choice == '1':
            link = input("\n🔗 Paste Link: ")
            if link: download_video(link, force_compress=True)
            
        elif sub_choice == '2':
            compress_local_file()
            
    elif choice == '3':
        print("Goodbye!")
        sys.exit()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    while True:
        try:
            main_menu()
            input("\nPress Enter to continue...")
        except KeyboardInterrupt:
            sys.exit()