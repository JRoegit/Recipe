const emptyStar = "/static/starEmpty.png"
const fullStar = "/static/starFull.png"

let urlSplit = window.location.href.split('/')
const recipe_id = urlSplit[urlSplit.length - 1]
console.log(recipe_id)

let ratings = [
    0,
    0,
    0,
    0,
    0
]

let starState = []

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

function starReview(rating){
    stars = [
        document.getElementById('star1'),
        document.getElementById('star2'),
        document.getElementById('star3'),
        document.getElementById('star4'),
        document.getElementById('star5') 
    ]
    for(let i = 0; i < stars.length ; i++){
        if(i < rating){
            stars[i].src = fullStar  
            starState[i] = fullStar
        } else {
            stars[i].src = emptyStar
            starState[i] = emptyStar
        }
    }
    document.getElementById('rating').value = rating
}

function starHover(rating){
    starState = [
        document.getElementById('star1').src,
        document.getElementById('star2').src,
        document.getElementById('star3').src,
        document.getElementById('star4').src,
        document.getElementById('star5').src
    ]

    stars = [
        document.getElementById('star1'),
        document.getElementById('star2'),
        document.getElementById('star3'),
        document.getElementById('star4'),
        document.getElementById('star5') 
    ]

    for(let i = 0; i < stars.length ; i++){
        if(i < rating){
            stars[i].src = fullStar  
        } else {
            stars[i].src = emptyStar
        }
    }
}

function starHoverEnd(){
    stars = [
        document.getElementById('star1'),
        document.getElementById('star2'),
        document.getElementById('star3'),
        document.getElementById('star4'),
        document.getElementById('star5') 
    ]
    for(let i = 0; i < stars.length ; i++){
        stars[i].src = starState[i]  
    }
}

function add(accumulator, a) {
    return accumulator + a;
  }


function setAvgStars(avg){
    stars = [
        document.getElementById('avgstar1'),
        document.getElementById('avgstar2'),
        document.getElementById('avgstar3'),
        document.getElementById('avgstar4'),
        document.getElementById('avgstar5') 
    ]
    otherStars = [
        document.getElementById('avgstar11'),
        document.getElementById('avgstar22'),
        document.getElementById('avgstar33'),
        document.getElementById('avgstar44'),
        document.getElementById('avgstar55') 
    ]
    for(let i = 0; i < stars.length ; i++){
        if(i < avg){
            stars[i].src = fullStar
            otherStars[i].src = fullStar
        }
    }
}

// format [[violet,grey,text]]
async function setupAvgReviews(){
    const avgRating = document.getElementById('avgRating')
    const totalReviews = document.getElementById('totalReviews')
    
    bars = [
        [
            document.getElementById('starbarv5'),
            document.getElementById('starbarg5'),
            document.getElementById('starbar5')
        ],
        [
            document.getElementById('starbarv4'),
            document.getElementById('starbarg4'),
            document.getElementById('starbar4')
        ],
        [
            document.getElementById('starbarv3'),
            document.getElementById('starbarg3'),
            document.getElementById('starbar3')
        ],
        [
            document.getElementById('starbarv2'),
            document.getElementById('starbarg2'),
            document.getElementById('starbar2')
        ],
        [
            document.getElementById('starbarv1'),
            document.getElementById('starbarg1'),
            document.getElementById('starbar1')
        ]
    ]
    try {
        const response = await fetch('/review/'.concat(recipe_id))
        const json = await response.json()
        for(review of json){
            rating = parseInt(review.rating)
            if (rating != ""){
                ratings[5 - rating] += 1
            }
        }
    } catch(err) {
        console.log(err.message)
    }
    
    total = ratings.reduce(add, 0)

    let avg = 0
    for(let i = 0; i < 5; i++){
        avg += ratings[i] * (5 - i)
    }
    avg /= total
    console.log(avg)

    avgRating.textContent = `${Math.round(avg * 10) / 10} (${total})`
    totalReviews.textContent = `${total} Reviews`
    setAvgStars(Math.round(avg))
    
    for(let i = 0; i < ratings.length; i++){
        let amount = ratings[i] / total
        let violetamount = Math.floor(200 * amount)
        let greyamount = 200 - violetamount

        bars[i][0].classList.remove("w-[0px]")
        bars[i][0].style.width = `${violetamount}px`

        bars[i][1].classList.remove("w-[200px]")
        bars[i][1].style.width = `${greyamount}px`

        bars[i][2].textContent = ratings[i]
    }
}

function add_scoll_anims(){
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
    
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
}


addEventListener('DOMContentLoaded',add_scoll_anims)
addEventListener('DOMContentLoaded',setupAvgReviews)