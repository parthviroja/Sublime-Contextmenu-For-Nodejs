import os
import sublime
import subprocess
import sublime_plugin
import time
from threading import Thread

class RunTerminalCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		path = self.view.file_name().split("\\")
		#current_driver = path[0]
		file = path.pop()
		current_directory="\\".join(path)
		cmd = ['cmd']
		thread = subprocess.Popen(cmd,shell=False,cwd=current_directory)
		thread.daemon = True

class RunNodeCommand(sublime_plugin.TextCommand,):
	def run(self, edit):
		path = self.view.file_name().split("\\")
		current_driver = path[0]
		file = path.pop()
		current_directory="\\".join(path)
		ext = file.split(".")
		extension = ext.pop()
		# command = "cd "+ current_directory + " & node " + file +" & start cmd"
		# os.system(command);
		if(extension == "js" or extension == "json"):
			#print(current_directory)
			cmd = ['cmd','/k node ' + self.view.file_name()]
			# p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, creationflags=subprocess.SW_HIDE)
			thread = subprocess.Popen(cmd,shell=False,cwd=current_directory)
			thread.daemon = True

class RunNodemonCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		path = self.view.file_name().split("\\")
		current_driver = path[0]
		file = path.pop()
		current_directory="\\".join(path)
		ext = file.split(".")
		extension = ext.pop()
		# command = "cd "+ current_directory + " & nodemon " + file +" & start cmd"
		# os.system(command);
		if(extension == "js"):
			print(current_directory)
			cmd = ['cmd','/k nodemon ' + self.view.file_name()]
			# p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, creationflags=subprocess.SW_HIDE)
			thread = subprocess.Popen(cmd,shell=False,cwd=current_directory)
			thread.daemon = True

class RunNwCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		path = self.view.file_name().split("\\")
		current_driver = path[0]
		file = path.pop()
		current_directory="\\".join(path)
		ext = file.split(".")
		extension = ext.pop()
		# command = "cd "+ current_directory + " & nodemon " + file +" & start cmd"
		# os.system(command);
		#if(extension == "json"):
		print(current_directory)
		cmd = ['cmd','/k nw.exe . --enable-transparent-visuals --force-cpu-draw']
		# p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, creationflags=subprocess.SW_HIDE)
		thread = subprocess.Popen(cmd,shell=False,cwd=current_directory)
		thread.daemon = False

class RunGruntCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		path = self.view.file_name().split("\\")
		current_driver = path[0]
		file = path.pop()
		current_directory="\\".join(path)
		ext = file.split(".")
		extension = ext.pop()
		# command = "cd "+ current_directory + " & nodemon " + file +" & start cmd"
		# os.system(command);
		if(extension == "js"):
			print(current_directory)
			cmd = ['cmd','/k grunt']
			# p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, creationflags=subprocess.SW_HIDE)
			thread = subprocess.Popen(cmd,shell=False,cwd=current_directory)
			thread.daemon = True

class RunMongoCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		cmd = ['cmd','/k mongod --bind_ip=localhost --dbpath=c:\mongo-data\db --rest'] # set you mongodb database path
		thread = subprocess.Popen(cmd,shell=False)
		thread.daemon = True

class RunJsonServerCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		path = self.view.file_name().split("\\")
		current_driver = path[0]
		file = path.pop()
		current_directory="\\".join(path)
		ext = file.split(".")
		extension = ext.pop()
		# command = "cd "+ current_directory + " & nodemon " + file +" & start cmd"
		# os.system(command);
		if(extension == "json"):
			print(current_directory)
			cmd = ['cmd','/k json-server --watch ' + self.view.file_name()]
			# p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, creationflags=subprocess.SW_HIDE)
			thread = subprocess.Popen(cmd,shell=False,cwd=current_directory)
			thread.daemon = True

class RunNotepadCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		cmd = ['notepad.exe',self.view.file_name()]
		thread = subprocess.Popen(cmd,shell=False)
		thread.daemon = True