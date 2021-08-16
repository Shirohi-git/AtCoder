function main(input) {
    let x = parseInt(input);

    if (x < 1200)
        console.log("ABC");
    else
        console.log("ARC");
    return 0;
}

Input = require('fs').readFileSync('/dev/stdin', 'utf8')
main(Input);
