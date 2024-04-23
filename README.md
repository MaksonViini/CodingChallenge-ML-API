# CodingChallenge-ML-API


## Run the Project
*Using Docker*

First you need to put in command line this command:

```
docker image build -t IMAGE_NAME:version .
```

That code will build your image.

The Dockerfile will be selected by the '.', the build will use multistage build, the firt part, use the 'alpine' image, the smallest to build and make a requirements using poetry, the second part will build a 'slim-bullseye' to build a image from the first stage, the imagem was used because needed to install the library 'scikit-learn' and you need 'gcc' and 'g++' to build that package.

The advantage about multistage is because you can use less space, the image size will be less than the normal image.


Seconth, to run the image, use the command:

```
docker container run -dit -p 8080:8080 IMAGE_ID
```
