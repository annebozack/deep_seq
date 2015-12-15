source /nfs/apps/qiime/1.9.1/activate.sh
join_paired_ends.py -f daisy-11-0-0_13s006145-1-1_lane5.screened.adapter.screened.hg19.pair.1.fq.gz -r daisy-11-0-0_13s006145-1-1_lane5.screened.adapter.screened.hg19.pair.2.fq.gz -o lane1
join_paired_ends.py -f daisy-11-0-0_13s006145-2-1_lane6.screened.adapter.screened.hg19.pair.1.fq.gz -r daisy-11-0-0_13s006145-2-1_lane6.screened.adapter.screened.hg19.pair.2.fq.gz -o lane2
join_paired_ends.py -f daisy-11-0-0_13s006145-3-1_lane7.screened.adapter.screened.hg19.pair.1.fq.gz -r daisy-11-0-0_13s006145-3-1_lane7.screened.adapter.screened.hg19.pair.2.fq.gz -o lane3
join_paired_ends.py -f daisy-11-0-0_13s006145-4-1_lane8.screened.adapter.screened.hg19.pair.1.fq.gz -r daisy-11-0-0_13s006145-4-1_lane8.screened.adapter.screened.hg19.pair.2.fq.gz -o lane5
cat lane1/fastqjoin.join.fastq lane2/fastqjoin.join.fastq lane3/fastqjoin.join.fastq lane5/fastqjoin.join.fastq > daisy0_join.fastq
gzip daisy0_join.fastq








