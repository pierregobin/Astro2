Image stacking experiments


./generateimage.py -f simple -n 20 --drifth 2 --noise_mean 20  --noise_sigma 30
./generateimage.py -f noisy03 -n 200 --drifth 2 --noise_mean 40  --noise_sigma 60
./imagestack.py --origin noisy03-00006.bmp --image "noisy03-*.bmp" --output=noisy03simple.bmp  --threshold=0.2




