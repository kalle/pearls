#!/bin/sh

EXE=$1
SUMS="150"
DIGITS="10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29"
OUTFILE="$EXE.dat"
OUTDIR="out_$EXE"

time_run() {
    cmd=$1
    wanted_sum=$2
    digits=$3
    num_digits=$4
    echo "$wanted_sum $num_digits"
    /usr/bin/time -p ./$cmd $wanted_sum $digits 2>&1
#    t=`(/usr/bin/time -ph ./$cmd $wanted_sum $digits) 2>&1 | grep real | cut -f 2 | tr m ' ' | tr -d s`
#    echo "$wanted_sum $num_digits $t"
}

rm -rf $OUTDIR
mkdir $OUTDIR
i="0"
for s in $SUMS; do
    echo "Doing sum $s"
    for d in $DIGITS; do
        echo "  Doing digit length $d"
        for r in `cat random_$d.dat`; do
            time_run $EXE $s $r $d > $OUTDIR/$i.out &
            i=`expr $i + 1`
        done
        wait
    done
done

#cat `find $OUTDIR -type f | sort -n` > $OUTFILE
#rm -rf $OUTDIR


