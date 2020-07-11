read name
{
    echo "s = input()"
    echo "n = map(int, input().split())"
    echo "a = list(map(int, input().split()))"
    echo "ab = [list(map(int, input().split())) for _ in range(n)]"
} >> ${name}_a.py
cp ${name}_a.py ${name}_b.py
cp ${name}_a.py ${name}_c.py

{
    echo "import sys"
    echo "input = sys.stdin.readline"
    echo
    echo "s = input()"
    echo "n = map(int, input().split())"
    echo "a = list(map(int, input().split()))"
    echo "ab = [list(map(int, input().split())) for _ in range(n)]"
} >> ${name}_d.py
cp ${name}_d.py ${name}_e.py
#cp ${name}_d.py ${name}_f.py