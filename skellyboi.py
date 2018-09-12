#!/usr/bin/env python
from threading import Lock
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, \
	close_room, rooms, disconnect
import pyaudio, os, math, audioop, time
from collections import deque

""" THRESHOLD: Modify this to adjust minimum level to initiate animation """
THRESHOLD = 3000

""" MIN_ANIMATION: Minimum seconds for animation to run """
MIN_ANIMATION = 0.5

""" Probably don't change any of this, though """
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
SILENCE_LIMIT = 1 
RECORD_SECONDS = 1
async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

def background_thread():
	p = pyaudio.PyAudio()
	stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
	cur_data = ''
	rel = RATE/CHUNK
	slid_win = deque(maxlen=SILENCE_LIMIT * rel)
	avg_count = 4
	ts = time.time()
	while True:
		cur_data = stream.read(CHUNK)
		slid_win.append(math.sqrt(abs(audioop.avg(cur_data, avg_count))))
		s = sum([round(x) for x in slid_win])
		status = None
		nstatus = 1 if s>THRESHOLD else 0
		if nstatus!=status and (nstatus==1 or time.time() - ts >= MIN_ANIMATION):
			status=nstatus
			ts = time.time()
			socketio.emit('response', {'data': status==1, 'level': s, 'count': status}, namespace='/skelly')
	stream.close()
	p.terminate()
		
@app.route('/')
def index():
	return render_template('index.html', async_mode=socketio.async_mode)

@socketio.on('connect', namespace='/skelly')
def client_connect():
	print("Connected!")
	global thread
	with thread_lock:
		if thread is None:
			thread = socketio.start_background_task(target=background_thread)
	emit('my_response', {'data': 'Connected', 'count': 0})

@socketio.on('disconnect', namespace='/skelly')
def client_disconnect():
	print('Client disconnected', request.sid)

if __name__ == '__main__':
	socketio.run(app) #, debug=True