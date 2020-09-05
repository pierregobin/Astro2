
clean:
	rm *.bmp

gene:
	./generateimage.py -f simple -n 20 --drifth 2 
	./generateimage.py -f noisy01 -n 40 --drifth 2 --noise_mean 20  --noise_sigma 30

all: gene


