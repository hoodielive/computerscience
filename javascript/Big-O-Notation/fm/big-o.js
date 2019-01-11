function crossAdd(input) {
    let answer = [];
    for (let i = 0; i < input.length; i++) {
        let goingUp = input[i]; 
        let goingDown = input[input.length-1-i]; 
        answer.push(goingUp + goingDown); 
    }
    return answer; 
} 

crossAdd(47); 
