import { useState } from "react";

function reducer(action, prevState) {
  const { type, amount } = action;
  if (type === "PLUS") {
    return prevState + amount;
  } else if (type === "MINUS") {
    return prevState - amount;
  }
  // else if (type === "CHANGE_COLOR") {
  //   return { prevState, color: color };
  // }
  return prevState;
}

function reducer_color(action, prevState) {
  const { type, color } = action;

  if (type === "CHANGE_COLOR") {
    return color;
  }
  return prevState;
}

function Counter() {
  const [value, setValue] = useState(0);
  const [color, setColor] = useState("red");

  const handlePlus = () => {
    const action = { type: "PLUS", amount: 1 };
    setValue((prevValue) => {
      return reducer(action, prevValue);
    });
  };

  const handleMinus = () => {
    const action = { type: "MINUS", amount: 1 };
    setValue((prevValue) => {
      return reducer(action, prevValue);
    });
  };

  const handleGreen = () => {
    const action = { type: "CHANGE_COLOR", color: "green" };
    setColor((prevValue) => {
      return reducer_color(action, prevValue);
    });
  };

  const handleBlue = () => {
    const action = { type: "CHANGE_COLOR", color: "blue" };
    setColor((prevValue) => {
      return reducer_color(action, prevValue);
    });
  };

  const handleRed = () => {
    const action = { type: "CHANGE_COLOR", color: "red" };
    setColor((prevValue) => {
      return reducer_color(action, prevValue);
    });
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
