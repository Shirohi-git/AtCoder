sh ../../secret/s_AtCoder/login.sh

problem_name=$1
test_dir=${problem_name}
base_url=${problem_name%_*}
url=https://atcoder.jp/contests/${base_url}/tasks/${problem_name}

# make test directory
if [ ! -e ${test_dir} ]; then
    oj dl -d ${problem_name} $url
fi

g++-10 ${problem_name}.cpp -o ${problem_name}.out
oj t -c "./${problem_name}.out" -d ${problem_name}
