import MFCC
import os
name_list = ["Uesaka_Sumire","Komatsu_Mikako","Okubo_Rumi","Takamori_Natsumi","Mikami_Shiori"]

for g in name_list:
	files = os.listdir("./" + g + "/")
	for f in files:
		MFCC.create_ceps("./" + g + "/" + f)
