const list_buttons = document.querySelectorAll(".add-product") // Отримати всі кнопки з класом "add-product" / Get all buttons with the class "add-product"

for (let button_number = 0; button_number < list_buttons.length; button_number++) { // Перебрати всі кнопки / Loop through all buttons

    let button = list_buttons[button_number] // Зберегти поточну кнопку в змінну / Save the current button to a variable

    button.addEventListener("click", function () { // Додати обробник подій "click" для кнопки / Add a "click" event handler to the button

        console.log(document.cookie) // Вивести поточні кукі у консоль / Log the current cookies to the console

        let button_block = document.getElementById(`product-${button.id}`) // Отримати блок продукту за ідентифікатором кнопки / Get the product block by the button's ID

        let in_stock = button_block.querySelector(".product-in-stock").id // Отримати ідентифікатор стану запасу продукту / Get the stock status ID of the product

        if (in_stock == "1"){ // Перевірити, чи продукт є в наявності / Check if the product is in stock
            let product = "" // Ініціалізувати змінну для продукту / Initialize a variable for the product

            if (document.cookie.includes("product")){ // Перевірити, чи кукі містять продукт / Check if cookies contain a product
                product = document.cookie.split("=")[1] // Отримати поточні продукти з кукі /  Get current products from cookies
                product = product + " " + button.id // Додати ідентифікатор кнопки до списку продуктів / Add the button's ID to the product list
            }
            else{
                product = button.id // Якщо кукі не містять продукт, встановити ідентифікатор кнопки як продукт / If cookies don't contain a product, set the button's ID as the product
            }

            document.cookie = `product = ${product}; path = /` // Оновити кукі з новим продуктом / Update the cookies with the new product
            let products = document.cookie.split(";") // Розділити кукі на окремі частини / Split cookies into individual parts
            let product_count = 0 // Ініціалізувати змінну для підрахунку кількості продуктів / Initialize a variable to count the number of products
            for (let product_num = 0; product_num < products.length; product_num ++) { // Перебрати всі кукі / Iterate through all cookies
                let product = products[product_num].split("=") // Розділити кожен кукі на ключ і значення / Split each cookie into key and value
                if (product[0].includes("product")) {// Перевірити, чи кукі містять інформацію про продукти / Check if the cookie contains product information
                    product_count = product[1].split(" ").length // Підрахувати кількість продуктів / Count the number of products
                }
            }

            let basket_counter = document.getElementById("basket-counter") // Отримати елемент кошика за його ідентифікатором / Get the basket element by its identifier
            if (product_count != 0){ // Перевірити, чи є продукти в кошику / Check if there are any products in the basket
                if (product_count > 99){ // Перевірити, чи кількість продуктів перевищує 99 / Check if the product count exceeds 99
                    product_count = "99+" // Встановити значення "99+" якщо кількість продуктів більше 99 / Set value to "99+" if product count is greater than 99
                }
                basket_counter.innerHTML = product_count // Оновити HTML з кількістю продуктів / Update HTML with product count
            }
            else {
                basket_counter.innerHTML = "" // Очистити значення кошику, якщо немає продуктів/ Clear basket value if no products
            }
        }
    }) // Закриття функції обробника подій та дужок for / Closing event handler function and for loop brackets
}