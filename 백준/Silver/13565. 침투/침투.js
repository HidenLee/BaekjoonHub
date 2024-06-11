const fs = require('fs');

// 입력 파일 읽기
const input = fs.readFileSync('/dev/stdin', 'utf8').trim().split('\n');

// 첫 줄 입력: N과 M
const [N, M] = input[0].split(' ').map(Number);

// 그리드 생성
const grid = input.slice(1).map(line => line.split('').map(Number));

const dfs = (x, y) => {
    const stack = [[x, y]]; // 시작 좌표
    const directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]; // 상하좌우 방향

    while (stack.length > 0) {
        const [currentX, currentY] = stack.pop(); // 현재 위치 스택에서 pop

        for (const [directionX, directionY] of directions) {
            const newX = currentX + directionX; // 현재 위치에 방향 좌표 더해 이동 좌표 계산
            const newY = currentY + directionY;

            if (newX >= 0 && newX < N && newY >= 0 && newY < M && grid[newX][newY] === 0) {
                grid[newX][newY] = -1; // 이동 표시
                stack.push([newX, newY]); // 스택에 push

                if (newX === N-1) {
                    return true; // 마지막 행에 도달
                }
            }
        }
    }
    return false;
};
let canReach = false;

for (let i = 0; i < M; i++) { 
    if (grid[0][i] === 0) { 
        grid[0][i] = -1; 
        if (dfs(0, i)) { 
            canReach = true;
            break;
        }
    }
}


if (canReach) {
    console.log("YES");
} else {
    console.log("NO"); 
}