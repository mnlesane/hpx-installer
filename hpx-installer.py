# Copyright (c) 2013 Michael LeSane
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

import os

#configuration
install_path = "/home/mlesane/hpx_bin"
build_path = "/home/mlesane/hpx_bld"
source_path = "/home/mlesane/Downloads/hpx"
boost_path = "/opt/boost/1.53.0-release/"
cores = 24

os.system("mkdir "+install_path)
os.system("mkdir "+build_path)
os.system("git clone https://github.com/STEllAR-GROUP/hpx.git "+source_path)
os.chdir(build_path)
os.system("cmake -DBOOST_ROOT="+boost_path+" -DCMAKE_INSTALL_PREFIX="+install_path+" "+source_path)
os.system("make -j "+str(cores)+" install")
