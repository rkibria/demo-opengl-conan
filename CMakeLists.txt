cmake_minimum_required(VERSION 3.10.0)

project(demo_opengl_conan)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

find_package(OpenGL REQUIRED)
find_package(GLEW REQUIRED)
find_package(glfw3 3.3 REQUIRED)

add_executable(demo_opengl_conan
	main.cpp )

target_compile_features(demo_opengl_conan PRIVATE cxx_std_14)

set_target_properties(demo_opengl_conan
	PROPERTIES
	RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin" )

target_link_libraries(demo_opengl_conan
	OpenGL::GL
	GLEW::GLEW
	glfw )
