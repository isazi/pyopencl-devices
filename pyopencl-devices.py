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
        print("\tDevice: " + device.name + " (" + pyopencl.device_type.to_string(device.type) + ")")
        print("\t\tGlobal memory: \t" + str(device.global_mem_size / 2**30) + " GB")
        print("\t\tGlobal cache: \t" + str(device.global_mem_cache_size / 2**10) + " KB (" + pyopencl.device_mem_cache_type.to_string(device.global_mem_cache_type) + ")")
        print("\t\tGlobal cache line: \t" + str(device.global_mem_cacheline_size) + " B")
        print("\t\tLocal memory: \t" + str(device.local_mem_size / 2**10) + " KB (" + pyopencl.device_local_mem_type.to_string(device.local_mem_type) + ")")
        print("\t\tConstant memory: \t" + str(device.max_constant_buffer_size / 2**10) + " KB")
        print("\t\tCompute units: \t" + str(device.max_compute_units))
        print("\t\tMax work-group size: \t" + str(device.max_work_group_size))
        print("\t\tMax work-item size: \t" + str(device.max_work_item_sizes))
        print("\t\tPreferred work-group multiple: \t" + str(kernel.get_work_group_info(pyopencl.kernel_work_group_info.PREFERRED_WORK_GROUP_SIZE_MULTIPLE, device)))
        print()
