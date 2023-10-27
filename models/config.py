# set lstm train parameters
class TrainingConfig(object):
    batch_size = 64
    # learn rate
    lr = 0.001
    epoches = 100
    print_step = 5


class LSTMConfig(object):
    emb_size = 128  # The dimension of the word vector
    hidden_size = 128  # lstm The dimension of an hidden vector
