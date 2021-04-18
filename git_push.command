cd Documents/AtCoder
git add *.py
git status
read comment
if [ -z "$comment" ]; then
    comment="daily mission"
fi
git commit -m "${comment}"
git push origin master
