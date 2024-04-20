from flask import Flask, render_template
from youtube_api import get_channel_videos, get_channel_playlists, get_channel_info, get_video_details
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

CHANNEL_ID=os.getenv('YOUTUBE_CHANNEL_ID')

@app.route('/')
def index():
    videos = get_channel_videos(CHANNEL_ID)
    channel_info = get_channel_info(CHANNEL_ID)
    return render_template('videos.html', videos=videos, channel=channel_info)

@app.route('/playlists')
def playlists():
    playlists = get_channel_playlists(CHANNEL_ID)
    channel_info = get_channel_info(CHANNEL_ID)
    return render_template('playlists.html', playlists=playlists, channel=channel_info)

@app.route('/about')
def about():
    channel_info = get_channel_info(CHANNEL_ID)
    return render_template('about.html', channel=channel_info)

@app.route('/discord')
def discord():
    channel_info = get_channel_info(CHANNEL_ID)
    return render_template('discord.html', channel=channel_info)

@app.route('/video/<video_id>')
def video(video_id):
    video_details = get_video_details(video_id)
    channel_info = get_channel_info(CHANNEL_ID)    
    return render_template('video.html', video=video_details, channel=channel_info)

@app.errorhandler(404)
def page_not_found():
    channel_info = get_channel_info(CHANNEL_ID)    
    return render_template('404.html', channel=channel_info), 404


if __name__ == "__main__":
    app.run(debug=False)
