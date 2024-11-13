function switchButton(multiplier){
    const defaultButton = document.getElementById("defaultButton")
    const doubleButton = document.getElementById("doubleButton")
    const quadButton = document.getElementById("quadButton")
    switch (multiplier){
        case 1:
            defaultButton.disabled = true    
            toggleButton(defaultButton)
            cleanButton(doubleButton)
            cleanButton(quadButton)
            break
        case 2:
            doubleButton.disabled = true    
            toggleButton(doubleButton)
            cleanButton(defaultButton)
            cleanButton(quadButton)
            break
        case 4:
            quadButton.disabled = true    
            toggleButton(quadButton)
            cleanButton(defaultButton)
            cleanButton(doubleButton)
            break
    }
}

function cleanButton(button){
    button.disabled = false
    button.classList.add("text-black")
    button.classList.add("hover:bg-gray-50")
    button.classList.remove("bg-violet-400")
    button.classList.remove("text-white")
}

function toggleButton(button){
    button.classList.remove("text-black")
    button.classList.remove("hover:bg-gray-50")
    button.classList.add("bg-violet-400")
    button.classList.add("text-white")
}

