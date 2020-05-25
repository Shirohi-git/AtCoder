sh ../../secret/s_AtCoder/login.sh

problem_name=$1
test_dir=test/${problem_name}
base_url=${problem_name%_*}
url=https://atcoder.jp/contests/${base_url}/tasks/${problem_name}

# make test directory
if [ ! -e ${test_dir} ]; then
    oj dl -d test/${problem_name} $url
fi

oj test -c "python3 ${problem_name}.py" -d test/${problem_name}