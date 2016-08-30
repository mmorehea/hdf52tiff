import h5py
import glob
import code

stack = h5py.File('cvcn/h5stack/VCN_corrected_EM_8bit_Tracking-Result_.h5', 'r')

print "extracting entire stack, please wait"
b = stack['exported_data'][:]
print "done extracting"
c = b.reshape(b.shape[0:2])
zz, xx, yy, cc, tt = b.shape


code.interact(local=locals())
