################################################################
####    Ryan McArdle
####    10 Sept. 2020
####   
####    Creates a weather_wrapper class which is able to read, 
####    describe, and plot data provided as a .csv file from 
####	the Florida Automated Weather Network. Returns 
####	statistics about an attribute to the command line and 
####	log file and plots the timeseries data in matplotlib 
####	without clutter. Intended to familiarize students with 
####	Pandas and data management.
####
################################################################

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
import sys
import os 


class weather_wrapper:
	""" Reads, describes, and plots data provided as a .csv 
		file from the Florida Automated Weather Network."""



	def read(self, input_file):
		""" 
		Converts the input .csv file into a Pandas DataFrame
		to prepare for processing.
		
		:param input_file: the relative location of a Florida 
			Automated Weather Network .csv file.
		"""


		try:
			self.data_set = pd.read_csv(input_file)
		except:
			print("weather_wrapper.read() can only accept .csv files as input!")


	def describe(self, start, end, attribute, statistics = ['min','mean','max','std']):
		""" 
		Returns a DataFrame containing the minimum, maximum, 
		mean, and std. dev. of variable for each date from the 
		start to the end dates. 
		
		:param start: a datetime string of the form 
			'YYYY-mm-dd HH:MM:SS' indicating the start of the 
			time period.
		:param end: a datetime string of the same form 
			indicating the end of the time period.
		:param attribute: the column of the .csv that we wish 
			to plot.
		:return: the DataFrame with the relevant statistics.
		"""


		## For convenience
		local_time = 'local_eastern_time'

		## Converts start and end time stamps to datetime.
		start_dt = pd.to_datetime(start)
		end_dt = pd.to_datetime(end)

		## Uses a mask to return only the needed time-stamps. 
		date_mask = (pd.to_datetime(self.data_set[local_time]) >= start_dt) & (pd.to_datetime(self.data_set[local_time]) <= end_dt)
		return_frame = self.data_set[date_mask]	

		## Groups data by day and returns a data frame of the 
		## min, max, mean, and std. dev. of the given variable.
		return_frame = return_frame.groupby('day', as_index=True)[attribute].agg(statistics)

		## Prints data frame to an output file.
		output_file = 'output.txt'
		with open(output_file, 'w') as f:
			orig_out = sys.stdout
			sys.stdout = f
			print(return_frame)
			sys.stdout = orig_out

		return return_frame


	def plot(self, start, end, attribute):
		""" 
		Plots the values of the given attribute from start to 
			end. 

		:param start: a datetime string of the form 
			'YYYY-mm-dd HH:MM:SS' indicating the start of the 
			time period.
		:param end: a datetime string of the same form 
			indicating the end of the time period.
		:param variable: the attribute or column of the .csv 
			that we wish to plot.
		"""


		## For convenience.
		local_time = "local_eastern_time"

		## Creates datetime items out of the input strings.
		start_time = pd.to_datetime(start)
		end_time = pd.to_datetime(end)

		## Creates datetime mask to selecting relevant instances.
		date_times = pd.to_datetime(self.data_set[local_time], format='%Y-%m-%d %H:%M:%S')
		date_mask = (date_times >= start_time) & (date_times <= end_time)
		plot_data = self.data_set[date_mask]

		## Creates x,y lists for plotting
		dates_in_range = pd.to_datetime(plot_data[local_time], format='%Y-%m-%d %H:%M:%S')
		data_in_range = plot_data[attribute]

		## Creates plot. 
		fig=plt.figure(figsize=(8,8))
		ax1 = fig.add_subplot(111, title=attribute, xlabel="Date")
		ax1.plot(dates_in_range,data_in_range)
		ax1.xaxis.set_major_locator(matplotlib.dates.DayLocator())
		ax1.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%Y-%m-%d'))
		
		plt.xticks(rotation=60)
		plt.tight_layout()
		plt.savefig('output_fig.png')
		plt.show()



## The assigned problem. 
def main():
	data_file = ".\weather_data_f2020.csv"
	w = weather_wrapper()
	w.read(data_file)
	df = w.describe("2018-06-06 12:59:59", "2018-06-09 12:59:59", "rfd_2m_wm2")
	print(df)
	w.plot("2018-06-06 12:59:59", "2018-06-09 12:59:59", "rfd_2m_wm2")


## The assignment example use case.
def example():
	data_file = ".\weather_data_f2020.csv"
	w = weather_wrapper()
	w.read(data_file)
	df = w.describe("2018-06-06 12:59:59", "2018-06-09 12:59:59", "temp_air_2m_C")
	print(df)
	w.plot("2018-06-06 12:59:59", "2018-06-09 12:59:59", "temp_air_2m_C")



if __name__=="__main__":
	main()
	#example()
