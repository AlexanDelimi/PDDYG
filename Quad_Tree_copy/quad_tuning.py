
def just_plots():
    from math import sqrt
    import matplotlib.pyplot as plt

    _, ax = plt.subplots()
    
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
    plt.plot(x_axis, root_of_root, '-d', label='sqrt(sqrt(x))')
    plt.plot(x_axis, half_root_of_root, '-x', label='0.5*sqrt(sqrt(x))')

    ax.legend()
    plt.show()


thres_funcs = ['log10(x)', '5', '(log10(x))^2', '0.5*(log10(x))^2', 'sqrt(sqrt(x))', '0.5*sqrt(sqrt(x))']
num_neighbors = [1, 5, 10, 25, 50, 100, 250, 500]
symbol = {  'log10(x)': '-o',
            '5': '-*',
            '(log10(x))^2': '-s',
            '0.5*(log10(x))^2': '-+',
            'sqrt(sqrt(x))': '-d',
            '0.5*sqrt(sqrt(x))': '-x'   }
target_points = [   (167,833), (500,833), (833,833),
                    (167,500), (500,500), (833,500),
                    (167,167), (500,167), (833,167)  ]


def get_ready(file):
    from QuadTree import QuadTree
    from random import uniform
    from math import sqrt
    from time import process_time_ns
    import json

    thres = {}

    results = {}

    for i in range(1, 7):
        print(i)
        
        x = 10**i
        points = [(uniform(0, 1000), uniform(0, 1000)) for _ in range(x)]
    
        thres['log10(x)'] = i
        thres['5'] = 5
        thres['(log10(x))^2'] = i**2
        thres['0.5*(log10(x))^2'] = 0.5*(i**2)
        thres['sqrt(sqrt(x))'] = sqrt(sqrt(10**i))
        thres['0.5*sqrt(sqrt(x))'] = 0.5*sqrt(sqrt(10**i))

        results[str(i)] = {}
    
        for func in thres_funcs:
            print('\t' + func)

            qtree = QuadTree(thres[func], points)

            results[str(i)][func] = {}

            for k in num_neighbors:
                print('\t\t' + str(k))

                start = process_time_ns()

                for target in target_points:

                    _ = qtree.k_nn(target, k)
                    
                elapsed = process_time_ns() - start

                results[str(i)][func][str(k)] = elapsed // 9

    with open(file, 'w') as f:
        json.dump(results, f)


def and_go(file):
    import matplotlib.pyplot as plt
    import json
    from math import log10

    with open(file, 'r') as f:
        results = json.load(f)

        _, axs = plt.subplots(2, 3)

        for i in range(1,7):

            for func in thres_funcs:

                axs[i//4, (i-1)%3].plot(num_neighbors, 
                                        [ results[str(i)][func][str(k)] for k in num_neighbors ],
                                        symbol[func], 
                                        label=func)
                # axs[i//4, (i-1)%3].plot(num_neighbors, 
                #                         [ log10( results[str(i)][func][str(k)] + 10**0.001 ) for k in num_neighbors ],
                #                         symbol[func], 
                #                         label=func)
                axs[i//4, (i-1)%3].set_title('10**' + str(i) + ' points')
                axs[i//4, (i-1)%3].legend()
        
        plt.show()

def new_one():
    from math import log
    
    for i in range(1,10):
        print( 'n=10^' + str(i) + '\td=' + str(log(10**i,4)) )


if __name__=='__main__':
    
    # file = './Quad_Tree_copy/times_5.json'
    # get_ready(file)
    # and_go(file)
    
    new_one()
