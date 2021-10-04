import matplotlib.pyplot as plt


def generate_plot(path, title, indicator, indicator_en, jacobi, gauss_seidel, sor, show_signatures=None):

    methods = ['Jacobi', 'Gauss-Seidel', 'SOR']
    results = [jacobi, gauss_seidel, sor]

    plt.figure(title)
    plt.title(title, weight='bold')
    plt.xlabel('metoda', weight='bold')
    plt.ylabel(indicator, weight='bold')
    # plt.grid(True)

    bars = plt.bar(methods, results)
    bars[0].set_color('#D14960')
    bars[1].set_color('#7DC481')
    bars[2].set_color('#2C84C7')

    if show_signatures is not None:
        for i in range(3):
            plt.text(i, results[i], results[i],
                     fontsize='10', ha='center', va='bottom')

    plt.savefig(f'{path}/{indicator_en}.png')
