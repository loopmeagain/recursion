const factorial = (unNumero) => {
    if(unNumero>1) {
        return factorial(unNumero-1) * unNumero;
    }
    return 1;
}
console.log(factorial(5));
