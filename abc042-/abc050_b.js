function main(input) {
    let [N, T, M] = input.split('\n').slice(0, 3);
    N = parseInt(N), M = parseInt(M);
    T = T.split(' ').map(v => parseInt(v));
    let PX = input.split('\n').slice(3, 3 + M);
    for (let i = 0; i < M; i++){
        PX[i] = PX[i].split(' ').map(v => parseInt(v));
    }

    let sum_t = T.reduce((i, j) => i + j, 0);
    for (let i = 0; i < M; i++){
        let [p, x] = PX[i];
        let ans = sum_t - T[p-1] + x;
        console.log(ans);
    }
    return 0;
}

main(require('fs').readFileSync('/dev/stdin', 'utf8'));
