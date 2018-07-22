import h5py
import numpy as np

mydict={'file_1': [np.eye(2), np.array([1, 4])], 
        'file_2': [np.zeros(3), np.array([5, 6]), 44]}

dictname = "mydict.hdf5"

print("---save---")

with h5py.File(dictname, "w") as fh:
    for key, value in mydict.items():
        print(key, value)
        grp = fh.create_group(key)
        for idx, item in enumerate(value):
            grp.create_dataset(str(idx), data=item)

print("---load---")

with h5py.File(dictname, 'r') as fh:
    for key, item in fh.items():
        for idx in item:
            print(key, fh[key][idx].value)
            print(key, fh.get(key).get(idx).value)
