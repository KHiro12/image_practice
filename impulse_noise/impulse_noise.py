import cv2
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def impulsenoise(img, low, high):
	noise = np.random.randint(0, 255, np.shape(img))
	imgnoi = img
	imgnoi[noise>high] = 255
	imgnoi[noise<low] = 0
	# ノイズ付与画像
	file_name = f'output/{str(1).zfill(2)}_impulsenoise_{str(low)}_{str(high)}.jpg'
	cv2.imwrite(file_name, imgnoi)
	# ノイズ画像
	file_name = f'output/{str(1).zfill(2)}_noise_{str(low)}_{str(high)}.jpg'
	cv2.imwrite(file_name, np.floor(noise))


if __name__ == "__main__":
	# 画像読み込み
	img = cv2.imread('C:/git/image_practice/sampe_image/car-race-gbc33400b0_1920.jpg')
	cv2.imwrite('output/00_base.jpg', img)

	# ガウシアンノイズ
	low = int(input("下限："))
	high = int(input("上限："))
	impulsenoise(img, low, high)