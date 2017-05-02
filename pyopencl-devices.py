"""
    Simple utility to list some interesting properties of all OpenCL devices.
"""

import pyopencl

print()
for platform in pyopencl.get_platforms():
    for device in platform.get_devices():
        print("Platform: " + platform.name)
        print("Device: " + device.name + " (" + pyopencl.device_type.to_string(device.type) + ")")
        print("Global memory: " + str(device.global_mem_size / 2**30) + " GB")
        print("Global cache: " + str(device.global_mem_cache_size / 2**10) + " KB (" + pyopencl.device_mem_cache_type.to_string(device.global_mem_cache_type) + ")")
        print("Global cache line: " + str(device.global_mem_cacheline_size) + " B")
        print("Local memory: " + str(device.local_mem_size / 2**10) + " KB (" + pyopencl.device_local_mem_type.to_string(device.local_mem_type) + ")")
        print("Constant memory: " + str(device.max_constant_buffer_size / 2**10) + " KB")
        print("Compute units: " + str(device.max_compute_units))
        print("Max work-group size: " + str(device.max_work_group_size))
        print("Max work-item size: " + str(device.max_work_item_sizes))
        print("Vector (float): " + str(device.native_vector_width_float))
        print("Vector (double): " + str(device.native_vector_width_double))
        print("Vector (half): " + str(device.native_vector_width_half))
        print()
