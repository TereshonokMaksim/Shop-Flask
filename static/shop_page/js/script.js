const list_buttons = document.querySelectorAll(".add-product")
for (let button_number = 0; button_number < list_buttons.length; button_number++) {
    let button = list_buttons[button_number]
    button.addEventListener("click", function () {
        console.log(document.cookie)

        let button_block = document.getElementById(`product-${button.id}`)
        let in_stock = button_block.querySelector(".product-in-stock").id
        if (in_stock == "1"){
        let product = ""
            if (document.cookie.includes("product")){
                product = document.cookie.split("=")[1]
                product = product + " " + button.id
            }
            else{
                product = button.id    
            }
            document.cookie = `product = ${product}; path = /`
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
        }
    }  
    )
}