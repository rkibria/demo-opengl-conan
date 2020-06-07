#include <iostream>
#include <stdlib.h>

#define GLEW_STATIC
#include <GL/glew.h>
#include <GLFW/glfw3.h>

int main(int argc, char **argv)
{
	GLFWwindow *window;
	if (!glfwInit()) {
		exit(EXIT_FAILURE);
	}

	window = glfwCreateWindow(1024, 768, "hello world", nullptr, nullptr);
	if (!window) {
		glfwTerminate();
		exit(EXIT_FAILURE);
	}
	glfwMakeContextCurrent(window);

	const auto version = glGetString(GL_VERSION);
	std::cout << "OpenGL version: " << version << std::endl;

	return 0;
}
