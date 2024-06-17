const editButtonList = document.querySelectorAll('.edit-button')

for (let buttonNumber = 0; buttonNumber < editButtonList.length; buttonNumber++) {
    let button = editButtonList[buttonNumber]
    button.addEventListener('click', function () {
            document.querySelector(".blur").style = `display: flex`
            document.querySelector(".modal-dialog").style = 'display: flex'
            console.log(document.body.scrollTop)
            document.body.style = "overflow-y: hidden;"
            let buttonIdData = button.id.split("-")
            document.querySelector(".modal-header").innerHTML = `CHANGE ${buttonIdData[1].toUpperCase()}`
            document.querySelector(".modal-input").type = "text"
            document.querySelector(".modal-input").name = `new-${buttonIdData[1]}-${buttonIdData[2]}`
            if (buttonIdData[1] == "price") {
                document.querySelector(".modal-input").style.display = "flex"
                document.querySelector(".modal-input").value = document.getElementById(`price-${buttonIdData[2]}`).innerHTML.split(" ")[0]
                document.querySelector(".modal-input").type = "number"
                document.querySelector(".modal-input").min = 1
            }
            else if (buttonIdData[1] == "discount") {
                document.querySelector(".modal-input").style.display = "flex"
                console.log(document.getElementById(`discount-${buttonIdData[2]}`).innerHTML.split(" ")[1])
                document.querySelector(".modal-input").value = document.getElementById(`discount-${buttonIdData[2]}`).innerHTML.split(" ")[1].split("%")[0]
                document.querySelector(".modal-input").type = "number"
                document.querySelector(".modal-input").min = 0
                document.querySelector(".modal-input").max = 100
            }
            else if (buttonIdData[1].includes("property")) {
                document.querySelector(".modal-input").style.display = "flex"
                document.querySelector(".modal-input").value = document.getElementById(`${buttonIdData[1]}-${buttonIdData[2]}-${buttonIdData[3]}`).innerHTML
                document.querySelector(".modal-input").name = `new-${buttonIdData[1]}-${buttonIdData[2]}-${buttonIdData[3]}`
            }
            else if (buttonIdData[1] == "image") {
                document.querySelector('.image-modal-input').style.display = 'flex'
            }
            else {
                document.querySelector(".modal-input").style.display = "flex"
                document.querySelector(".modal-input").value = document.getElementById(`${buttonIdData[1]}-${buttonIdData[2]}`).innerHTML
            }
        }
    )
}

let buttons_image = document.querySelectorAll(".select-image-input")
let button_input =  document.querySelectorAll(".modal-input-image")

for (let buttonNumber = 0; buttonNumber < buttons_image.length; buttonNumber++ ){
    let button_image = buttons_image[buttonNumber]
    button_image.addEventListener("click", () => {
        button_input[buttonNumber].click()
    })
    button_input[buttonNumber].onchange = () => {
        document.querySelectorAll(".selected-image-input")[buttonNumber].innerHTML = button_input[buttonNumber].files[0].name
    }
}


let buttonNewProduct = document.querySelector(".new-product")
buttonNewProduct.addEventListener(
    type = "click",
    listener = () => {
        document.querySelector(".blur").style.display = "flex"
        document.querySelector(".modal-window-product").style.display = "flex"
        document.querySelector("body").style.overflowY = "hidden"
    }
)

// const exitModalButton = document.querySelector(".modal-close")

// exitModalButton.addEventListener("click", function () {
//     document.querySelector(".blur").style = `display: none`
//     document.body.style = "overflow-y: auto"
//     document.querySelector(".modal-input").value = ""
// })