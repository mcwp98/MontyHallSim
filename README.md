# MontyHallSim
A simulator for the classic Monty-Hall problem.

## The Problem
You are on the television show "Let's Make a Deal" and are shown three doors. Behind two of the doors, there are goats. Behind one, there is a shiny new (insert favorite car here)(that's an BMW M4 for me). You choose one of the three doors. The host of the show then reveals one of the other doors to be a goat. There are now only two doors remaining, and the host gives you the chance to change your pick. Do you do it? The aim of this simulator is to prove that switching will afford you a higher probability of winning.

## Installation

### Python
Python can be downloaded and installed to your system from https://www.python.org/. Currently, the MontyHallSim.py only works with Python 2.x installations. Support for Python 3.x is forthcoming.

### Dependencies
The MontyHallSim requires the package argsparse. This may be installed using easy_install or pip:
'''
	easy_install argparse
'''

## Usage

### Running
In order to run this file, simply navigate to the folder containing MontyHallSim.py and enter:
'''
	python MontyHallSim.py
'''

### Arguments
The Monty Hall Sim comes with several options which can be utilized through command line arguments.
'''
	usage: MontyHallSim.py [-h] [-d int] [-t int] [-v] [-p]
	
	A program to simulate the counter-intuitive statistics of the Monty-Hall problem.
	
	optional arguments:
		-h, --help			  show this help message and exit
		-d int, --doors int   designate the number of doors
		-t int, --trials int  designate the number of trials to run
		-v, --verbose		  display the details of each trials
		-p, --play			  play the game manually - only one trial will be run
'''

By default, the Monty Hall Sim will run a simulation with 3 doors and 10,000 trials.  However, these parameters can be changed. For example, to run a simulation with 100 doors and 40 trials:
'''
	python MontyHallSim.py -d 100 -t 40
'''

To display the verbose version of a simulation, use the -v flag:
'''
	python MontyHallSim.py -v
'''

The simulator can be run single-game style using the -p flag. When using this option, you can still designate how many doors you would like.  However, there is no option to select the number of trials and this option does not have a verbose option.  For example, the following will allow you to play through the game once with 44 doors:
'''
	python MontyHallSim.py -p -d 44
'''