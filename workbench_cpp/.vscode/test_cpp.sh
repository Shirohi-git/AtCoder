sh ../../secret/s_AtCoder/login.sh

problem_name=$1
test_dir=../w_sample_test
base_url=${problem_name%_*}
url=https://atcoder.jp/contests/${base_url}/tasks/${problem_name}

# make test directory
if [ ! -e ${test_dir}/${problem_name} ]; then
    oj dl -d ${test_dir}/${problem_name} $url
fi

g++-10 -std=gnu++17 ${problem_name}.cpp -o ${test_dir}/${problem_name}.out
oj t -N -c "${test_dir}/${problem_name}.out" -d ${test_dir}/${problem_name}
