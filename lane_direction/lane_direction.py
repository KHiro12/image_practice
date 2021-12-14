import cv2
import numpy as np


def lane_edge_horizon(img, threshold):
	edge_img = img.copy()

	for j in range(0, img.shape[0]):
		edge_img[j][0] = 0

		for i in range(1, img.shape[1]):
			edge_val = abs(int(img[j][i]) - int(img[j][i-1]))

			if edge_val < threshold:
				edge_img[j][i] = 255
			else:
				edge_img[j][i] = 0

	cv2.imwrite('output/02_edge_image.jpg', edge_img)


def lane_edge_vartical(img, threshold):
	edge_img = img.copy()

	for j in range(1, img.shape[0]):
		edge_img[j][0] = 0

		for i in range(0, img.shape[1]):
			edge_val = abs(int(img[j][i]) - int(img[j-1][i]))

			if edge_val < threshold:
				edge_img[j][i] = 255
			else:
				edge_img[j][i] = 0

	cv2.imwrite('output/03_edge_image.jpg', edge_img)


if __name__ == "__main__":
	img = cv2.imread('C:\git\image_practice\sampe_image\photo0000-0732.jpg')
	cv2.imwrite('output/00_base.jpg', img)

	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	cv2.imwrite('output/01_gray.jpg', img_gray)

	lane_edge_horizon(img_gray, 50)
	lane_edge_vartical(img_gray, 50)
