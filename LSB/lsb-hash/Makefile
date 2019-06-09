encode-img:
	python steganography_hash.py merge --img1=../imgs/imgs-cover/cover_img.png --img2=../imgs/imgs-secret/secret_img.png --output=../imgs/imgs-steg/steg_img.png

decode-img:
	python steganography_hash.py unmerge --img=../imgs/imgs-steg/steg_img.png --output=../imgs/imgs-un/un_img.png

display-steg:
	display ../imgs/imgs-steg/steg_img.png

display-un:
	display ../imgs/imgs-un/un_img.png