# CurrentToConductivity



I continued my progress from the last time and I took the metadata generated in TkinterPandasGUI scripts and generated dataframes from the raw data.

After that, linear regression was calculated for each dataframe to get the current of specific membrane potential points for all cells.

After that, the current was subtracted from the membrane potential for all the current dataframes. The result was divided by the specific Volt at each point minus the Nernst potential of potassium.

I fetched the result as 4 graphs. one of the graphs is the conductivity graph of the membrane to potassium at any moment in time.

Last Commit = "Normalized" Actually what I made is to divide all the DataFrame by the highest vaulu of the highest voltage to get normalized results for all the DataFrame between 0-1
