from conans import ConanFile, CMake

class DemoOpenglConan(ConanFile):
	name = "demoopenglconan"
	version = "0.1"
	description = """OpenGL demo using conan packages"""
	homepage = "https://github.com/rkibria"
	url = "https://github.com/rkibria/demo-opengl-conan"
	license = "MIT"
	author = "Raihan Kibria"

	settings = "os", "compiler", "build_type", "arch"
	requires = (
		"glew/2.1.0@bincrafters/stable",
		"glfw/3.3.2@bincrafters/stable", )
	generators = "cmake"

	def build(self):
		cmake = CMake(self, generator="Ninja")
		cmake.configure()
		cmake.build()
