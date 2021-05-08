cd Documents/AtCoder
git add *.py
git add *.cpp
git status
read -p "y/n? -> " res
if [ "$res" = "y" ]; then
	read -p "if U have comment -> " comment
	if [ -z "$comment" ]; then
	    comment="daily mission"
	fi
	git commit -m "${comment}"
	git push origin master
fi
