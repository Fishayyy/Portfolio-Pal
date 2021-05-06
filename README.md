# Portfolio-Pal

## Overview
Portfolio-Pal is a research project that I took on to determine if Reinforcement Learning could be a useful tool for training an AI to learn how to trade stocks effectively. Along the way I realized that I didn't know much about the stock market so I tried to incorperate a lot of data exploration and data analysis tools into my project to help me learn more about the stock market, but also to help me visualize the trends in the data I aquired. Many humans have tried their hand at trading in the stock market and failed due to the highly stochastic and unpredictable nature associated with the fluctations of a stock's price. This project aims to be an educational tool for anyone who is looking to get into programming their own stock trading bots or just learn more about stock trading in general.

### Experience Gained ###
* Python
* Keras, Tensorflow, OpenAI Gym, and Pytorch at different points
* Matplotlib, Seaborn, and Pyfolio
* pandas, scikit-learn, and numpy
* Several specialized stock APIs through different stages
* Stock market and Investing knowledge

### Prerequisites
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
- After that it's as simple as opening up Portfolio-Pal.ipynb in Jupyter Notebook and following along with the guided instructions.

## Current State
Currently this project exists as a Jupyter notebook that is easy to follow along with and incorperates different steps of having the user to explore their stock options then eventually transitioning into an AI simulating a stock portfolio. As is, all trade simulations are theoretical and it is not necisarrily meant to be used as something you could follow along with and make trades every day. You can however analyse the predictions that are outputed based on a previous days data to see how the AI would try to perform the next day. The 4 ML we chose to simulate with FinRL libraries are:
  1. A2C: Advantage Actor Critic
  2. PPO: Proximal Policy Optimization
  3. SAC: Soft Actor-Critic
  4. TD3: Twin Delayed Deep Deterministic Policy Gradients 

### TODO Improvements ###
1. Replace FinRL with custom built solutions - FinRL is meant to be educational and has many videos and tutorials to make it easy to use and accessible, but it is limited to the models, environments and agents that are included with it. Thus, it is not very customizable. Originally my project had a custom built agent and environment for single stock trading without any budget implemented, but I was unsuccessful and getting it to be reliable and the results it outputted were less useful than what I can get with FinRL
2. Sentiment analysis - One project that I thought was interesting but didn't have enough time for was including sentiment analysis in the algorithm. By utilizing sentiment indicators it is also possible to help predict a stocks price movent that would defy tradiontional movement patterns. 
3. Better way to train hyperparameters - My current method for training the algorithm is by using a guess and check method and sometimes it can be difficult to determine when certain changes have made enough a difference. The backtesting plots and graphs can be difficult to interpret if you don't know what it is you looking at.
4. Inclusion of better features - Since I'm a computer scientist and not necissarily a financial expert there could be other features out there that I had not considered. I tried to keep my inputs relatively simple since I already had such a large network to train. Another possible consideration could be performing more indepth feature analysis. This would also mean we could build in more charts and graphs to analyze!
5. Trading Fees - Currently I only had a flat trading fee of $0.01 for each trade, but there's so much more involved with the costs associated with making a trade such as taxes and fees per trade, available trading times, and trading speed that exist in real world scenarios.
6. Simplification and possible GUI - Currently this project is meant for data scientists and those who are comfortable programming and installing packages in a python environment. If this were to become a tool in the future it would need to be built in a way that is more accessible to a general user.

### Recommended Reading and Resources
- [FinRL](https://arxiv.org/abs/2011.09607): A Deep Reinforcement Learning Library for Automated Stock Trading in Quantitative Finance
- [The Intelligent Investor](https://www.amazon.com/dp/B000FC12C8?tag=aboutcom02thebalance-20&linkCode=ogi&th=1&psc=1&ascsubtag=4171823%7Cn51c19562956647b8b4e53e8e4ef49f4b03)
- [Machine Learning for Finance](https://www.amazon.com/dp/1789136369)
- [Deep Reinforcement Learning Hands-On](https://www.amazon.com/Deep-Reinforcement-Learning-Hands-optimization/dp/1838826998)

