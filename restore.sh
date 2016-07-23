#!/bin/bash

string=`find .git/objects -type f` >& /dev/null
#echo $string
almost_result=${string//.git/}
almost_result=${almost_result//objects//}
almost_result=${almost_result////}
#echo $almost_result
for sha in $almost_result
do
file_type=`git cat-file -t $sha`
#echo $file_type
if [ $file_type != 'tree' ]; then
	clear
	echo "$sha " && git cat-file -p $sha
	echo
	echo "Add file to index?"
	read answer
	if [ $answer == 'y' ]; then
		echo
		echo "Input name:"
		read name
		git update-index --add --cacheinfo 100644 $sha $name
		git checkout -- $name
		git add $name
	fi
fi
done
