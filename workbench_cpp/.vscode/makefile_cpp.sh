read name
if [ `echo ${name} | grep '_'` ]; then
    cp .vscode/original.cpp ${name}.cpp
    code ${name}.cpp
else
    cp .vscode/original.cpp ${name}_a.cpp
    cp .vscode/original.cpp ${name}_b.cpp
    cp .vscode/original.cpp ${name}_c.cpp
    cp .vscode/original.cpp ${name}_d.cpp
    cp .vscode/original.cpp ${name}_e.cpp
    code ${name}_a.cpp
fi
