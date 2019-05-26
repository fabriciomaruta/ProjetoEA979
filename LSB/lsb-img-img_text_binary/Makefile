encode-img:
	python LSBSteg.py encode -i imgs-in/img.pnm -o imgs-out/new_img.pnm -f imgs-in/secret-img.pnm

decode-img:
	python LSBSteg.py decode -i imgs-out/new_img.pnm -o img.pnm

encode-txt:
	python LSBSteg.py encode -i imgs-in/img.pnm -o imgs-out/new_img.pnm -f texts-in/message.txt

decode-txt:
	python LSBSteg.py decode -i imgs-out/new_img.pnm -o texts-out/secret-message.txt