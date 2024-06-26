function change_price (product_id, increase) { // функція для зміни ціни продукту / function to change the product price
    let product_price = +document.getElementById(`price-${product_id}`).innerHTML.split(" ")[0] // отримання ціни продукту / getting the product price
    let current_price_overall = +document.querySelector(".overall-price").innerHTML.split(" ")[0] // отримання поточної загальної ціни / getting the current overall price
    let current_products_price = +document.querySelector(".all-products-price").innerHTML.split(" ")[0] // отримання поточної ціни всіх продуктів / getting the current total products price
    let all_discount = +document.querySelector(".discount-price").innerHTML.split(' ')[0] // отримання поточної загальної знижки / getting the current total discount
    let new_discount = 0 // ініціалізація нової знижки / initializing the new discount
    try { // спроба виконати наступний блок коду / try to execute the following block of code
        new_discount = Math.round((+document.getElementById(`price-${product_id}`).innerHTML.split(' ')[0] - +document.getElementById(`discount-${product_id}`).innerHTML.split(' ')[0]) * 100) / 100 // розрахунок нової знижки / calculating the new discount
        console.log(new_discount) // виведення нової знижки в консоль / logging the new discount to the console
    }
    catch (err) { // у разі помилки виконати наступний блок коду / if there is an error, execute the following block of code
        console.log("This product has no discount") // виведення повідомлення про відсутність знижки в консоль / logging the message about no discount to the console
    }
    if (increase == 1){ // якщо значення increase дорівнює 1 / if the value of increase is 1
        current_products_price += product_price // збільшення поточної ціни всіх продуктів / increasing the current total products price
        all_discount += new_discount // збільшення загальної знижки / increasing the total discount
    }
    else{ // інакше / otherwise
        current_products_price -= product_price // зменшення поточної ціни всіх продуктів / decreasing the current total products price
        all_discount -= new_discount // зменшення загальної знижки / decreasing the total discount
    }
    current_products_price = Math.round(current_products_price * 100) / 100 // округлення поточної ціни всіх продуктів / rounding the current total products price
    all_discount = Math.round(all_discount * 100) / 100 // округлення загальної знижки / rounding the total discount
    console.log(new_discount, all_discount) // виведення нової знижки та загальної знижки в консоль / logging the new discount and total discount to the console
    current_price_overall = Math.round((current_products_price - all_discount) * 100) / 100 // розрахунок та округлення нової загальної ціни / calculating and rounding the new overall price
    document.querySelector(".overall-price").innerHTML = `${current_price_overall} грн` // оновлення значення загальної ціни на сторінці / updating the overall price on the page
    document.querySelector(".discount-price").innerHTML = `${all_discount} грн` // оновлення значення знижки на сторінці / updating the discount price on the page
    document.querySelector(".all-products-price").innerHTML = `${current_products_price} грн` // оновлення значення ціни всіх продуктів на сторінці / updating the total products price on the page
}

function change_product_count (product_id, increase){ // функція для зміни кількості продуктів / function to change the product count
    let product_count = +document.getElementById(`count-${product_id}`).innerHTML // отримання кількості продукту / getting the product count
    let products_count = +document.querySelector(".all-products-text").innerHTML.split("-")[0] // отримання поточної кількості всіх продуктів / getting the current total products count
    let current_cookie = document.cookie.split(";") // отримання поточних кукі / getting the current cookies
    let product_cookie = 0 // ініціалізація кукі для продукту / initializing the product cookie
    let product_cookie_index = 0 // ініціалізація індексу кукі для продукту / initializing the product cookie index
    for (let cookie_num = 0; cookie_num < current_cookie.length; cookie_num++) { // цикл по всіх кукі / loop through all cookies
        if (product_cookie == 0) { // якщо кукі для продукту ще не знайдено / if the product cookie is not found yet
            let this_cookie = current_cookie[cookie_num].split("=") // розділити кукі по знаку рівності / split the cookie by the equals sign
            if (this_cookie[0] == "product") { // якщо знайдено кукі для продукту / if the product cookie is found
                product_cookie_index = cookie_num // зберегти індекс кукі для продукту / save the product cookie index
                product_cookie = this_cookie[1].split(" ") // розділити значення кукі на окремі продукти / split the cookie value into individual products
            }
        }
    }
    if(increase == 1){ // якщо значення increase дорівнює 1 / if the value of increase is 1
        products_count++ // збільшити загальну кількість продуктів / increment the total product count
        product_count++ // збільшити кількість конкретного продукту / increment the product count
        product_cookie.push(product_id) // додати ідентифікатор продукту до кукі / add the product ID to the cookie
    }
    else{ // інакше / otherwise
        products_count-- // зменшити загальну кількість продуктів / decrement the total product count
        product_count-- // зменшити кількість конкретного продукту / decrement the product count
        if (product_count == 0){ // якщо кількість продукту дорівнює нулю / if the product count is zero
            document.getElementById(`product-${product_id}`).remove() // видалити продукт з DOM / remove the product from the DOM
        }
        product_cookie.splice(product_cookie.indexOf(String(product_id)), 1) // видалити ідентифікатор продукту з кукі / remove the product ID from the cookie
        if (product_cookie.length == 0) { // якщо більше немає продуктів у кукі / if there are no more products in the cookie
            product_cookie = null // встановити значення кукі для продукту як null / set the product cookie to null
        }
        console.log(product_cookie) // вивести значення кукі для продукту в консоль / log the product cookie to the console
    }
    if (product_cookie != null) { // якщо кукі для продукту не є null / if the product cookie is not null
        current_cookie[product_cookie_index] = `product=${product_cookie.join(" ")}; Path=/` // оновити кукі для продукту / update the product cookie
        document.cookie = current_cookie.join(";") // оновити кукі браузера / update the browser cookies
    }
    else { // інакше / otherwise
        current_cookie[product_cookie_index] = "product='1'; Path=/; Max-Age=-1" // видалити кукі для продукту / delete the product cookie
        document.cookie = current_cookie.join(";") // оновити кукі браузера / update the browser cookies
        console.log(document.cookie, current_cookie) // вивести оновлені кукі в консоль / log the updated cookies to the console
    }
    try { // спроба виконати наступний блок коду / try to execute the following block of code
        document.getElementById(`count-${product_id}`).innerHTML = product_count // оновити кількість продукту в DOM / update the product count in the DOM
    }
    catch (no_product_error) { // у разі помилки виконати наступний блок коду / if there is an error, execute the following block of code
        console.log("Product was successfully deleted, I guess.") // вивести повідомлення про видалення продукту в консоль / log the product deletion message to the console
        console.log(`Take a look at the error: ${no_product_error.name} /// ${no_product_error.message}`) // вивести інформацію про помилку в консоль / log the error information to the console
    }
    console.log(document.querySelector(".all-products-text")) // вивести інформацію про всі продукти в консоль / log the all products text to the console
    document.querySelector(".all-products-text").innerHTML = `${products_count}-и товари на суму` // оновити текст з інформацією про всі продукти / update the all products text
}

function delete_all_product (product_id){ // функція для видалення всіх продуктів / function to delete all products
    let product_count = Number(document.getElementById(`count-${product_id}`).innerHTML);

    // Одержуємо загальну ціну продуктів/ Get the total price of the products
    let all_products_price = Number(document.getElementById(`price-${product_id}`).innerHTML.split(" ")[0]) * product_count;

    // Змінна для загальної знижки/ Variable for total discount
    let all_products_discount = 0;

    try {
        // Розрахунок загальної знижки/ Calculate the total discount
        all_products_discount = Math.round((-Number(document.getElementById(`discount-${product_id}`).innerHTML.split(" ")[0]) * product_count + all_products_price) * 100) / 100;
    } catch (error) {
        // Якщо продукт не має знижки/ If the product has no discount
        console.log("This product has no discount");
    }

    // Отримуємо кукі продуктів/ Get the product cookies
    let product_cookie = document.cookie.split(";");

    // Перебираємо усі кукі / We go through all the cookies
    for (let number_cookie = 0; number_cookie < product_cookie.length; number_cookie++) {
        // Перевіряємо чи відноситься кукі до продуктів / We check whether cookies belong to products
        if (product_cookie[number_cookie].includes("product")) {
            // Ділимо значення кукі продуктів на окремі значення / We divide the cookie values ​​of the products into separate values
            product_cookie = product_cookie[number_cookie].split('=')[1].split(' ');
            // Зберігаємо кількість значень кукі / We store the number of cookie values
            let cookie_count = product_cookie.length;
            // Створюємо змінну для фіксування видалення продукту / We create a variable to record the removal of the product
            let deleted_cookie = 0;
            console.log(product_cookie); // Виводимо кукі продуктів у консоль/ Log the product cookies
            // Перебираємо кукі продуктів
            for (let number_product = 0; number_product < cookie_count; number_product++) {
                // Зберігаємо індекс кукі продукта / We store the product cookie index
                let cookie_index = number_product - deleted_cookie;
                // Перевіряємо чи є поточне кукі продукту тим, що потрібно видалити / Checking if the current product cookie is the one to delete
                if (product_cookie[cookie_index] == product_id) {
                    // Збільшуємо індекс видаленого продукту на 1 / We increase the index of the deleted product by 1
                    deleted_cookie++;
                    // Зберігаємо видалене кукі продукту і видаляємо його з всього списку продуктів / We save the deleted product cookie and remove it from the entire list of products
                    let deleted = product_cookie.splice(cookie_index, 1);
                    // Виводимо у консоль усі кукі продуктів, поточне кукі продукта, індекс кукі та видалене кукі / We output all product cookies, the current product cookie, the cookie index, and the deleted cookie to the console
                    console.log(product_cookie, product_cookie[cookie_index], cookie_index, deleted);
                }
            }

            if (product_cookie.length == 0) {
                // Видаляємо кукі, якщо продуктів не залишилось/ Delete the cookie if no products left
                document.cookie = "product = 0; path = /; Max-Age = -1";
            } else {
                // Оновлюємо кукі продуктів/ Update the product cookies
                document.cookie = `product = ${product_cookie.join(' ')}; path = /`;
            }
            // Зупиняємо цикл / We stop the cycle
            break;
        }
    }

    console.log(all_products_discount);
    // Оновлюємо загальну кількість продуктів / We update the total number of products
    document.querySelector(".all-products-text").innerHTML = `${document.querySelector(".all-products-text").innerHTML.split("-")[0] - product_count}-и товари на суму`
    // Оновлюємо загальну ціну всіх продуктів без знижки / We update the total price of all products without discount
    document.querySelector('.all-products-price').innerHTML = `${Math.round((document.querySelector('.all-products-price').innerHTML.split(' ')[0] - all_products_price) * 100) / 100} грн`
    // Оноволюємо загальну знижку усіх продуктів / We are renewing the general discount for all products
    document.querySelector('.discount-price').innerHTML = `${Math.round((document.querySelector('.discount-price').innerHTML.split(' ')[0] - all_products_discount) * 100) / 100} грн`
    // Оновлюємо загальну ціну усіх продуктів з знижкою / We update the total price of all discounted products
    document.querySelector('.overall-price').innerHTML = `${Math.round((document.querySelector('.overall-price').innerHTML.split(' ')[0] - (all_products_price - all_products_discount)) * 100) / 100} грн`
    // Видаляємо поточний продукт з сторінки / We remove the current product from the page
    document.getElementById(`product-${product_id}`).remove()

}

// Зберігаємо у константу лічильник кошику / We save the basket counter as a constant
const basket_counter = document.getElementById("basket-counter")
// Створюємо функцію для оновлення лічильнику кошику / We create a function to update the counter of the basket
function change_basket_count () {
    // Створюємо змінну для кількості продуктів у кукі / We create a variable for the number of products in the cookie
    let product_count = 0
    // Перебираємо кукі / Sort through cookies
    for (let cookie_num = 0; cookie_num < document.cookie.split(";").length; cookie_num++) {
        // Перевіряємо чи є кількість продуктів 0 / We check whether the number of products is 0
        if (product_count == 0) {
            // Зберігаємо поточне кукі / We save the current cookie
            let this_cookie = document.cookie.split(";")[cookie_num].split("=")
            // Перевіряємо чи є поточне кукі кукі продуктів / We check whether the current cookie is a product cookie
            if (this_cookie[0] == "product") {
                // Зберігаємо кількість продуктів у кукі / We store the number of products in a cookie
                product_count = this_cookie[1].split(" ").length
            }
        }
    }
    // Виводимо у консоль кількість продуктів / We output the number of products to the console
    console.log(product_count)
    // Перевіряємо чи є продукти у кукі / We check whether there are products in the cookie
    if (product_count != 0){
        // Перевіряємо чи є кількість продуктів більше ніж 99 / We check whether the number of products is more than 99
        if (product_count > 99){
            // Якщо умова вище виконалась, то текст замінюється на 99+ показуючи лімит / If the condition above is met, the text is replaced by 99+ showing the limit
            product_count = "99+"
        }
        // Замінюємо текст у лічильнику на кількість продуктів / We replace the text in the counter with the number of products
        basket_counter.innerHTML = product_count
    }
    // Якщо продуктів у кукі нема / If there are no products in the cookie
    else {
        // Видаляємо текст з лічильника кошику / We delete the text from the counting basket
        basket_counter.innerHTML = ""
    }
}  

// Зберігаємо усі кнопки які зменшують кількість продуктів / We keep all the buttons that reduce the number of products
const reduce_buttons = document.querySelectorAll(".button-reduce")
// Зберігаємо усі кнопки які збільшують кількість продуктів / We keep all the buttons that increase the number of products
const increase_buttons = document.querySelectorAll(".button-increase")
// Зберігаємо усі кнопки які видаляють продукт / We keep all the buttons that remove the product
const delete_buttons = document.querySelectorAll(".button-delete")

// Перебираємо усі кнопки / We go through all the buttons
for (let button_number = 0; button_number < reduce_buttons.length; button_number++){
    // Зберігаємо id продукта / We store the product id
    let product_id = reduce_buttons[button_number].id.split("-")[1]
    // Додаємо до поточної кнопки зменшення функцію яка буде виконуватися при натисненні на кнопку / We add to the current decrease button a function that will be executed when the button is pressed
    reduce_buttons[button_number].addEventListener("click", function(){
        // Зменшуємо ціну на -1 поточним продуктом / We reduce the price by -1 current product
        change_price(product_id, -1)
        // Зменшуємо кількість на -1 поточним продуктом / We reduce the quantity by -1 with the current product
        change_product_count(product_id, -1) 
        // Змінюємо кількість продуктів у лічильнику / We change the number of products in the counter
        change_basket_count()
    })
    // Додаємо до поточної кнопки збільшення функцію яка буде виконуватися при натисненні на кнопку / We add to the current increase button a function that will be executed when the button is pressed
    increase_buttons[button_number].addEventListener("click", function(){
        // Збільшуємо ціну на 1 поточним продуктом / We increase the price by 1 current product
        change_price(product_id, 1)
        // Збільшуємо кількість на 1 поточним продуктом / We increase the quantity by 1 current product
        change_product_count(product_id, 1)
        // Змінюємо кількість продуктів у лічильнику / We change the number of products in the counter
        change_basket_count()
    })
    // Додаємо до поточної кнопки видалення функцію яка буде виконуватися при натисненні на кнопку / We add to the current delete button a function that will be executed when the button is pressed
    delete_buttons[button_number].addEventListener("click", function(){
        // Видаляємо усі продукти / Remove all products
        delete_all_product(product_id)
        // Змінюємо кількість продуктів у лічильнику / We change the number of products in the counter
        change_basket_count()
    })
}

// Зберігаємо кнопку відкриття модального вікна / Save the modal window opening button
const modalOpenButton = document.querySelector(".confirmation-button")
// Додаємо кнопці відкриття модального вікна дію при натисненні на неї / We add an action to the modal window opening button when it is clicked
modalOpenButton.addEventListener("click", () => {
    // Перевіряємо чи є продукти у кошику шляхом перевірки їх кількості / We check whether there are products in the basket by checking their quantity
    if (document.getElementById("basket-counter").innerHTML != "") {
        // Задаємо розмиттю заднього фону відображення / We set the background blur of the display
        document.querySelector(".blur").style.display = "flex"
    }
})