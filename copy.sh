#!/bin/bash

template="blog_"
dir="mysite/blog/"


tocopy=`find . -maxdepth 1 -name "*$template*" -print` >& /dev/null
#echo $tocopy
for file in $tocopy
do
#echo $file
file=${file/.\//}
#echo $file
cp $file $dir
tofile=${file/$template/}
mv $dir$file $dir$tofile
#echo $tofile
done
