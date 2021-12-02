import numpy as np
import matplotlib.pyplot as plt


def get_beans(counts):
    xs = np.random.rand(counts)
    xs = np.sort(xs)
    ys = [1.2 * x + np.random.rand() / 10 for x in xs]
    return xs, ys


if __name__ == '__main__':
    xs, ys = get_beans(100)

    plt.title("Size-Toxicity Function", fontsize=12)
    plt.xlabel("Beean Size")
    plt.ylabel("Toxicity")

    w = 0.1
    for _ in range(100):
        for i in range(100):
            x = xs[i]
            y = ys[i]
            k = 2 * (x ** 2) * w + (-2 * x * y)
            alpha = 0.1
            w = w - alpha * k

            plt.clf()
            plt.xlim(0, 1.1)
            plt.ylim(0, 1.4)
            plt.scatter(xs, ys)
            y_pre = w * xs
            plt.plot(xs, y_pre)
            plt.pause(0.1)
