cd Documents/AtCoder
git status
read -p "y/n? -> " res
if [ "$res" = "y" ]; then
	git add *.py
	git add *.cpp
	read -p "if U have a comment -> " comment
	if [ -z "$comment" ]; then
	    comment="daily mission"
	fi
	git commit -m "${comment}"
	git push origin master
fi
