### Flappy Bird

this repo is an AI model trained to beat Flappy Bird game with the help of ML and Neural-Network.
this project was divided on 2 section [game-dev](#Game-dev) and [AI-training](#AI-training).

### Game dev
using `pygame` library to create 2d object. 

### AI training
using `tensorflow` to create the neural-network and train the model to beat this game

### install / run

 
* 1 install dependencies:
``` bash 
    $> python install.py # to install dependencies 
```

* 2 run the project
``` bash 
    $> python main.py # to start the game and play it
    $> # or to play vs the ai
    $> python main.py --with-ai --level=[0-9]
    $> # only the bot play 
    $> python main.py --ai
```

### training 
* to train the model use this command
``` bash
    $> python main.py --train
```

### help 
use help command to see all the commands

### this project created for fun and to play with tensorflow library.