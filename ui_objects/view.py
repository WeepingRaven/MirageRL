
class View:
	"""Class handling data and behaviour of views.

		View contains everything that visible on screen - it is the screen.
		It has one or more consoles.
	"""
	def __init__(self, name, main_con, render_func, root_console, *args, **kwargs):

		self.name = name
		self.main_con = main_con
		self.render_func = render_func
		self.root_console = root_console
		self.args = args
		self.kwargs = kwargs
		self.consoles = {self.name: (self.main_con, self.render_func)}
		self.menus = dict()


	def render(self, *args):

		# iterate over dict

		self.render_func(self.main_con, self.root_console, *self.args)


	def add_console(self, name, func, *func_args):
		"""Adds console to display additional content."""
		pass



		