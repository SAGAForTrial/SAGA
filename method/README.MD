

### Environment

- CUDA 9.0
- jdk 1.8
- python3 (group2pair.py needs python3 transforming clone_class_format to clone_pair_format )
- at least 6G graphic memory  (for 100 000 000 tokens)
- Windows



### Run

If you don't configure, just run `java -jar SAGA.jar code_dictory_path`



If configuration, do as follow :  

```bat
java -jar SAGA.jar F:\\bcb_reduced 0.7 50 20 100000000
python group2pair.py
```

There is also a sample bat script `pipeline.bat`

DatasetDirPath    Threshold	LMC	LMCC	     TokenSeq Unit (in 6G graphic memory)

F:\\bcb_reduced    0.7    		50    	 20   	      100000000





### Result

It would generate a result.csv file containing clone result.

The format of result.csv is for bigclonebench.