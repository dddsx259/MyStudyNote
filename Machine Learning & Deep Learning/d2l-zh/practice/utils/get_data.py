import torchvision
from torch.utils import data
from torchvision import transforms

DATA_PATH = '../data/'

trans = transforms.ToTensor()
mnist_train = torchvision.datasets.FashionMNIST(root=DATA_PATH, train=True, download=True, transform=trans)
mnist_test = torchvision.datasets.FashionMNIST(root=DATA_PATH, train=False, download=True, transform=trans)

def get_data(dataset = 'fashion_mnist', batch_size = 256, train_shuffle = True, test_shuffle = False, n_workers = 0):
    
    if dataset == 'fashion_mnist':
        train_iter = data.DataLoader(mnist_train, batch_size, shuffle=train_shuffle, num_workers=n_workers)
        test_iter = data.DataLoader(mnist_test, batch_size, shuffle=test_shuffle, num_workers=n_workers)
    else:
        raise NotImplementedError('Dataset not implemented: ' + dataset)
    return train_iter, test_iter