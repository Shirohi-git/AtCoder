function main(input) {
    let [n, a] = input.split('\n');
    n = parseInt(n);
    a = a.split(' ').map(v => parseInt(v));
    a.sort(function (x, y) { return x - y; });

    let ans = 'Yes';
    for (let i = 0; i < n; i++) { if (a[i] != i + 1) ans = 'No'; }

    console.log(ans);
    return 0;
}

main(require('fs').readFileSync('/dev/stdin', 'utf8'));
