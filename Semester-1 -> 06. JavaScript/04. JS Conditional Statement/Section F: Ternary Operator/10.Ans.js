let cart$Total = 6000;
let discount = cart$Total >= 5000 ? 20
             : cart$Total >= 2000 ? 10
             : cart$Total >= 1000 ? 5
             : 0;
let $result = {
    discount: discount + "%",
    finalAmount: cart$Total - (cart$Total * discount / 100)
};
console.log($result);


let cartTotal = 900;
let result =
    cartTotal >= 5000
        ? `Discount = 20% & Final Amount = ${cartTotal * 0.80} Rs`
        : cartTotal >= 2000
            ? `Discount = 10% & Final Amount = ${cartTotal * 0.90} Rs`
            : cartTotal >= 1000
                ? `Discount = 5% & Final Amount = ${cartTotal * 0.95} Rs`
                : `Discount = 0% & Final Amount = ${cartTotal} Rs`;
console.log(result);


let $cartTotal = 900;
let resul$ = `Discount = ${
    $cartTotal >= 5000 ? 20 :
    $cartTotal >= 2000 ? 10 :
    $cartTotal >= 1000 ? 5 : 0
}% & Final Amount = ${
    $cartTotal - $cartTotal * (
        $cartTotal >= 5000 ? 0.20 :
        $cartTotal >= 2000 ? 0.10 :
        $cartTotal >= 1000 ? 0.05 : 0
    )
} Rs`;
console.log(result$);