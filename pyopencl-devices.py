"""
    Simple utility to list some interesting properties of all OpenCL devices.
"""

import pyopencl

# Dummy kernel to have access to kernel properties
CODE = "__kernel void test() { float a = (1.0f + 2.0f) * 3.0f; }"

print()
for platform in pyopencl.get_platforms():
    for device in platform.get_devices():
        context = pyopencl.Context([device])
        program = pyopencl.Program(context, CODE).build()
        kernel = pyopencl.Kernel(program, "test")

        print("Platform: " + platform.name)
        print("Device: " + device.name + " (" + pyopencl.device_type.to_string(device.type) + ")")
        print("\tGlobal memory: \t\t" + str(device.global_mem_size / 2**30) + " GB")
        print("\tGlobal cache: \t\t" + str(device.global_mem_cache_size / 2**10) + " KB (" + pyopencl.device_mem_cache_type.to_string(device.global_mem_cache_type) + ")")
        print("\tGlobal cache line: \t" + str(device.global_mem_cacheline_size) + " B")
        print("\tLocal memory: \t\t" + str(device.local_mem_size / 2**10) + " KB (" + pyopencl.device_local_mem_type.to_string(device.local_mem_type) + ")")
        print("\tConstant memory: \t" + str(device.max_constant_buffer_size / 2**10) + " KB")
        print("\tCompute units: \t\t" + str(device.max_compute_units))
        print("\tMax work-group size: \t" + str(device.max_work_group_size))
        print("\tMax work-item size: \t" + str(device.max_work_item_sizes))
        print("\tLockstep unit: \t\t" + str(kernel.get_work_group_info(pyopencl.kernel_work_group_info.PREFERRED_WORK_GROUP_SIZE_MULTIPLE, device)))
        print()
