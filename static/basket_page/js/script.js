function change_price (product_id, increase) {
    let product_price = +document.getElementById(`price-${product_id}`).innerHTML.split(" ")[0]
    let current_price_overall = +document.querySelector(".overall-price").innerHTML.split(" ")[0]
    let current_products_price = +document.querySelector(".all-products-price").innerHTML.split(" ")[0]
    let all_discount = +document.querySelector(".discount-price").innerHTML.split(' ')[0]
    let new_discount = 0
    try {
        new_discount = Math.round((+document.getElementById(`price-${product_id}`).innerHTML.split(' ')[0] * +document.getElementById(`discount-${product_id}`).innerHTML.split(' ')[0]) / 100)
        console.log(new_discount)
    }
    catch (err) {
        console.log("This product has no discount")
    }
    if (increase == 1){
        current_products_price += product_price
        all_discount += new_discount
    }
    else{
        current_products_price -= product_price
        all_discount -= new_discount
    }
    current_products_price = Math.round(current_products_price * 100) / 100
    all_discount = Math.round(all_discount * 100) / 100
    console.log(new_discount, all_discount)
    current_price_overall = Math.round((current_products_price - all_discount) * 100) / 100
    document.querySelector(".overall-price").innerHTML = `${current_price_overall} грн`
    document.querySelector(".discount-price").innerHTML = `${all_discount} грн`
    document.querySelector(".all-products-price").innerHTML = `${current_products_price} грн`
}

function change_product_count (product_id, increase){
    let product_count = +document.getElementById(`count-${product_id}`).innerHTML
    let products_count = +document.querySelector(".all-products-text").innerHTML.split("-")[0]
    let current_cookie = document.cookie.split(";")
    let product_cookie = 0
    let product_cookie_index = 0
    for (let cookie_num = 0; cookie_num < current_cookie.length; cookie_num++) {
        if (product_cookie == 0) {
            let this_cookie = current_cookie[cookie_num].split("=")
            if (this_cookie[0] == "product") {
                product_cookie_index = cookie_num
                product_cookie = this_cookie[1].split(" ")
            }
        }
    }
    if(increase == 1){
        products_count++
        product_count++
        product_cookie.push(product_id)
    }
    else{
        products_count--
        product_count--
        if (product_count == 0){
            document.getElementById(`product-${product_id}`).remove()
        }
        product_cookie.splice(product_cookie.indexOf(String(product_id)), 1)
        if (product_cookie.length == 0) {
            product_cookie = null
        }
        console.log(product_cookie)
    }
    if (product_cookie != null) { 
        current_cookie[product_cookie_index] = `product = ${product_cookie.join(" ")}; Path = /`
        document.cookie = current_cookie.join(";")
    }
    else {
        current_cookie[product_cookie_index] = "product = '1'; Path = /; Max-Age = -1"
        document.cookie = current_cookie.join(";")
        console.log(document.cookie, current_cookie)
    }
    try {
        document.getElementById(`count-${product_id}`).innerHTML = product_count
    }
    catch (no_product_error) {
        console.log(`Product was succefully deleted, i guess.`)
        console.log(`Take a look at the error: ${no_product_error.name} /// ${no_product_error.message}`)
    }
    console.log(document.querySelector(".all-products-text"))
    document.querySelector(".all-products-text").innerHTML = `${products_count}-и товари на суму`
}

function delete_all_product (product_id){
    let product_count = Number(document.getElementById(`count-${product_id}`).innerHTML)
    let all_products_price = Number(document.getElementById(`price-${product_id}`).innerHTML.split(" ")[0]) * product_count
    let all_products_discount = 0
    try{
        all_products_discount = Math.round((-Number(document.getElementById(`discount-${product_id}`).innerHTML.split(" ")[0]) * product_count + all_products_price) * 100) / 100
    }
    catch (error){
        console.log("This product has no discount")
    }

    // console.log(all_products_discount, all_products_price, product_count, document.getElementById(`count-${product_id}`).innerHTML, Number(document.getElementById(`discount-${product_id}`).innerHTML.split(" ")[0]) * product_count)
    let product_cookie = document.cookie.split(";")
    for (let number_cookie = 0; number_cookie < product_cookie.length; number_cookie++){
        if (product_cookie[number_cookie].includes("product")){
            product_cookie = product_cookie[number_cookie].split('=')[1].split(' ')
            let cookie_count = product_cookie.length
            let deleted_cookie = 0
            console.log(product_cookie)
            for (let number_product = 0; number_product < cookie_count; number_product++){
                // console.log(number_product - deleted_cookie, product_cookie, product_id, product_cookie[number_cookie])
                let cookie_index = number_product - deleted_cookie
                if (product_cookie[cookie_index] == product_id){
                    deleted_cookie++
                    let deleted = product_cookie.splice(cookie_index, 1)
                    console.log(product_cookie, product_cookie[cookie_index], cookie_index, deleted)
                }
            }
            if (product_cookie.length == 0){
                document.cookie = "product = 0; path = /; Max-Age = -1" 
                
            }
            else {
                document.cookie = `product = ${product_cookie.join(' ')}; path = /`
            }
        break
        }
    } 
    document.querySelector(".all-products-text").innerHTML = `${document.querySelector(".all-products-text").innerHTML.split("-")[0] - product_count}-и товари на суму`
    document.querySelector('.all-products-price').innerHTML = `${Math.round((document.querySelector('.all-products-price').innerHTML.split(' ')[0] - all_products_price) * 100) / 100} грн`
    document.querySelector('.discount-price').innerHTML = `${Math.round((document.querySelector('.discount-price').innerHTML.split(' ')[0] - all_products_discount) * 100) / 100} грн`
    document.querySelector('.overall-price').innerHTML = `${Math.round((document.querySelector('.overall-price').innerHTML.split(' ')[0] - (all_products_price - all_products_discount)) * 100) / 100} грн`
    document.getElementById(`product-${product_id}`).remove()

}

const basket_counter = document.getElementById("basket-counter")
function change_basket_count () {
    let product_count = 0
    for (let cookie_num = 0; cookie_num < document.cookie.split(";").length; cookie_num++) {
        if (product_count == 0) {
            let this_cookie = document.cookie.split(";")[cookie_num].split("=")
            if (this_cookie[0] == "product") {
                product_count = this_cookie[1].split(" ").length
            }
        }
    }
    console.log(product_count)
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

const reduce_buttons = document.querySelectorAll(".button-reduce")
const increase_buttons = document.querySelectorAll(".button-increase")
const delete_buttons = document.querySelectorAll(".button-delete")

for (let button_number = 0; button_number < reduce_buttons.length; button_number++){
    let product_id = reduce_buttons[button_number].id.split("-")[1]
    reduce_buttons[button_number].addEventListener("click", function(){
        change_price(product_id, -1)
        change_product_count(product_id, -1) 
        change_basket_count()
    })
    increase_buttons[button_number].addEventListener("click", function(){
        change_price(product_id, 1)
        change_product_count(product_id, 1)
        change_basket_count()
    })
    delete_buttons[button_number].addEventListener("click", function(){
        delete_all_product(product_id)
        change_basket_count()
    })
}