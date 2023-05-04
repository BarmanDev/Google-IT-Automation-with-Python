# Fill in the blank to calculate how many sectors a given 16 GB (gigabyte) hard disk drive has.
# The given hard drive is divided into sectors of 512 bytes each.
# How many sectors should this drive have? Your result should be in the format of just a number, not a sentence.
# Note: To calculate the disk size, multiply by multiples of 1024.  In the code below,  the "disk_size" of 16 GB is expressed as multiplying 16 by 1024 three times to get from bytes, to kilobytes, to megabytes, and finally to gigabytes.


disk_size = 16*1024*1024*1024
sector_size = 512
sector_amount = 16*1024**3/512


print(sector_amount)
