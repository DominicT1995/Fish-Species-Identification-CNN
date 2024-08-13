# Fish-Species-Identification-CNN
![banner image](https://github.com/DominicT1995/Fish-Species-Identification-CNN/blob/main/Project4/images/bannerCNN.png?raw=true)

## Group Members: 
Alberto Alvarado, Jeff Neal, Dominic Thomas, Angelie Wanner

## Project Proposal:
The aim of this project is to develop a machine learning model capable of classifying different species of fish from images. The project will involve data collection, preprocessing, model training, and evaluation to identify various fish species with high accuracy.

Further enhancements to this project can effectively be beneficial to researchers, conservationists, and fishing enthusiasts. By following a structured approach, we aim to build an effective and user-friendly classification system.

Tools utilized: Python, Tensorflow, Flask, Web Based UI (HTML, JavaScript) 

## Process:

#### Data Collection:

The first step in creating the classification system was defining which species of fish were of interest for the scope of the project and acquiring image data of these fish to train the neural network. The following 11 species of Texas game fish were used for image data collection and gathered using Google Image download extension for the chrome browser:

* Black Crappie
* Cobia
* Flounder
* King Mackeral
* Large Mouth Bass
* Small Mouth Bass
* Red Drum Fish
* Snook
* Tarpon
* Tripletail
* Trout

#### Image Directory Setup and Preprocessing:

Approximately 200-250 images were collected for each species of fish. Next, an image directory was setup consisting of training, testing, and validation datasets with a split ratio of (0.7, 0.1, 0.2). Images were then preprocessed and scaled to 256x256 pixels and pixel values were then rescaled to values in the range of 0 to 1 for model training.

#### Model Creation:

A convolutional neural network model was then created with architecture consisting of the following layers:

* Convolutional layers
* Pooling layers
* Augmentation layer (opted to omit for noted improved performance)
* Dropout layers
* Batch Normalization layers
* Flatten layer
* Fully Connected layer

The number of layers, overall architecture, and hyperparameters including epochs, learning rate, and batch size were continuously adjusted and evaluated based on resulting training accuracy, training loss, validation accuracy, and validation loss.

In addition, two different optimizers (adam and sgd) were utilized in the compiling of the different model architectures with the sgd optimizer outperforming the adam optimizer when training on the full image dataset and thus used for final model compiling.

Final Model Architecture:

![Model Architecture](https://github.com/DominicT1995/Fish-Species-Identification-CNN/blob/main/Project4/images/final_model_architecture.png?raw=true)

## Results:

The final model was chosen to be used for the web based application due to its lower validation loss compared to other previous models and its improved performance with identifying random fish images when run through the Flask app.

![Final Model Accuracy](https://github.com/DominicT1995/Fish-Species-Identification-CNN/blob/main/Project4/images/acc_graph_model_final_2.png?raw=true) ![Final Model Loss](https://github.com/DominicT1995/Fish-Species-Identification-CNN/blob/main/Project4/images/loss_graph_model_final_2.png?raw=true)

Hyperparamters of final model include:
* Batch Size: 32
* Epochs: 75
* Two layers of convolution and pooling with Batch Normalization
* Optimizer: sgd
* Callback function to reduce learning rate on plateau (initial LR: 0.01, reduction factor: 0.1, patience: 10)

The final model was then hosted on a web based Flask application allowing users to upload an image from their personal device and make a prediction between the 11 defined species of Texas game fish with confidence percentages of the prediction and information regarding the fish species relative to Texas game fishing regulations.

![web model use](https://github.com/DominicT1995/Fish-Species-Identification-CNN/blob/main/Project4/images/predictionCNN.png?raw=true)

## Limitations:

* Limited to 11 species of fish
  - Due to time constraints of the project and long training times, the project was limited to only 11 species of fish. The dataset could be expanded in the future and the model architecture applied to a larger variety of fish.
* Small Dataset Size
  - The overall size of the dataset was relatively small and additional images could have improved performance in distinguishing between differing species or more specific features of each species.
* Similarities in Images
  - All images contained some variation of similarities in dark areas of water, water based backgrounds, or presence of fishermen likely creating identifiable patterns that were not of interest when training the model.
* Image Availability
  - More images were available of some species of fish than others. In the final dataset used, some fish such as the Black Crappie had closer to 300-400 images while others only had close to 200 images which could have resulted in the model favoring the Black Crappie class in its predictions. In future variations of this model, the classes should be trimmed and made even based upon the least available images of a species.
* Model Creation Method
  - Transfer learning could have been utilized to improve efficiency and startup times when training the model, yielding quicker results to meet the project deadline.

## Data Source and Inspirations:

Model creation guidance taken from the following article:
https://medium.com/latinxinai/convolutional-neural-network-from-scratch-6b1c856e1c07

Texas game fish information:
https://tpwd.texas.gov/regulations/outdoor-annual/fishing/general-rules-regulations/general-fishing-regulations

Dataset images were retrieved from Google Image searches.
