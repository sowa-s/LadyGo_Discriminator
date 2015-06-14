import FFT
import os
name_list = ["Uesaka_Sumire_Anime","Komatsu_Mikako_Anime","Okubo_Rumi_Anime","Takamori_Natsumi_Anime","Mikami_Shiori_Anime"]

for g in name_list:
	files = os.listdir("./" + g + "/")
	for f in files:
		FFT.create_fft("./" + g + "/" + f)
