#!/bin/bash

 # afconvert -f WAVE -d LEI16 classical.00008.au
array=("Uesaka_Sumire_Anime/*" "Komatsu_Mikako_Anime/*" "Okubo_Rumi_Anime/*" "Takamori_Natsumi_Anime/*" "Mikami_Shiori_Anime/*")
for files in ${array[@]}
do
	afconvert -f WAVE -d LEI16 ${files}
	rm ${files}
done



