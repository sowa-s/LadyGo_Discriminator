#!/bin/bash
array=("Uesaka_Sumire_Anime/" "Komatsu_Mikako_Anime/" "Okubo_Rumi_Anime/" "Takamori_Natsumi_Anime/" "Mikami_Shiori_Anime/")
for dir in ${array[@]}
do
	cd ${dir}
	rm .DS_Store
	rm -rf *.npy
	cd ..
done
