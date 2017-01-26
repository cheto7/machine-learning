#
#
# Regression and Classification programming exercises
#
#


#
#	In this exercise we will be taking a small data set and computing a linear function
#	that fits it, by hand.
#	

#	the data set

import numpy as np

sleep = [5,6,7,8,10]
scores = [65,51,75,75,86]


def compute_regression(sleep,scores):

    #	First, compute the average amount of each list

    avg_sleep = np.mean(sleep)
    avg_scores = np.mean(scores)

    #	Then normalize the lists by subtracting the mean value from each entry

    normalized_sleep = [xx - avg_sleep for xx in sleep]
    normalized_scores = [xx - avg_scores for xx in scores]

    #	Compute the slope of the line by taking the sum over each student
    #	of the product of their normalized sleep times their normalized test score.
    #	Then divide this by the sum of squares of the normalized sleep times.

    slope = 0
    sum_product = 0
    sum_squares_sleep = 0
    for ii in range(0,len(normalized_sleep)):
        sum_product += normalized_sleep[ii] * normalized_scores[ii]
        sum_squares_sleep += normalized_sleep[ii]**2
        
    slope = sum_product / sum_squares_sleep

    #	Finally, We have a linear function of the form
    #	y - avg_y = slope * ( x - avg_x )
    #	Rewrite this function in the form
    #	y = m * x + b
    #	Then return the values m, b
    
    b = - (slope * avg_sleep) + avg_scores
    m = slope

    return m,b


if __name__=="__main__":
    m,b = compute_regression(sleep,scores)
    print "Your linear model is y={}*x+{}".format(m,b)