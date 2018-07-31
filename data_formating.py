import pandas as pd;
import os;
import sys;
import datetime;
import numpy as np;

def groupby_geohash_weekday_csv(path_to_file):
	opened_file=open(path_to_file);
	dict_data={};
	totals={};
	lines_parsed=0;
	for _ in opened_file:
		lines_parsed+=1;
		if lines_parsed%1000000==0:
			print('{} lines parsed'.format(lines_parsed));
		sp=_.split('\t');
		weekday=datetime.datetime(int(sp[1]),int(sp[2]),int(sp[3])).weekday();
		key=tuple([sp[0][0:8],weekday,sp[4]]);
		if key in dict_data:
			dict_data[key]=dict_data[key]+1;
		else:
			dict_data[key]=1;

		if sp[0] in totals:
			totals[sp[0]]=totals[sp[0]]+1;
		else:
			totals[sp[0]]=1;

def groupby_geohash_weekday_matrix(path_to_file,target_folder):
	opened_file=open(path_to_file);
	dict_data={};

	lines_parsed=0;
	for _ in opened_file:
		lines_parsed+=1;
		if lines_parsed%1000000==0:
			print('{} lines parsed'.format(lines_parsed));
		
		sp=_.split('\t');
		key=sp[0][0:6];
		weekday=datetime.datetime(int(sp[1]),int(sp[2]),int(sp[3])).weekday();
		hour_=int(sp[4]);
		if key in dict_data:
			dict_data[key][weekday,hour_]+=1;
		else:
		    dict_data[key]=np.zeros([7,24]);
		    dict_data[key][weekday,hour_]+=1;

	for _ in dict_data:
		np.savetxt(target_folder+"/{}".format(_),dict_data[_],delimiter=',',fmt='%.1e');

	return 0;


def main():
    if len(sys.argv)>3:
        print('Incorrect input format ');
        return;
    script = sys.argv[0];
    groupby_geohash_weekday_matrix(sys.argv[1],sys.argv[2]);


main();