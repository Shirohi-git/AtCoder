function main(input) {
    let [a, b, c, d] = input.split(' ');

    let ans = Math.max(a * b, c * d);
    console.log(ans);
    return 0;
}

main(require('fs').readFileSync('/dev/stdin', 'utf8'));
