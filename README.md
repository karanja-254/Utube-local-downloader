# ⚠️ Disclaimer
**This tool is for educational purposes only.**
Please respect YouTube's Terms of Service. Only download content if you have permission from the creator or if your usage falls under Fair Use guidelines. The creator of this tool is not responsible for any misuse.

---

# 📹 Karanja's Ultimate YouTube Downloader & Compressor

A robust Python command-line tool that downloads, compresses, and trims videos. It includes a smart main menu, precision trimming tools, and the ability to compress both online links and local video files on your computer.

## 🚀 New Features
- **✂️ Precision Trimming:** Download only the part you need (e.g., from `1:00` to `2:30`) instead of the whole video.
- **📉 Smart Compression (CRF 28):** Reduce file size by up to 50% while keeping watchable quality.
- **📂 Local File Compressor:** Use a Windows popup to select videos already on your PC and squash them.
- **⏱️ Duration Analyzer:** Shows the exact length of the video before you download.
- **High Resolution Support:** Downloads 1080p/4K video with merged audio.

---

## 🛠️ Installation & Setup

### 1. Install Python
If you don't have Python installed, download it from [python.org](https://www.python.org/downloads/).
> **Important:** During installation, make sure to check the box that says **"Add Python to PATH"**.

### 2. Download this Code
1.  Click the green **Code** button at the top of this GitHub page.
2.  Select **Download ZIP**.
3.  Extract the folder to your Desktop.

### 3. Install FFmpeg (Crucial Step)
This tool requires **FFmpeg** for merging, trimming, and compressing. Choose the method that fits your skill level:

#### 🟢 Option A: Newbie Level (Easiest)
*Use this if you don't know what "System Environment Variables" are.*

1.  Download FFmpeg from this safe link: [ffmpeg-release-essentials.zip](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip)
2.  Unzip the downloaded file (Right-click > Extract All).
3.  Open the extracted folder until you find a folder named `bin`.
4.  Inside `bin`, find the file named `ffmpeg.exe`.
5.  **Copy** `ffmpeg.exe` and **Paste** it into the **SAME FOLDER** as `downloader.py`.
    * *Your folder should look like this:*
      ```text
      📁 Youtube_Downloader
       ├── downloader.py
       ├── README.md
       └── ffmpeg.exe
      ```

#### 🔴 Option B: Developer Level (Cleanest)
*Use this if you are comfortable editing System Paths.*

1.  Download and extract FFmpeg to a permanent location (e.g., `C:\ffmpeg`).
2.  Add `C:\ffmpeg\bin` to your Windows **System Path** Environment Variables.
3.  Verify installation by typing `ffmpeg -version` in a new terminal.
4.  You do *not* need to copy any files into the script folder.

### 4. Install the Python Library
1.  Open the folder containing the script.
2.  Type `cmd` in the folder's address bar and press **Enter**.
3.  Run this command:
    ```bash
    pip install yt-dlp
    ```

---

## ▶️ How to Use

1.  **Run the script:**
    ```bash
    python downloader.py
    ```

2.  **Choose a Mode from the Main Menu:**
    * **Option 1: Download Video (Standard)**
        * Paste the link.
        * Select Quality (e.g., 1080p).
        * **Sub-Option:** Choose **Full Video** OR **Trim Video**.
        * *If Trimming:* Enter Start Time (e.g., `1:15`) and End Time (e.g., `2:30`).

    * **Option 2: Compression Tools**
        * **From Link:** Downloads a YouTube video and immediately compresses it.
        * **From Local File:** Opens a Windows File Picker. Select any video on your PC, and it will create a smaller version (e.g., `video_compressed.mp4`).

3.  **Wait for the Magic:**
    * Downloads are saved in the same folder.
    * Compression takes a moment depending on your CPU speed.

## 🤝 Contributing
Feel free to fork this repository and submit pull requests.

## 📄 License
This project is open-source and available for personal use.