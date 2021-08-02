function main(input) {
    let s = input;
    s = s.split(',').join(' ')
    console.log(s);
    return 0;
}

main(require('fs').readFileSync('/dev/stdin', 'utf8'));
