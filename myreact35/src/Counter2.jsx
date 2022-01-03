import { useState } from "react";

function Counter() {
  const [value, setValue] = useState(0);
  const [color, setColor] = useState("red");

  const handlePlus = () => {
    // setValue(value + 1);
    setValue((prevValue) => prevValue + 1);
  };

  const handleMinus = () => {
    // setValue(value - 1);
    setValue((prevValue) => prevValue - 1);
  };

  const handleGreen = () => {
    //setColor("green");
    setColor(() => "green");
  };

  const handleBlue = () => {
    //setColor("blue");
    setColor(() => "blue");
  };

  const handleRed = () => {
    //setColor("red");
    setColor(() => "Red");
  };
  return (
    <div>
      <h2>Counter</h2>
      <div style={{ ...defaultStyle, backgroundColor: color }}>{value}</div>
      <h3>
        <button onClick={handlePlus}>+</button>
        <button onClick={handleMinus}>-</button>
        <button onClick={handleGreen}>green</button>
        <button onClick={handleBlue}>blue</button>
        <button onClick={handleRed}>red</button>
      </h3>
    </div>
  );
}

const defaultStyle = {
  width: "100px",
  height: "100px",
  borderRadius: "50px",
  lineHeight: "100px",
  textAlign: "center",
  display: "inline-block",
  fontSize: "3rem",
  userSelect: "none",
};

export default Counter;
