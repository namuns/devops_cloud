
const get_default_value = () => {
    console.log("get_default_value()")


    // const get_default_value = () => 10;

    // const get_default_value = () => {
    //     return 10;
    // };

    // function get_default_value() {
    //     return 10;
    // }


    function hello(name, age = get_default_value()) {
        console.log(`안녕 나는 ${name}이야. ${age}살이지.`);
    }

    hello("Tom");
    hello("Steve");
    hello("John");


