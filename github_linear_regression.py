import requests
import tqdm
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt


API_URL = "https://api.github.com/search/repositories?"+\
          "q=language:python&sort=stars&per_page=100&page={}"


def data_to_tuple (data):
    x1 = [item[0] for item in data]
    y1 = [item[1] for item in data]
    tuple = (x1, y1)
    return tuple


def get_github_data(git_api):
    response_data = []
    for i in tqdm.trange(1, 31):
        # print(git_api.format(i))
        response = requests.get(git_api.format(i))
        if response.status_code == 200:
            data = response.json()
            # print(data)
            items = data['items']
            forks_and_stars = [(item['forks_count'], item['stargazers_count'])
                               for item in items]
            response_data.extend(forks_and_stars)
            return (response_data)


def calc_liner_regression(data):
    X = [[item[0]]for item in data]
    y = [[item[1]]for item in data]
    reg = LinearRegression()
    reg.fit(X, y)
    slop = reg.coef_[0]
    intercept = reg.intercept_
    x1 = [item[0] for item in data]
    y1 = [item[1] for item in data]

    return x1, y1,  slop, intercept


def desplay_lr_line(x, y, slop, intercept ):

    reg_line_x =[0, max(x)]
    reg_line_y =[intercept, max(x)*slop + intercept]
    plt.figure(figsize=(14, 8))
    plt.scatter(x,y, label='fork and stars')
    plt.plot(reg_line_x, reg_line_y, label = 'linear regression line')
    plt.xlabel('forks')
    plt.ylabel('stars')
    plt.show()

def main():
    data = get_github_data(API_URL)
    x, y, slop, intercept = calc_liner_regression(data)
    desplay_lr_line(x, y, slop, intercept)
    # return a

main()

# x = [1,2,3,4]
# y = [3,5,7,10] # 10, not 9, so the fit isn't perfect
#
# coef = np.polyfit(x,y,1)
# poly1d_fn = np.poly1d(coef)
# # poly1d_fn is now a function which takes in x and returns an estimate for y
#
# plt.plot(x,y, 'yo', x, poly1d_fn(x), '--k') #'--k'=black dashed line, 'yo' = yellow circle marker
#
# plt.xlim(0, 5)
# plt.ylim(0, 12)


def test(x, y, slop, intercept):
    coef = np.polyfit(x, y, 1)
    poly1d_fn = np.poly1d(coef)
    plt.plot(x, y, 'yo', x, poly1d_fn(x), '--k')
    plt.xlabel('forks')
    plt.ylabel('stars')
    plt.xlim(0, max(x))
    plt.ylim(0, max(y))
    plt.show()