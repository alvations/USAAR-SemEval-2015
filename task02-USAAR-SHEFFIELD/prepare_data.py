
import numpy as np

from sts_data import get_meteor_scores, get_sts_scores
from asiya import get_asiya_scores, get_asiya_test_scores


def prepare_training_data_modelx():
    sts_scores = np.array(get_sts_scores('score.train'))
    _x, to_remove = get_asiya_scores()
    x = np.array(_x)
    y = sts_scores
    y =np.delete(y, to_remove, axis=0)
    n = len(y)
    
    np.savetxt('x.asiya.train', x)
    np.savetxt('y.asiya.train', y)

    test_asiya_scores = np.array(get_asiya_test_scores())
    np.savetxt('x.asiya.test', test_asiya_scores)

def prepare_training_data_modelz():
    meteor_scores = np.array(get_meteor_scores('meteor.output.train'))
    test_meteor_scores = np.array(get_meteor_scores('meteor.output.test'))
    sts_scores = np.array(get_sts_scores('score.train'))
    
    np.savetxt('x.meteor.train', meteor_scores)
    np.savetxt('y.meteor.train', sts_scores)
    np.savetxt('x.meteor.test', test_meteor_scores)
