function main(input) {
    let [a, b] = input.split(' ').map(v => parseInt(v));
    if (a == 1) a += 13;
    if (b == 1) b += 13;

    let ans = '';
    if (a > b) {
        ans = "Alice";
    } else if (b > a) {
        ans = "Bob";
    } else {
        ans = "Draw";
    }
    console.log(ans);
    return 0;
}

main(require('fs').readFileSync('/dev/stdin', 'utf8'));
