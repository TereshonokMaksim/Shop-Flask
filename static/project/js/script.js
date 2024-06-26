// Зберігаємо всі кукі / We store all cookies
let products = document.cookie.split(";")
// Створюємо кількість продуктів / We create a number of products
let product_count = 0
// Перебираємо всі кукі / We go through all the cookies
for (let product_num = 0; product_num < products.length; product_num ++) {
    // Зберігаємо кукі за поточним номером кукі / We store cookies by the current cookie number
    let product = products[product_num].split("=")
    // Перевіряємо чи є кукі кукі продукта / We check whether there are cookies in the product
    if (product[0].includes("product")) {
        // Зберігаємо кількість продукта з кукі / We save the amount of product from the cookie
        product_count = product[1].split(" ").length
    }
}
// Зберігаємо лічильник кошику / We save the basket counter
let basket_counter = document.getElementById("basket-counter")
// Перевіряємо чи є продукти у кукі / We check whether there are products in the cookie
if (product_count != 0){
    // Перевіряємо чи кількість продуктів перевищує 99 / We check whether the number of products exceeds 99
    if (product_count > 99){
        // Змінюємо текст продуктів на 99+ вказуючи на ліміт / We change the text of the products to 99+ indicating the limit
        product_count = "99+"
    }
    // Змінюємо текст лічильника кошику на кількість продуктів / We change the text of the basket counter to the number of products
    basket_counter.innerHTML = product_count
}
// Якщо продуктів немає у кукі / If there are no products in the cookie
else {
    // Видаляємо текст з лічильника кошику / We delete the text from the counter of the basket
    basket_counter.innerHTML = ""
}