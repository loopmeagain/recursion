const por = (unNumero,otroNumero) => unNumero * otroNumero;
const dividir = (unNumero,otroNumero) => unNumero / otroNumero;
const ejecutarOperacion = (unNumero,otroNumero,unaOperacion) => unaOperacion(unNumero,otroNumero)
console.log(por(4,2));
console.log(por(8,8));
console.log(dividir(4,12));
console.log(ejecutarOperacion(2,4,por));