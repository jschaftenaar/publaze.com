from flask import Flask, render_template, send_from_directory, request, jsonify
from youtube_api import get_channel_videos, get_channel_playlists, get_channel_info, get_video_details, get_playlist_details, get_playlist_videos
import os
from dotenv import load_dotenv
from helpers import read_yaml_file, RegexConverter
import markdown

load_dotenv()
app = Flask(__name__)
app.url_map.converters['regex'] = RegexConverter
CHANNEL_ID=os.getenv('YOUTUBE_CHANNEL_ID')
script_dir = os.path.dirname(os.path.realpath(__file__))
configuration = read_yaml_file(os.path.join(f'{script_dir}', os.getenv('CONFIGURATION_FILE','configuration.yaml')))

@app.context_processor
def inject_videos_and_info():
    videos = get_channel_videos(CHANNEL_ID)
    channel_info = get_channel_info(CHANNEL_ID)
    playlists = get_channel_playlists(CHANNEL_ID)
    return {
        'videos': videos,
        'channel': channel_info,
        'playlists': playlists,
        'configuration': configuration
    }

@app.route('/')
def index():
    if video_id := configuration.get('lander', {}).get('video_id'):
        video_details = get_video_details(video_id)
        return render_template('index.html', video=video_details)
    return render_template('index.html')    

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/content/<markdown_file>')
def content(markdown_file):
    markdown_path=f'{script_dir}/content/{markdown_file}.md'
    if os.path.exists(markdown_path):
        with open(markdown_path, 'r', encoding='utf-8') as file:
            content = file.read()
        html_content = markdown.markdown(content)
        return render_template('content.html', content=html_content)
    return render_template('404.html'), 404

@app.route('/video/<video_id>.json')
@app.route('/video/<video_id>')
def video(video_id):
    video_details = get_video_details(video_id)
    if request.content_type == 'application/json' or request.path.endswith('json'):
        return jsonify(video_details)
    return render_template('video.html', video=video_details)

@app.route('/playlist/<playlist_id>.json')
@app.route('/playlist/<playlist_id>')
def playlist(playlist_id):
    playlist_details = get_playlist_details(playlist_id)
    playlist_videos = get_playlist_videos(playlist_id)
    if request.content_type == 'application/json' or request.path.endswith('json'):
        return jsonify({
            'playlist':playlist_details,
            'playlist_videos':playlist_videos
        })
    return render_template('playlist.html', playlist=playlist_details, playlist_videos=playlist_videos)

@app.route('/playlist/<playlist_id>/<video_id>.json')
@app.route('/playlist/<playlist_id>/<video_id>')
def playlist_video(playlist_id, video_id):
    playlist_details = get_playlist_details(playlist_id)
    video_details = get_video_details(video_id)
    if request.content_type == 'application/json' or request.path.endswith('json'):
        return jsonify({
            'playlist': playlist_details,
            'video': video_details
        })
    return render_template('playlistvideo.html', playlist=playlist_details, video=video_details)

@app.errorhandler(404)
def page_not_found(_error):
    return render_template('404.html'), 404 

@app.route('/<regex("(videos|playlists|about|discord)"):slug>')
def template(slug):
    return render_template(f'{slug}.html')

@app.route('/<regex("(videos|playlists|channel|configuration)"):slug>.json')
def json_context(slug):
    return jsonify(inject_videos_and_info()[slug])


if __name__ == "__main__":
    app.run()
