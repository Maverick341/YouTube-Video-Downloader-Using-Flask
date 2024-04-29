from flask import Flask, render_template, request, jsonify
from pytube import YouTube


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

DOWNLOAD_DIR = "E:\Downloads"

@app.route('/download', methods=['POST'])
def download():
    video_url = request.form['video_url']
    try:
        yt = YouTube(video_url)
        stream = yt.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()
        filename = stream.default_filename
        download_path = os.path.join(DOWNLOAD_DIR, filename)
        stream.download(output_path=DOWNLOAD_DIR)
        message = f"Video downloaded successfully! Check '{filename}' in the '{DOWNLOAD_DIR}' directory."
    except Exception as e:
        message = f"Error: {str(e)}"
    return jsonify({'message': message})

if __name__ == '__main__':
    import os
    import webbrowser
    import threading

    def open_browser():
        webbrowser.open('http://localhost:5000')

    if 'WERKZEUG_RUN_MAIN' not in os.environ:
        # Start the Flask development server
        threading.Timer(1, open_browser).start()

    app.run(debug=True)
