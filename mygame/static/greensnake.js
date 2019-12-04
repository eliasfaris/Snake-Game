const cvs = document.getElementById("snake");
const ctx = cvs.getContext("2d");


// create the unit
const box = 32;

// load images

const ground = new Image();
ground.src = "/static/gameboard.png";



// create the snake
//snake must be an array in order to track the amount of food & if hit itself
let snake = [];

//make the head of the snake
snake[0] = {
    x : 10 * box ,
    y : 10 * box
};

// create the food
let food = {
    //randomize the food around the play board
    x : Math.floor(Math.random()*17+1) * box,
    y : Math.floor(Math.random()*15+3) * box
}

// create the score to keep track
let score = 0;

//variable in order to check if the opposite direction was played previously
let d;

document.addEventListener("keydown",direction);
//snake movement with the arrow keys on the keyboard
function direction(event){
    let key = event.keyCode;
    if( key == 37 && d != "RIGHT"){
        d = "LEFT";
    }else if(key == 38 && d != "DOWN"){
        d = "UP";
    }else if(key == 39 && d != "LEFT"){
        d = "RIGHT";
    }else if(key == 40 && d != "UP"){
        d = "DOWN";
    }
}


// check collision function
function collision(head,array){
  //traverse the snake body to see if the snake hit itself
    for(let i = 0; i < array.length; i++){
        if(head.x == array[i].x && head.y == array[i].y){
            return true;
        }
    }
    return false;
}


// draw everything to the canvas
function draw(){

    ctx.drawImage(ground,0,0);

    for( let i = 0; i < snake.length ; i++){
        ctx.fillStyle = ( i == 0 )? "#25D943" : "green";
        ctx.fillRect(snake[i].x,snake[i].y,box,box);

        //places a border around each snake body for more aesthetics
        ctx.strokeStyle = "black";
        ctx.strokeRect(snake[i].x,snake[i].y,box,box);
    }

    //color in the food
    ctx.fillStyle = "blue";
    ctx.fillRect(food.x, food.y, 32, 32);

    //ctx.rect(food.x,food.y, 32, 32);
    //ctx.fillStyle= "red";
    //ctx.strokeStyle = "red";
    //ctx.stroke();

    //draw the food on the canvas
    //ctx.drawImage(foodImg, food.x, food.y);

    // old head position
    let snakeX = snake[0].x;
    let snakeY = snake[0].y;

    // checks the direction
    if( d == "LEFT")
        snakeX -= box;
    if( d == "UP")
        snakeY -= box;
    if( d == "RIGHT")
        snakeX += box;
    if( d == "DOWN")
        snakeY += box;

    // if the snake eats the food
    if(snakeX == food.x && snakeY == food.y){
        score++;
        food = {
            x : Math.floor(Math.random()*17+1) * box,
            y : Math.floor(Math.random()*15+3) * box
                }
        // we don't remove the tail
    }
    else{
        // remove the tail
        snake.pop();
    }

    // add new Head

    let newHead = {
        x : snakeX,
        y : snakeY
    }

    // game over
    //the gameboard is 544x544 px, therefore
    if(snakeX < box || snakeX > 17 * box || snakeY < 3 * box || snakeY > 17 * box || collision(newHead,snake)){
        clearInterval(game); //stops the frames from continuing to show that it is game over
        localStorage.setItem("points",score);

        $.post( "/postmethod1",
        {
        point: score
        }, function(err, req, resp){
            //window.location.href = "/leaderboard";
        // if you want to redirect after you get a response
        // remove this function if you do not need to do anything in response.
        });
        window.location.href = "leaderboard";
    }



    snake.unshift(newHead);

    ctx.fillStyle = "white";
    ctx.font = "45px Saira Stencil One";
    ctx.fillText(score,16*box,1.6*box);
}

// call draw function every 100 ms. This is the speed of the snake
let game = setInterval(draw,125);
