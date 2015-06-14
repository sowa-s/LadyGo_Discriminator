#!/bin/bash
array=("Uesaka_Sumire/" "Komatsu_Mikako/" "Okubo_Rumi/" "Takamori_Natsumi/" "Mikami_Shiori/")
for dir in ${array[@]}
do
	cd ${dir}
	rm .DS_Store
	rm -rf *.npy
	cd ..
done
