Matt Stevenson
HW 3: Tuner

This was a challenging assignment, but I did find a great source to follow as a guide. For the wavfile part, I create a window, read in the wav data, and truncate the wav data to be the same length as my window. With that, I then multiply my window with my wav data and feed that to numpy's fft function. 

If the wav file data is already shorter than my window, I create a numpy array of zeros and write all of the wav data to the new array starting from the beginning. 

Finally, I find the largest bin from the resulting fft, get its absolute value, and multiply it by my frequency step (samples * frames per fft). This results in the dominate frequency of the wav clip.

For the streaming part, I do the same as above except I read from the audio buffer in chunks of 8192 samples; this is then processed the same way as my wav data from above. The buffer array is created to be the same size as the window to enable multiplcation, but only the first 8192 samples are written into the buffer array at a time. 

