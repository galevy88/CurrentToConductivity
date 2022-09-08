# CurrentToConductivity


With continuation of my progress from last time I took the meta data was generated in TkinterPandasGUI scripts and generated dataframes from the raw data.

After it, I took the dataframes and calculate linear regression of a specifc moment on time in order to get the current of specific membrane potential points for all cells.

After it, I substract the current of the membrane potential from the current dataframe and divide the result by the specific Volt at each point minus the nernst potential of potassium.

I fetched the result as 4 graph that one of the is the conductivity graph of the membrane to potassium at any moment on time.
