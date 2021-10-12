# Summary

This is a complete guide for the Code Implementation of our Project Report.

It is necessary to understand the scheme of advanced methods for high-quality face swapping and generate enough and representative face swapping images to train DeepFake detection algorithms. 

## Code Implementation


This report is to how to train a swap-face algorithm. 

The submission files are the three Ipython Notebooks: 

	1. [Training data generation.ipynb](https://github.com/somya51p/Face_swap/blob/main/Face_swap/Training%20data%20generation.ipynb)
	2. [Train.ipynb](https://github.com/somya51p/Face_swap/blob/main/Face_swap/train.ipynb)
	3. [Prediction.ipynb](https://github.com/somya51p/Face_swap/blob/main/Face_swap/Prediction.ipynb)

## What is DeepFake??

Deepfake is implemented as an autoencoder.
The face of the actor 1 is cropped and aligned to his face. Then the autoencoder learns how to encode and decode (reconstruct) the face. The goal here is to minimize the reconstruction error.

The face of the actor 2 is cropped and aligned to his face. Then the autoencoder learns how to encode and decode (reconstruct) the face. The goal here is to minimize the reconstruction error. The interesting part is that the encoder is the same for actor 1 and 2.

The goal is to find a mathematical function that for a face of the actor 1, outputs a face that looks like the actor 2.


## Autoencoder: how does it work ?

Autoencoder is great tool for producing images which respect the probability distribution of the original ones.

Auto encoder wants to find a function `f(x)` &asymp; ` x `where x is your image. For that, we have an **encoder** which goal is to encode your image in a smaller representation, and a **decoder** which goal is to use this representation and get back the original images. 


## Additional Points

1. In the original deepfakes' architecture, there is no mask segmentation. The only output is reconstructed image.

2. The interesting (and smart) parts of deepfakes' algorithm are the usage of warped image as input and shared-weights encoder. The encoder get update information (backprop. information) from both two decoder_A and B. But on the contrary, decoder_A never trained on face B for reconstruction (and vise versa for decoder_B). In other words, the encoder is able to encode both face A and B into good embedding, but decoder A/B can only generates face A/B respectively from the given embedding.

3. To swap face of person B to person A in test time, we feed face B in to encoder to get the embedding, and then feed the embedding into decoder A (not decoder B) to get a face B which is face A look-alike. The reason of such method works is that the autoencoder_A (i.e., encoder + decoder_A) treats face B as if its a warped A, so it "reconstruct" face B into a face A look-alike. If we did not train the autoencoder using warped images, it might not able to "treat face B as if its a warped A".

## Transfer Learning

In contrast to the base version of Deepfakes, we provide a very convenient way to speed up the training process via transfer learning. The idea is to load the weight of a pre-trained network. These weights are used as a starting point to learn new weight. The network will, therefore, converge faster than if it would be trained from scratch.


## Dependencies

Associated with this project, there is a file, "requirements.txt" which lists all libraries that need to be installed before to run the application.After creating Virtual env with **Python version 3.7**
```bash
pip install -r requirements.txt
```

Download the weights [here](https://drive.google.com/file/d/1J1PgGZDCufCxZ6vEwHwnM7czAXjIliH5/view?usp=sharing)
and unzip them in the folder:
```bash
cd deepfakes/weight
```

## Motivation

With AI area, it becomes easy for anyone to fake video, pictures, and news. As someone smart said one day: "With great power comes great responsibility".

