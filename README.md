# ML-DL-Projects

Genre Classifier

In this project I have scrapped data off the Billboard music charts using a library called billboard, specifically designed for this purpose.
I extracted the top songs in each genre from Billboard charts.
Next I stored these song names and artists for fetching lyrics.
I used musixmatch to get song lyrics from the info I had extracted.
I have performed text processing to prepare the lyrics for the training and testing datasets.
I implemented the use of a Naive Bayes Classifier to identify the genre of the song from the lyrics provided.
To feed into the classifier, I had to create tuples with lyrics and the associated genre.
The classifier was trained on several genre's and at the end I could input lyrics of a song and let the classifier predict it's genre with decent accuracy.


Edge Detection

It takes an input image and converts it into an array.
It then uses a matrix (kernel) that is multiplied across the array that represents the image (convolve2d).
This kernel highlights the edges of the image.
The image has been greyscaled and grad biases have been added to amplify the visibility of the edges.
