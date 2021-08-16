function main(input) {
    let s = input;
    let n = s.length;
    
    let p = 0, q = 0;
    for (let i = 0; i < n; i++){
        if (s[i] == 'Z') p = i + 1;
    }
    for (let i = n - 1; i >= 0; i--){
        if (s[i] == 'A') q = i;
    }
    console.log(p - q);
    return 0;
}

main(require('fs').readFileSync('/dev/stdin', 'utf8'));
