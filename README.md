# GAN-Generative-Adversarial-Network
This repo illustrates how GAN -Generative Adversarial Networks can be helpful in creating incredibly highly realistic images and its architecture

## Overview :

The objective of this repository is to develop a Generative Adversarial Network (GAN) capable of generating realistic human faces. Leveraging the power of deep learning, this model is designed to learn from a dataset of human faces and create synthetic images that are indistinguishable from real ones. Here we explore GANs' ability to generate high-quality, fake human faces, showcasing their potential .

## Background :
 Generative Adversarial Networks (GANs) have revolutionized image synthesis by creating realistic images, including human faces, from scratch. GANs consist of two neural networks:
a generator that creates images and a discriminator that evaluates them for authenticity. Over multiple training iterations, the generator learns to produce increasingly realistic images while trying to fool the discriminator.

we focuses on applying GANs to generate photorealistic human faces. The generator is trained using a large dataset of real human faces, while the discriminator's task is to distinguish between real and synthetic faces, pushing the generator to improve over time.

## Dataset Details :

| value     | Description |
| | :------- | :------------------------- |
| Type | Images of real human faces|
| Dataset Sources| CelebA, FFHQ (Flickr-Faces-HQ) |
|Preprocessing|resized, normalized, and augmented to improve generalization flipping, cropping, and color normalization|
| Size | I have sample 3000 images due to less computational resources |
|PS.|for demonstration purpose|


## Model Architecture :
The GAN model consists of two key components:
## Generator: 
A neural network designed to generate realistic human faces from random noise (latent vectors).

![sample frame ](/generator.png)

## Discriminator:
A classifier that distinguishes between real and fake images, providing feedback to the generator.
The architecture employs deep convolutional layers (DCGAN) for both the generator and discriminator to effectively capture facial features.

![sample frame ](/discriminator.png)

## General Architecture

![sample frame ](/img2.png)