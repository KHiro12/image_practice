import cv2
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def gausiannoise(img, sig, ave, file_no):
	# np.random.normal(平均, 標準偏差, サイズ)
	noise = np.random.normal(ave, sig, np.shape(img))
	imgnoi = img + np.floor(noise)
	imgnoi[imgnoi>255] = 255
	imgnoi[imgnoi<0] = 0
	# ノイズ付与画像
	file_name = f'output/{str(file_no).zfill(2)}_gausunoise_{str(sig)}_{str(ave)}.jpg'
	cv2.imwrite(file_name, imgnoi)
	# ノイズ画像
	file_name = f'output/{str(file_no).zfill(2)}_noise_{str(sig)}_{str(ave)}.jpg'
	cv2.imwrite(file_name, np.floor(noise))


if __name__ == "__main__":
	# 画像読み込み
	img = cv2.imread('C:/git/image_practice/sampe_image/car-race-gbc33400b0_1920.jpg')
	cv2.imwrite('output/00_base.jpg', img)

	# ガウシアンノイズ
	for n in range(1, 10):
		# 標準偏差
		sig = 20 * n
		ave = 0
		gausiannoise(img, sig, ave, 1)

		sig = 20
		ave = 0 + n * 10
		gausiannoise(img, sig, ave, 2)

		sig = 20
		ave = 0 - n * 10
		gausiannoise(img, sig, ave, 2)