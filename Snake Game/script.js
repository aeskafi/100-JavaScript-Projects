
    const canvas = document.getElementById('snakeCanvas');
    const ctx = canvas.getContext('2d');
    const scoreEl = document.getElementById('snakeScore');
    const restartBtn = document.getElementById('snakeRestart');

    const grid = 15;
    let snake = [{x: 150, y: 150}];
    let dx = grid;
    let dy = 0;
    let food = {x: 60, y: 60};
    let score = 0;
    let loop = null;

    function randomFood() {
        food.x = Math.floor(Math.random() * (canvas.width / grid)) * grid;
        food.y = Math.floor(Math.random() * (canvas.height / grid)) * grid;
    }

    function update() {
        const head = {x: snake[0].x + dx, y: snake[0].y + dy};

        // Wall collision wrap
        if (head.x < 0) head.x = canvas.width - grid;
        if (head.x >= canvas.width) head.x = 0;
        if (head.y < 0) head.y = canvas.height - grid;
        if (head.y >= canvas.height) head.y = 0;

        // Self collision
        for (let i = 1; i < snake.length; i++) {
            if (head.x === snake[i].x && head.y === snake[i].y) {
                clearInterval(loop);
                alert(`Game Over! Score: ${score}`);
                return;
            }
        }

        snake.unshift(head);

        if (head.x === food.x && head.y === food.y) {
            score += 10;
            scoreEl.innerText = score;
            randomFood();
        } else {
            snake.pop();
        }

        ctx.fillStyle = '#0f172a';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        ctx.fillStyle = '#ec4899';
        ctx.fillRect(food.x, food.y, grid - 1, grid - 1);

        ctx.fillStyle = '#06b6d4';
        snake.forEach(part => ctx.fillRect(part.x, part.y, grid - 1, grid - 1));
    }

    window.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowUp' && dy === 0) { dx = 0; dy = -grid; }
        if (e.key === 'ArrowDown' && dy === 0) { dx = 0; dy = grid; }
        if (e.key === 'ArrowLeft' && dx === 0) { dx = -grid; dy = 0; }
        if (e.key === 'ArrowRight' && dx === 0) { dx = grid; dy = 0; }
    });

    restartBtn.addEventListener('click', () => {
        clearInterval(loop);
        snake = [{x: 150, y: 150}];
        dx = grid; dy = 0;
        score = 0;
        scoreEl.innerText = '0';
        randomFood();
        loop = setInterval(update, 100);
    });
    