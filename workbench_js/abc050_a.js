function main(input) {
    let [a, op, b] = input.split(' ');
    a = parseInt(a), b = parseInt(b);
    let ans = 0;
    if (op == '+') ans = a + b;
    if (op == '-') ans = a - b;
    console.log(ans);
    return 0;
}

main(require('fs').readFileSync('/dev/stdin', 'utf8'));
