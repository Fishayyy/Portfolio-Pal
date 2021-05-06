# Portfolio-Pal

## Overview


### Experience Gained ###
* Python
* Keras, Tensorflow, OpenAI Gym, and Pytorch at different points
* Matplotlib, Seaborn, and Pyfolio
* pandas, scikit-learn, and numpy
* Several specialized stock APIs through different stages
* I gained a lot of knowledge about the stock market during this project

### Program and Code Prerequisites ###
- Anaconda (Recommended)
  - Python 3
  - numpy
  - pandas
  - scikit-learn
  - matplotlib
  - Jupyter Notebook
- FinRL Library
- stockstats
- yfinance
- pyfolio
- gym
- stable-baselines3[extra] (IMPORTANT)

### Getting Started ###
- If you haven't already I would start by installing Anaconda on you computing environment then heading over to the [FinRL](http://finrl.org/guide/installation.html) website to begin installing their library and making sure that you have all the recommended packages and code.


### Current State ###


### TODO Improvements ###
1. Replace FinRL with custom built solutions - FinRL is meant to be educational and has many videos and tutorials to make it easy to use and accessible, but it is limited to the models, environments and agents that are included with it. Thus, it is not very customizable. Originally my project had a custom built agent and environment for single stock trading without any budget implemented, but I was unsuccessful and getting it to be reliable and the results it outputted were less useful than what I can get with FinRL
2. Sentiment analysis - One project that I thought was interesting but didn't have enough time for was including sentiment analysis in the algorithm. By utilizing sentiment indicators it is also possible to help predict a stocks price movent that would defy tradiontional movement patterns. 
3. Better way to train hyperparameters - My current method for training the algorithm is by using a guess and check method and sometimes it can be difficult to determine when certain changes have made enough a difference. The backtesting plots and graphs can be difficult to interpret if you don't know what it is you looking at.
4. Inclusion of better features - Since I'm a computer scientist and not necissarily a financial expert there could be other features out there that I had not considered. I tried to keep my inputs relatively simple since I already had such a large network to train. Another possible consideration could be performing more indepth feature analysis. This would also mean we could build in more charts and graphs to analyze!
5. Simplification and possible GUI - Currently this project is meant for data scientists and those who are comfortable programming and installing packages in a python environment. If this were to become a tool in the future it would need to be built in a way that is more accessible to a general user.

### Recommended Reading and Resources ###
