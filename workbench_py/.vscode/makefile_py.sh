read name
if [ `echo ${name} | grep '_'` ]; then
    cp .vscode/original.py ${name}.py
    code ${name}.py
else
    cp .vscode/original.py ${name}_a.py
    cp .vscode/original.py ${name}_b.py
    cp .vscode/original.py ${name}_c.py
    cp .vscode/original.py ${name}_d.py
    cp .vscode/original.py ${name}_e.py
    code ${name}_a.py
fi
