#!/usr/bin/python

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

txt_file = "bench_results.txt"
csv_file = "myresults.csv"

def parse_bench(txt_file):
    cufftbench = []
    crnt_batch = 0;
    idx_row = -1

    names = ["fft_size", "batch_size", "time", "gflops"]
    
    with open(txt_file) as f:
        for line in f:
            lst = line.split()
            if("xsize:" in lst):
                idx = lst.index("xsize:")
                lst = line.split()
                size = int(lst[idx + 1])
            if("batch:" in lst):
                idx = lst.index("batch:")
                batch = int(lst[idx + 1])
                if(batch != crnt_batch):
                    crnt_batch = batch
                    idx_row += 1
                    cufftbench.append([size, batch])
            if(("time:" in lst) and ("plan" not in lst) and ("reference" not in lst)):
                idx = lst.index("time:")
                time = float(lst[idx + 1])
                cufftbench[idx_row].append(time)
            if(("gflops:" in lst) and ("reference" not in line)):
                idx = lst.index("gflops:")
                gflops = float(lst[idx + 1])
                cufftbench[idx_row].append(gflops)
    f.closed

    df = pd.DataFrame(cufftbench, columns=names)
    df.dropna(inplace=True)
    return df

def parse_2dresults(csv_file):
    names = ["fft_size", "batch_size", "time", "gflops"]
    df = pd.read_csv(csv_file,  header = None, names = names) 
    return df;

def plot(df1, df2, metric):
    fft_sizes = df1["fft_size"].unique()

    fig, axes = plt.subplots(nrows = len(fft_sizes), ncols = 1, figsize=(10, 8))

    #plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
    plt.tight_layout()
    
    idx = 0

    for fft_size in fft_sizes:
        row1 = (df1["fft_size"] == fft_size)
        row2 = (df2["fft_size"] == fft_size)
        
        batch_size = df1[row1]["batch_size"]
        
        mtr1 = df1[row1][metric]
        mtr2 = df2[row2][metric]
        
        axes[idx].loglog(batch_size, mtr1, color="purple", lw=1, ls='-', marker='o', markersize=6, 
            label="2d-kernel")

        axes[idx].loglog(batch_size, mtr2, color="green", lw=1, ls='-', marker='d', markersize=6, 
            label="2 1d-kernel")

        if(metric == "time"):
            axes[idx].set_ylabel("elapsed time (ms)")
        else:
            axes[idx].set_ylabel("gflops")

        axes[idx].legend(loc=2)
        axes[idx].grid(True)
        axes[idx].set_title("fftsize={:d}x{:d}".format(fft_size, fft_size))

        idx += 1
        
        if(metric == "time"):
           plt.savefig(metric + ".jpg", bbox_inches="tight")
        else:
           plt.savefig(metric + ".jpg", bbox_inches="tight")

if __name__== "__main__":
    df_bench    = parse_bench(txt_file)
    df_2dkernel = parse_2dresults(csv_file)
    
    plot(df_2dkernel, df_bench, "gflops")
    plot(df_2dkernel, df_bench, "time")

    plt.show()
