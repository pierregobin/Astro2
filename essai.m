image = eye(32);
for t=1:2
	s = sprintf("octave-%03d.bmp",t);
	m = [0:31]+t*[0:31]';
	p = exp(-2*i*pi/32 * m);
	im = ifft2(fft2(image) .* p)
	imwrite(im,s)
endfor

