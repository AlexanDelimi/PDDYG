from QuadTree import QuadTree
from random import uniform
from math import log10, sqrt
import matplotlib.pyplot as plt

def main():
    fig, ax = plt.subplots()
    
    x_axis = []
    lg = []
    lg_times_2 = []
    lg_squared = []
    half_lg_squared = []
    root_of_root = []
    half_root_of_root = []
    for i in range(1,10):
        x_axis.append(10**i)
        lg.append(i)
        lg_times_2.append(2*i)
        lg_squared.append(i**2)
        half_lg_squared.append(0.5*(i**2))
        root_of_root.append(sqrt(sqrt(10**i)))
        half_root_of_root.append(0.5*sqrt(sqrt(10**i)))
    
    plt.plot(x_axis, lg, '-o', label='log10(x)')
    plt.plot(x_axis, lg_times_2, '-*', label='2*log10(x)')
    plt.plot(x_axis, lg_squared, '-s', label='(log10(x))^2')
    plt.plot(x_axis, half_lg_squared, '-+', label='0.5*(log10(x))^2')
    plt.plot(x_axis, root_of_root, '-d', label='sqrt(sqrt(x)')
    plt.plot(x_axis, half_root_of_root, '-x', label='0.5*sqrt(sqrt(x)')

    ax.legend()

    plt.show()

if __name__=='__main__':
    main()