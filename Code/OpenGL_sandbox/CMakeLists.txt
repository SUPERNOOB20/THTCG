# Template / barebone settings :3
cmake_minimum_required(VERSION 3.23)
find_package(PkgConfig REQUIRED)

project(Tutorial_01 CXX C)

set(LIB_INCLUDE)
set(LIB_LINK)

# glfw
pkg_search_module(GLFW REQUIRED glfw3)
list(APPEND LIB_INCLUDE ${GLFW_INCLUDE_DIRS})
list(APPEND LIB_LINK glfw)

# glew
find_package(GLEW REQUIRED)
list(APPEND LIB_INCLUDE ${GLEW_INCLUDE_DIRS})
list(APPEND LIB_LINK GLEW GLU GL)

# glm
find_package(glm CONFIG REQUIRED)
list(APPEND LIB_INCLUDE ${GLM_INCLUDE_DIRS})
# list(APPEND LIB_LINK glm)

# stb
list(APPEND LIB_INCLUDE "external/stb/")

# # bass
# list(APPEND LIB_INCLUDE "external/bass/")
# list(APPEND LIB_LINK "external/bass/libs/x86_64/libass.so")

# Source files
file(GLOB_RECURSE SOURCE_FILES "src/*.cpp")

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_CXX_FLAGS_DEBUG "$ENV{CXXFLAGS} -Wall -Wextra -Wpedantic -O0 -g2 -ggdb -Wno-psabi")
set(CMAKE_CXX_FLAGS_RELEASE "$ENV{CXXFLAGS} -Wall -Wextra -Wpedantic -O3 -Wno-psabi")

add_executable(${PROJECT_NAME} ${SOURCE_FILES})
target_include_directories(${PROJECT_NAME} PUBLIC ${LIB_INCLUDE})
target_link_libraries(${PROJECT_NAME} ${LIB_LINK})
