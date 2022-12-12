// let width = 600
// let height = 400


let width = 1700
let height = 880

let s = 10

let w = width /s
let h = height / s

let life = []

function setup() {
    let c = createCanvas(width, height);
    // console.log( w, h );
    frameRate(15);

    saveCanvas(c, 'myCanvas', 'jpg');

    for(let i = 0 ; i < w ; i++){
        let f = []
        for(let j = 0 ; j < h ; j++){
            n = random(0 , 100)
            if(n < 10){
                f.push(new cell(i , j , s , w , h ,  true));            
            }
            else{
                f.push(new cell(i , j , s , w , h ,  false));             

            }
        }
        life.push(f);
    }
}   

function draw() {
    background(0);


    for(let i = 0 ; i < w ; i++){
        for(let j = 0 ; j < h ; j++){
            life[i][j].make();
            life[i][j].add_neibour(life);
        }
    }

    for(let i = 0 ; i < w ; i++){
        for(let j = 0 ; j < h ; j++){
            
            if(life[i][j].Alive){
                life[i][j].stay = true;
            }
            else{
                life[i][j].stay = false;
            }

        }
    }   
}

function keyPressed() {
    if(key == " "){
        saveGif("GameofLife.gif" , 5 );
    }
}