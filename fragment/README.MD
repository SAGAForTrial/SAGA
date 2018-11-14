

### Environment

- CUDA 9.0
- jdk 1.8
- at least 6G graphic memory  (for 100 000 000 tokens)
- Windows 



### Run

run the pipeline.bat.

It would execute our tool, then run the group2pair.py .



```bat
java -jar SAGA.jar F:\\bcb_reduced 0.7 50 20 100000000
```

DatasetDirPath    Threshold	LMC	LMCC	TokenSeq      Unit (in 6G graphic memory)

F:\\bcb_reduced    0.7    		50    	 20   	      100000000





### Result

This is a fragment-version of SAGA tool, which will process a java source code folder,
and produce two result file.
File named `Result_type1&2.csv` contains the clone fragment that is type1 or type2.
Another file named `Result_type3.csv` contains the clone fragment that is type3.