# CMakeLists.txt

cmake_minimum_required(VERSION 2.8)

project(eigenbox)

include_directories(contrib/eigen3)

add_executable(hello
	src/hello.cpp
	include/hello.hpp)

# EOF
