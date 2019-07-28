import cv2
import os

class Video(object):
	def __init__(self, vid_dir):
		self.gray_frames = []
		self.frames = []
		self.cap = cv2.VideoCapture(vid_dir)
		if not self.cap.isOpened():
			raise Exception("The video is not properly opened"%vid_dir)
			return 
		else:
			success = True
			while success:
				cur_frame = self.cap.read()[1]
				self.gray_frames.append(self.rgb2gray())
				self.frames.append(cur_frame)

	def rgb2gray(self):
		r, g, b = self.frames[:,:,0], self.frames[:,:,1], self.frames[:,:,2]
		gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
		return gray

	# Only support grayscale images
	def get_average_illumination(self, frame):
		sum_val = 0
		for row in frame:
			sum_val += (sum(row) / len(row))
		sum_val /= len(frame)
		return sum_val

	def get_background(self):
		background = []
		prev_frame = frames[0]
		for frame in frames:
			if frames.index(frame) == 0:
				continue
			else:
				pass 
if __name__ == "__main__":
	v = Video("./spider.mp4")
	print(v.cap.read())
	print(v.frames[600][1000])
	