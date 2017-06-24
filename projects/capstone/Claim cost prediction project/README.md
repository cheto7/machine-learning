# Machine Learning Engineer Nanodegree
# Capstone Project
## Project: Allstate Claim Severity

Before my enrollment on the Machine Learning Nanodegree Program I had an Idea of what Supervised Learning was, but now after seen all the scope of what this course offers me, I have a very clear understanding of what to do to solve multiple problems and situations. 
Supervised machine learning is the search for algorithms that reason from externally supplied instances to produce general hypotheses, which then make predictions about future instances. In other words, the goal of supervised learning is to build a concise model of the distribution of class labels in terms of predictor features. The resulting classifier is then used to assign class labels to the testing instances where the values of the predictor features are known, but the value of the class label is unknown. 
In this Capstone Project, I had the option to select a topic in Kaggle, so found a competition that I think suits my needs for this project, is the “Allstate Claims Severity Challenge”: Allstate is currently developing automated methods of predicting the cost, and hence severity, of claims. In this challenge, Allstate enforce you to show off your creativity by creating an algorithm which accurately predicts claims severity.


### Install

This project requires **Python 2.7** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [seaborn] (https://seaborn.pydata.org/)

You will also need to have software installed to run and execute an [iPython Notebook](http://ipython.org/notebook.html) or [Jupyter Notebook] (http://jupyter.org/)

### Code

Template code is provided in the `capstone-claim-loss-prediction.ipynb` notebook file. You will also be required to use the included `train.csv` dataset file.

### Run

In a terminal or command window, navigate to the top-level project directory (that contains this README) and run one of the following commands:

```bash
ipython notebook capstone-claim-loss-prediction.ipynb
```  
or
```bash
jupyter notebook capstone-claim-loss-prediction.ipynb
```

This will open the iPython Notebook software and project file in your browser.

### Data

The data is provided in (https://www.kaggle.com/c/allstate-claims-severity/data). 
Each row in this dataset represents an insurance claim. You must predict the value for the 'loss' column. Variables prefaced with 'cat' are categorical, while those prefaced with 'cont' are continuous. 

