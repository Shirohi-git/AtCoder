sh ../../secret/s_AtCoder/login.sh

problem_name=$1
base_url=${problem_name%_*}
url=https://atcoder.jp/contests/${base_url}/tasks/${problem_name}

#oj s --wait=0 $url "${problem_name}.py"
#oj s --wait=0 $url "${problem_name}.py" -l 4047 #PyPy3
#oj s --wait=0 --yes $url "${problem_name}.py"
#
oj s --wait=0 --yes $url "${problem_name}.py" -l 4047 #PyPy3
