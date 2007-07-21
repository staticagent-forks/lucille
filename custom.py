#
# If you want to specify your C compiler, uncomment below line and set it.
#
#CC = 'gcc'


#
# Build target 
#
# 'debug'   : debug compile(-g).
# 'release' : release compile(-O2). default
# 'speed'   : Maximum optimization. experimental
build_target = 'debug'

#
# SSE option.
#
enable_sse = 1

#
# Specify floating point precision.
#
# 0 : use float
# 1 : use double
#
use_double = 0


#
# LLVM settings
#
#use_llvm = 1


#
# If you turn 'use_llvm' on, set path to llvm toolchain here.
#
LLVM_CC     = 'llvm-gcc'
LLVM_AR     = 'llvm-ar'
LLVM_LD     = 'llvm-ld'
LLVM_RANLIB = 'llvm-ranlib'
LLVM_LINK   = 'llvm-ld'
