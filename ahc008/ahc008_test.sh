function TEST(){
    num=$1
    cargo run --release --bin tester ./ahc008_a.py < in/${num}.txt > out/${num}out.txt 2>> score.txt
}

read -p "num or all? -> " res
: > score.txt

if [ "$res" = "all" ]; then
    for idx in {0000..0010};
    do 
        num="0000${idx}"
        TEST ${num: -4}
        echo "^"${num: -4} >> score.txt
        echo "^"${num: -4}
    done
else
    TEST ${res}
fi

python3 sumcalc.py
