function TEST(){
    num=$1
    cargo run --release --bin tester ./ahc008_a.py < in/${num}.txt > out/${num}out.txt
}

read -p "num or all? -> " res

if [ "$res" = "all" ]; then
    for idx in {0000..0099};
        do 
        num="0000${idx}"
        TEST ${num: -4}
        echo "^"${num: -4}
        done
else
    TEST ${res}
fi
