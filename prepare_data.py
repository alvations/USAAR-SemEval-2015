from sts_data import get_meteor_scores, get_sts_scores
from asiya import get_asiya_scores

meteor_scores = np.array(get_meteor_scores('meteor.output.train'))
sts_scores = np.array(get_sts_scores('score.train'))

test_meteor_scores = np.array(get_meteor_scores('meteor.output.test'))

x = meteor_scores
_x, to_remove = get_asiya_scores()

x = np.array(_x)
y = sts_scores
y =np.delete(y, to_remove, axis=0)
n = len(y)

np.savetxt('x.train', x)
np.savetxt('y.train', y)
