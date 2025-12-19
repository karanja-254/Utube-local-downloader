⚠️ Disclaimer
This tool is for educational purposes only. Please respect YouTube's Terms of Service and only download content if you have permission or if it falls under Fair Use guidelines.

# 📹 High-Quality Python YouTube Downloader

A robust command-line tool that downloads YouTube videos in the best available quality (1080p, 4K, etc.) by automatically merging video and audio streams. It also estimates file sizes before downloading to help you manage data usage.

## 🚀 Features
- **High Resolution Support:** Downloads video and audio separately and merges them for maximum quality (bypassing YouTube's separate stream limitations).
- **Quality Selection:** Lists all available resolutions (1080p, 720p, 480p) with **estimated file sizes**.
- **Audio/Video Merging:** Uses `FFmpeg` to ensure the final output is a clean, playable `.mp4` file.
- **Smart Formatting:** Automatically names files with the video title and resolution (e.g., `Tutorial_1080p.mp4`).

## 🛠️ Prerequisites
Before running this tool, ensure you have the following installed:

1.  **Python 3.x**
2.  **FFmpeg** (Required for merging audio/video)
    - *Windows:* Download from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/), extract, and add the `bin` folder to your System PATH (or place `ffmpeg.exe` in the same folder as the script).
    - *Linux:* `sudo apt install ffmpeg`
    - *Mac:* `brew install ffmpeg`

## 📦 Installation

1.  **Clone the repository** (or download the files):
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Install the required Python library:**
    ```bash
    pip install yt-dlp
    ```

## ▶️ How to Use

1.  Open your terminal or command prompt in the project folder.
2.  Run the script:
    ```bash
    python downloader.py
    ```
3.  **Paste the YouTube URL** when prompted.
4.  **Select your desired quality** from the list (e.g., Type `1` for 1080p).
5.  Wait for the "Download complete!" message. The video will be saved in the same folder.

## 📝 Example Output
```text
Enter YouTube URL: [https://youtu.be/example](https://youtu.be/example)
Analyzing video... please wait.

Title: Learn Python in 10 Minutes
Available Qualities:
1. 1080p (~150.2 MB)
2. 720p (~85.5 MB)
3. 480p (~40.1 MB)

Choose a number: 1
Downloading 1080p version...
Download complete!