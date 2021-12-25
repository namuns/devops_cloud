
Array.prototype.sum = function () {
    return this.reduce((acc, element) => {
        return acc + element;
    }, 0);
};

const result = [1, 2, 3, 4, 5].sum();
console.log(result);