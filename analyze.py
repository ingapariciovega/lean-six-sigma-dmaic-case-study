from pathlib import Path
from statistics import mean, median, stdev
import json

def summarize(data):
    before,after=data['baseline'],data['illustrative_after']
    for series in [before,after]:
        if len(series)<2 or any(not isinstance(v,(int,float)) or not 0<v<1e9 for v in series):
            raise ValueError('At least two positive finite observations per phase are required.')
    a,b=mean(before),mean(after)
    return {'synthetic_example':True,'baseline_n':len(before),'after_n':len(after),'baseline_mean_min':a,'after_mean_min':b,'baseline_median_min':median(before),'after_median_min':median(after),'baseline_sample_sd_min':stdev(before),'after_sample_sd_min':stdev(after),'difference_min':a-b,'relative_reduction_percent':(a-b)/a*100,'interpretation':'Descriptive comparison only; no proof of causality, sustained control or real savings.'}

if __name__=='__main__':
    print(json.dumps(summarize(json.loads(Path(__file__).with_name('sample-data.json').read_text())),indent=2))
