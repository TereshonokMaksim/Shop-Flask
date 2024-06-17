let products = document.cookie.split(";")
let product_count = 0
for (let product_num = 0; product_num < products.length; product_num ++) {
    let product = products[product_num].split("=")
    if (product[0].includes("product")) {
        product_count = product[1].split(" ").length
    }
}
let basket_counter = document.getElementById("basket-counter")
if (product_count != 0){
    if (product_count > 99){
        product_count = "99+"
    }
    basket_counter.innerHTML = product_count
}
else {
    basket_counter.innerHTML = ""
}