# http://karthikhegde.blogspot.co.at/2013/09/hope-you-liked-previous-introductory.html

# import the required modules
import pyopencl as cl
import numpy as np
#this line would create a context
cntxt = cl.create_some_context()
#now create a command queue in the context
queue = cl.CommandQueue(cntxt)


# create some data array to give as input to Kernel and get output
num1 = np.array(range(100), dtype=np.int32)
num2 = np.array(range(100), dtype=np.int32)
out = np.empty(num1.shape, dtype=np.int32)

# create the buffers to hold the values of the input
num1_buf = cl.Buffer(cntxt, cl.mem_flags.READ_ONLY | 
cl.mem_flags.COPY_HOST_PTR,hostbuf=num1)
num2_buf = cl.Buffer(cntxt, cl.mem_flags.READ_ONLY | 
cl.mem_flags.COPY_HOST_PTR,hostbuf=num2)

# create output buffer
out_buf = cl.Buffer(cntxt, cl.mem_flags.WRITE_ONLY, out.nbytes)

# Kernel Program
code = """
__kernel void frst_prog(__global int* num1, __global int* num2,__global int* out) 
{
    int i = get_global_id(0);
    out[i] = num1[i]*num1[i]+ num2[i]*num2[i];
}
"""
# build the Kernel
bld = cl.Program(cntxt, code).build()
# Kernel is now launched
launch = bld.frst_prog(queue, num1.shape, num1_buf,num2_buf,out_buf)
# wait till the process completes
launch.wait()

cl.enqueue_read_buffer(queue, out_buf, out).wait()
# print the output
print "Number1:", num1
print "Number2:", num2
print "Output :", out