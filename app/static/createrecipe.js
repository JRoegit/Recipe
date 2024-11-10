let ingredient_index = 0
let direction_index = 0

let num_directions = 0
let num_ingredients = 0

function create_ingredient(){
    const ingredient_list = document.getElementById('ingredientlist')
    if(num_ingredients < 20){
        create_input(ingredient_list, "ingredient")
        ingredient_index += 1
        num_ingredients += 1
    }
}

function create_direction(){
    const direction_list = document.getElementById('directionlist')
    if(num_directions < 20){
        create_input(direction_list, "direction")
        direction_index += 1
        num_directions += 1
    }
}

function delete_ingredient(){
    num_ingredients -= 1
    this.parentNode.parentNode.removeChild(this.parentNode);

    const ingredient_list = document.getElementById('ingredientlist').children
        
    for(let i = 0 ; i < ingredient_list.length; i++){
        console.log(i)
        ingredient_list[i].children[0].name = `ingredient_${i}`
    }
    ingredient_index = ingredient_list.length
}

function delete_direction(){
    num_directions -= 1
    this.parentNode.parentNode.removeChild(this.parentNode);

    const direction_list = document.getElementById('directionlist').children
        
    for(let i = 0 ; i < direction_list.length; i++){
        direction_list[i].children[0].name = `direction_${i}`
    }
    direction_index = direction_list.length
}

function create_input(list,type){
    const container_div = document.createElement('div')
    container_div.classList.add("flex")

    if (type === "ingredient"){
        const input = document.createElement('input')
        input.type = "text"
        input.maxLength = "40"
        input.placeholder = type === "ingredient" ? "1 Cup Flour" : "Step #" 
        input.classList.add('w-full')
        input.name = type === "ingredient" ? `ingredient_${ingredient_index}` : `direction_${direction_index}`  
        container_div.appendChild(input)
    } else {
        const input = document.createElement('textarea')
        input.placeholder = "Step #"
        input.maxLength = "320" 
        input.classList.add('w-full')
        input.name = type === "ingredient" ? `ingredient_${ingredient_index}` : `direction_${direction_index}`  
        container_div.appendChild(input)
    }

    const delete_button = document.createElement('button')
    const delete_button_content = document.createTextNode("Remove")
    delete_button.appendChild(delete_button_content)
    delete_button.type = "button"
    delete_button.classList.add('ml-auto') 
    delete_button.classList.add('px-2')
    type === "ingredient" ? delete_button.addEventListener('click', delete_ingredient) : delete_button.addEventListener('click', delete_direction)

    container_div.appendChild(delete_button)
    list.appendChild(container_div)
}

function handle_submit(){
    const ingredient_list = document.getElementById('ingredientlist').children
    const direction_list = document.getElementById('directionlist').children

    console.log(ingredient_list, direction_list)

}

addEventListener('DOMContentLoaded', create_ingredient)
addEventListener('DOMContentLoaded', create_direction)