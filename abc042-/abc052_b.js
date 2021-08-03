function main(input) {
    let [n, s] = input.split('\n');
    n = parseInt(n);

    let ans = 0, x = 0;
    for (let i = 0; i < n; i++){
        if (s[i] == 'I') x += 1;
        if (s[i] == 'D') x -= 1;
        ans = Math.max(ans, x);
    }
    console.log(ans);
    return 0;
}

main(require('fs').readFileSync('/dev/stdin', 'utf8'));
