import os
os.chdir('/home/aron/Downloads/NextGame/')

import pandas as pd
import numpy as np
from random import choice
from nextme import run_sequence

def run():

	seqs = pd.read_csv('sequences_medium',header=None,sep=' ')

	seqs_matrix = seqs.as_matrix()

	aviables = seqs_matrix[:,-1] == 0

	total = len(seqs_matrix)

	index = np.arange(total)

	ch = choice(index[aviables])

	seq = seqs_matrix[ch,:-1]

	file = open("logs.txt", "ab")

	file.write(str(seq)+"\n")

	run_sequence(seq)

	seqs_matrix[ch,-1] = seqs_matrix[ch,-1] + 1

	seqs_updated = pd.DataFrame(seqs_matrix)

	seqs_updated.to_csv('sequences_medium',header=None,sep=' ',index=False)
