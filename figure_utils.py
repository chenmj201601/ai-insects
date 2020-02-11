import matplotlib.pyplot as plt


def draw_figure_loss(loss, val_loss):
    count = len(loss)
    epochs = range(1, count + 1)
    plt.plot(epochs, loss, 'bo', label='Training loss')
    plt.plot(epochs, val_loss, 'b', label='Validation loss')
    plt.title('Training and Validation loss')
    plt.legend()
    plt.savefig('insects_loss_{}.png'.format(count))
    plt.show()
