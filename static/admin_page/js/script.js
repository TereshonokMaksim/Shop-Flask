// Вибір всіх елементів з класом 'edit-button' / Select all elements with class 'edit-button'
const editButtonList = document.querySelectorAll('.edit-button')

for (let buttonNumber = 0; buttonNumber < editButtonList.length; buttonNumber++) { // Проходимо по всіх кнопках / Iterate over all buttons
    let button = editButtonList[buttonNumber] // Отримуємо кнопку за її індексом / Get the button by its index
    button.addEventListener('click', function () { // Додаємо обробник подій 'click' до кнопки / Add 'click' event listener to the button
        document.querySelector(".blur").style = `display: flex` // Показуємо елемент з класом 'blur' / Show the element with class 'blur'
        document.querySelector(".modal-dialog").style = 'display: flex' // Показуємо модальне вікно / Show the modal dialog
        console.log(document.body.scrollTop) // Виводимо поточне прокручування сторінки / Log the current scroll position of the page
        document.body.style = "overflow-y: hidden;" // Забороняємо вертикальну прокрутку сторінки / Disable vertical scrolling of the page
        let buttonIdData = button.id.split("-") // Розділяємо id кнопки на частини / Split the button's id into parts
        document.querySelector(".modal-header").innerHTML = `CHANGE ${buttonIdData[1].toUpperCase()}` // Змінюємо заголовок модального вікна / Change the modal header
        document.querySelector(".modal-input").type = "text" // Встановлюємо тип поля введення як текст / Set the input field type to text
        document.querySelector(".modal-input").name = `new-${buttonIdData[1]}-${buttonIdData[2]}` // Встановлюємо ім'я поля введення / Set the input field name
        
        if (buttonIdData[1] == "price") { // Перевіряємо, чи тип даних 'price' / Check if the data type is 'price'
            document.querySelector(".modal-input").style.display = "flex" // Показуємо поле введення / Show the input field
            document.querySelector(".modal-input").value = document.getElementById(`price-${buttonIdData[2]}`).innerHTML.split(" ")[0] // Встановлюємо значення поля введення / Set the input field value
            document.querySelector(".modal-input").type = "number" // Встановлюємо тип поля введення як число / Set the input field type to number
            document.querySelector(".modal-input").min = 1 // Встановлюємо мінімальне значення поля введення / Set the input field minimum value
        } else if (buttonIdData[1] == "discount") { // Перевіряємо, чи тип даних 'discount' / Check if the data type is 'discount'
            document.querySelector(".modal-input").style.display = "flex" // Показуємо поле введення / Show the input field
            console.log(document.getElementById(`discount-${buttonIdData[2]}`).innerHTML.split(" ")[1]) // Виводимо значення знижки / Log the discount value
            document.querySelector(".modal-input").value = document.getElementById(`discount-${buttonIdData[2]}`).innerHTML.split(" ")[1].split("%")[0] // Встановлюємо значення поля введення / Set the input field value
            document.querySelector(".modal-input").type = "number" // Встановлюємо тип поля введення як число / Set the input field type to number
            document.querySelector(".modal-input").min = 0 // Встановлюємо мінімальне значення поля введення / Set the input field minimum value
            document.querySelector(".modal-input").max = 100 // Встановлюємо максимальне значення поля введення / Set the input field maximum value
        } else if (buttonIdData[1].includes("property")) { // Перевіряємо, чи тип даних містить 'property' / Check if the data type includes 'property'
            document.querySelector(".modal-input").style.display = "flex" // Показуємо поле введення / Show the input field
            document.querySelector(".modal-input").value = document.getElementById(`${buttonIdData[1]}-${buttonIdData[2]}-${buttonIdData[3]}`).innerHTML // Встановлюємо значення поля введення / Set the input field value
            document.querySelector(".modal-input").name = `new-${buttonIdData[1]}-${buttonIdData[2]}-${buttonIdData[3]}` // Встановлюємо ім'я поля введення / Set the input field name
        } else if (buttonIdData[1] == "image") { // Перевіряємо, чи тип даних 'image' / Check if the data type is 'image'
            document.querySelector('.image-modal-input').style.display = 'flex' // Показуємо поле введення для зображення / Show the image input field
        } else { // Інші випадки / Other cases
            document.querySelector(".modal-input").style.display = "flex" // Показуємо поле введення / Show the input field
            document.querySelector(".modal-input").value = document.getElementById(`${buttonIdData[1]}-${buttonIdData[2]}`).innerHTML // Встановлюємо значення поля введення / Set the input field value
        }
    })
}

let buttons_image = document.querySelectorAll(".select-image-input") // Вибір всіх елементів з класом 'select-image-input' / Select all elements with class 'select-image-input'
let button_input = document.querySelectorAll(".modal-input-image") // Вибір всіх елементів з класом 'modal-input-image' / Select all elements with class 'modal-input-image'

for (let buttonNumber = 0; buttonNumber < buttons_image.length; buttonNumber++) { // Проходимо по всіх кнопках зображень / Iterate over all image buttons
    let button_image = buttons_image[buttonNumber] // Отримуємо кнопку зображення за її індексом / Get the image button by its index
    button_image.addEventListener("click", () => { // Додаємо обробник подій 'click' до кнопки зображення / Add 'click' event listener to the image button
        button_input[buttonNumber].click() // Імітуємо клік по прихованому полю введення зображення / Simulate click on the hidden image input field
    })
    button_input[buttonNumber].onchange = () => { // Додаємо обробник подій 'change' до поля введення зображення / Add 'change' event listener to the image input field
        document.querySelectorAll(".selected-image-input")[buttonNumber].innerHTML = button_input[buttonNumber].files[0].name // Оновлюємо текст вибраного файлу зображення / Update the selected image file text
    }
}

let buttonNewProduct = document.querySelector(".new-product") // Вибір кнопки додавання нового продукту / Select the new product button
buttonNewProduct.addEventListener( // Додаємо обробник подій 'click' до кнопки нового продукту / Add 'click' event listener to the new product button
    type = "click", // Тип події 'click' / Event type 'click'
    listener = () => { // Лістенер події / Event listener
        document.querySelector(".blur").style.display = "flex" // Показуємо елемент з класом 'blur' / Show the element with class 'blur'
        document.querySelector(".modal-window-product").style.display = "flex" // Показуємо модальне вікно продукту / Show the product modal window
        document.querySelector("body").style.overflowY = "hidden" // Забороняємо вертикальну прокрутку сторінки / Disable vertical scrolling of the page
    }
)